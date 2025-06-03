import os
from datasets import load_dataset

def load_or_download_dataset(dataset_path: str, split: str = "test", local_dir: str = "./datasets"):
    """
    Loads a dataset from local JSON if available, otherwise downloads it from Hugging Face
    and saves it locally for future use.

    Args:
        dataset_path (str): The Hugging Face dataset path (e.g., "esquivelgor/F1_SBL_T_60").
        split (str): The dataset split to load (e.g., "train", "test", "validation").
        local_dir (str): Directory to store or look for local JSON files.

    Returns:
        Dataset: A HuggingFace Dataset object.
    """
    local_file = os.path.join(local_dir, f"{dataset_path}.json")

    if os.path.exists(local_file):
        print(f"📂 Loading dataset from local file: {local_file}")
        dataset = load_dataset("json", data_files={split: local_file})[split]
    else:
        print(f"⬇️  Downloading dataset from Hugging Face: {dataset_path} ({split})")
        dataset = load_dataset(dataset_path, split=split)

        os.makedirs(local_dir, exist_ok=True)
        dataset.to_json(local_file)
        print(f"💾 Saved to: {local_file}")

    return dataset

def save2Local(dataset, local_path, dataset_id, n, split="T"):
    """
    Save a dataset to a JSON file if it doesn't already exist.

    Args:
        dataset (Dataset or pd.DataFrame): The dataset to save.
        local_path (str): Directory where the JSON will be stored.
        dataset_id (str): Base name identifier for the dataset.
        n (str): Number of elements in the dataset.
        split (str): Dataset split suffix (e.g., "T" for test).
    """
    dataset_name = f"{dataset_id}_{split}_{n}"
    file_path = os.path.join(local_path, f"{dataset_name}.json")

    if not os.path.exists(file_path):
        dataset.to_json(file_path)
        print(f"✅ Dataset saved to {file_path}")
    else:
        print(f"⚠️ File already exists at {file_path}")

