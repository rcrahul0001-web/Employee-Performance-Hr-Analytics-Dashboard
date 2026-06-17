import pandas as pd

# Load dataset
df = pd.read_csv(
    r"C:\Users\Admin\Documents\employee\WA_Fn-UseC_-HR-Employee-Attrition.csv"
)

# Show missing values
print("Missing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Check dataset shape
print("\nDataset Shape:")
print(df.shape)

# Save cleaned dataset
df.to_csv("cleaned_employee_data.csv", index=False)

print("\nData cleaned successfully!")