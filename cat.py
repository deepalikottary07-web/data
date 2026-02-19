import json
import pandas as pd

# Load JSON file
with open("jala.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# JSON is already a list
df = pd.DataFrame(data)

print("Columns in JSON:")
print(df.columns)

category_column = "category"

category_count = df[category_column].value_counts()

print("\nCategory Counts:")
print(category_count)
