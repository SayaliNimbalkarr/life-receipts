import pandas as pd

df = pd.read_csv("data/sample_logs.csv", on_bad_lines='skip')
print(df.head())  # Shows first 5 rows
