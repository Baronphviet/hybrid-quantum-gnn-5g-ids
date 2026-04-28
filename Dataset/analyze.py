import csv
from collections import Counter
import sys

try:
    with open('tron.csv', mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        
        num_cols = len(header)
        num_rows = 0
        class_counter = Counter()
        label_counter = Counter()
        
        # Identify index of 'class' and 'label' if they exist
        class_idx = header.index('class') if 'class' in header else -1
        label_idx = header.index('label') if 'label' in header else -1
        
        for row in reader:
            num_rows += 1
            if class_idx != -1 and class_idx < len(row):
                class_counter[row[class_idx]] += 1
            if label_idx != -1 and label_idx < len(row):
                label_counter[row[label_idx]] += 1
                
    print("=== Basic Info ===")
    print(f"Total Rows: {num_rows}")
    print(f"Total Columns: {num_cols}")
    
    print("\n=== Class Distribution ===")
    for k, v in class_counter.most_common():
        print(f"  {k}: {v}")
        
    print("\n=== Label Distribution ===")
    for k, v in label_counter.most_common():
        print(f"  {k}: {v}")

except Exception as e:
    print(f"Error: {e}")
