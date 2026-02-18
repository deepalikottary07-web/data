import json
import pandas as pd

# Load JSON file
with open("jala.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# If JSON is a list of products
df = pd.DataFrame(data)

# See all column names (important)
print("Columns in JSON:")
print(df.columns)

# 🔹 Change 'category' below if your column name is different
category_column = "category"

# Count products per category
category_count = df[category_column].value_counts()

print("\nCategory Counts:")
print(category_count)
