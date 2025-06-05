import asyncio
import os
import subprocess
import modal
import httpx

MODEL_DIR = "/ollama_models"
MODELS_TO_DOWNLOAD = ["hf.co/esquivelgor/SWE_QwenOOP_Model_q4_k_m:Q4_K_M"]
OLLAMA_VERSION = "0.6.5"
OLLAMA_PORT = 11434

# Modal image setup
ollama_image = (
    modal.Image.debian_slim(python_version="3.11")
    .apt_install("curl", "ca-certificates")
    .pip_install(
        "httpx==0.27.0",          # ✅ Add this line
        "fastapi==0.115.8",
        "uvicorn[standard]==0.34.0",
        "openai~=1.30"
    )
    .run_commands(
        f"OLLAMA_VERSION={OLLAMA_VERSION} curl -fsSL https://ollama.com/install.sh | sh",
        f"mkdir -p {MODEL_DIR}",
    )
    .env({
        "OLLAMA_HOST": f"0.0.0.0:{OLLAMA_PORT}",
        "OLLAMA_MODELS": MODEL_DIR,
    })
)


model_volume = modal.Volume.from_name("ollama-models-store", create_if_missing=True)
app = modal.App("ollama-server-fast", image=ollama_image)

@app.cls(
    gpu="H100",
    volumes={MODEL_DIR: model_volume},
    timeout=60 * 12,
    min_containers=1,
)
@modal.concurrent(max_inputs=8, target_inputs=4)
class OllamaServer:
    ollama_process: subprocess.Popen | None = None

    @modal.enter()
    async def start_ollama(self):
        print("🟡 Starting Ollama server...")
        env = os.environ.copy()
        env["OLLAMA_CONTEXT_LENGTH"] = "14000"  # reduce from 45k for speed
        self.ollama_process = subprocess.Popen(["ollama", "serve"], env=env)
        await asyncio.sleep(10)
        print("🟢 Ollama server ready.")

        # Download the model if not already present
        model = MODELS_TO_DOWNLOAD[0]
        list_proc = subprocess.run(["ollama", "list"], capture_output=True, text=True)
        if model not in list_proc.stdout:
            print(f"📦 Pulling model: {model}")
            pull_proc = await asyncio.create_subprocess_exec("ollama", "pull", model)
            if await pull_proc.wait() != 0:
                raise RuntimeError(f"❌ Model pull failed: {model}")
            print(f"✅ Model pulled: {model}")
        else:
            print(f"📁 Model already available: {model}")

        # Warm-up inference
        try:
            print("🔥 Warming up model...")
            async with httpx.AsyncClient() as client:
                resp = await client.post(f"http://localhost:{OLLAMA_PORT}/api/generate", json={
                    "model": model,
                    "prompt": "Hello!",
                }, timeout=30.0)
                if resp.status_code == 200:
                    print("✅ Warm-up response:", resp.json().get("response", "").strip())
                else:
                    print(f"⚠️ Warm-up failed: {resp.status_code} - {resp.text}")
        except Exception as e:
            print(f"Warm-up exception: {e}")

    @modal.exit()
    def stop_ollama(self):
        if self.ollama_process and self.ollama_process.poll() is None:
            self.ollama_process.terminate()
            try:
                self.ollama_process.wait(timeout=10)
                print("🛑 Ollama server stopped.")
            except subprocess.TimeoutExpired:
                self.ollama_process.kill()
                print("🧨 Ollama server force-killed.")
        else:
            print("🔚 Ollama already terminated.")

    @modal.method()
    async def infer(self, prompt: str) -> str:
        model = MODELS_TO_DOWNLOAD[0]
        async with httpx.AsyncClient() as client:
            resp = await client.post(f"http://localhost:{OLLAMA_PORT}/api/generate", json={
                "model": model,
                "prompt": prompt,
            }, timeout=60.0)
            if resp.status_code == 200:
                return resp.json().get("response", "").strip()
            return f"❌ Error: {resp.status_code} - {resp.text}"

    @modal.web_server(port=OLLAMA_PORT, startup_timeout=180)
    def serve(self):
        print(f"🌐 Serving Ollama API on port {OLLAMA_PORT}")

