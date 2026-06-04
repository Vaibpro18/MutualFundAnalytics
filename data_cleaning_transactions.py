import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

# Standardize transaction type
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

# Check invalid amount
invalid_amount = df[df["amount_inr"] <= 0]

print("\nInvalid Amount Rows:")
print(len(invalid_amount))

# Check KYC values
print("\nKYC Status Values:")
print(df["kyc_status"].unique())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("\nCleaned Shape:", df.shape)
print("Saved Successfully!")