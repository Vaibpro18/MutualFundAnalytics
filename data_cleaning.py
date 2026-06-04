import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Original Shape:", df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Validate returns
return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Check expense ratio
invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nInvalid Expense Ratio Rows:")
print(len(invalid_expense))

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned data
df.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("\nCleaned Shape:", df.shape)
print("Saved Successfully!")