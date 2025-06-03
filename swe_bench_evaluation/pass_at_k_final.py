import json
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter


k = 2

totalInstances = 52 ## 300 for full SWE-bench Lite. We ran 52 issues

resolvedInstances = {}

pass_at_k = []

for i in range(1,k+1):


    ## Change to swe_bench_results/swe_bench_results_MFT_P{i}.json for fine-tuned model
    filename = f"swe_bench_results/swe_bench_results_MB_P{i}.json"
    # Open the JSON file
    try: 
        with open(filename, 'r') as file:
            results = json.load(file)
            # print("File opened")
    except FileNotFoundError:
        print(f"{filename} not found.")
    

    for instance in results["resolved_ids"]:
        if (instance in resolvedInstances.keys()):
            continue
        else:
            resolvedInstances[instance] = 1
    
    pass_at_k.append(len(resolvedInstances) / totalInstances)



    print(f"pass@{i}: {pass_at_k[i-1]:.2%}")

# Plotting the pass@k chart
plt.figure(figsize=(8, 6))
plt.plot(range(1, k+1), pass_at_k, marker='o', linestyle='-', color='blue')
plt.xlabel('k')
plt.ylabel('Pass@k')
plt.title('Pass@k with Base Model')
plt.ylim(0, 0.2)  # Since pass@k is a fraction
plt.grid(True)

# Ensure only 1 and 2 are on the x-axis
plt.xticks(range(1, k+1))

# Format the y-axis as percentages
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))

plt.show()



    











































# data[0].instance_id
# data[0].prediction

# # Print the contents
# print(data)

# candidate_solutions = data


# def calculate_pass_at_k(problems_dataset, model, k):
#     num_solved = 0

#     for problem_instance in problems_dataset:
#         # problem_description = problem_instance["description"]
#         # test_cases = problem_instance["test_cases"]

#         # candidate_solutions = model.generate_solutions(problem_description, num_solutions=k)
#         solved_this_problem = False

#         for solution in candidate_solutions:
#             try:
#                 #validate or something
#                 if run_unit_tests(solution.prediction, test_cases):
#                     solved_this_problem = True
#                     break  # One successful solution is enough
#             except Exception as e:
#                 # Handle execution errors, timeouts, etc.
#                 print(f"Error running solution for problem {candidate_solutions.instance_id}: {e}")
#                 continue

#         if solved_this_problem:
#             num_solved += 1

#     return num_solved / len(problems_dataset)

