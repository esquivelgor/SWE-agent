import os
import array
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from parser import Parser, lex
from runner import is_oop_code


def analyze_file(filepath):
    with open(filepath, 'r') as f:
        code = f.read()
    try:
        tokens = lex(code)
        parser = Parser(tokens) 
        parse_result = parser.parse()
        oop = is_oop_code(parse_result)

    except Exception as e:
        # If parsing fails, treat as not OOP
        oop = False
    return oop

def bench_testing(testpath):
    results = []

    # Iterate over all .txt files in testpath
    for filename in os.listdir(testpath):
        if filename.endswith('.txt'):
            filepath = os.path.join(testpath, filename)
            oop_found = analyze_file(filepath)
            results.append({'filename': filename[:-4], 'is_oop': oop_found})
        if filename.endswith('.py'):
            filepath = os.path.join(testpath, filename)
            oop_found = analyze_file(filepath)
            results.append({'filename': filename[:-3], 'is_oop': oop_found})

    # Create dataframe
    df = pd.DataFrame(results)

    # Save to CSV
    df.to_csv('parser_results.csv', index=False)
    print(df)

    return df

def get_statistics(df, true_labels, visualize=False):
    import pandas as pd

    predicted_labels = df['is_oop'].astype(int)

    cm = pd.crosstab(pd.Series(true_labels, name='Actual'),
                     pd.Series(predicted_labels, name='Predicted'))

    print("\nConfusion Matrix:")
    print(cm)

    TP = cm.loc[1, 1] if (1 in cm.index and 1 in cm.columns) else 0
    TN = cm.loc[0, 0] if (0 in cm.index and 0 in cm.columns) else 0
    FP = cm.loc[0, 1] if (0 in cm.index and 1 in cm.columns) else 0
    FN = cm.loc[1, 0] if (1 in cm.index and 0 in cm.columns) else 0

    total = TP + TN + FP + FN
    accuracy = (TP + TN) / total if total > 0 else 0
    precision = TP / (TP + FP) if (TP + FP) > 0 else 0
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0
    f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    print("\nMetrics:")
    print(f"Accuracy:  {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"F1 Score:  {f1:.4f}")

    if visualize:
        try:
            import seaborn as sns
            import matplotlib.pyplot as plt
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
            plt.title('Confusion Matrix')
            plt.ylabel('Actual')
            plt.xlabel('Predicted')
            plt.show()
        except ImportError:
            print("Visualization libraries not installed. Skipping visualization.")

def main():
    tester_dir = 'tests'
    df = bench_testing(tester_dir)

    true_labels = [1] * 100

    if len(true_labels) != len(df):
        print(f"Warning: Number of ground truth labels ({len(true_labels)}) "
              f"does not match number of files parsed ({len(df)}). "
              "Confusion matrix may be invalid.")
    else:
        get_statistics(df, true_labels, visualize=True)

if __name__ == '__main__':
    main()

    

