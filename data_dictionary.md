# Data Dictionary

## 02_nav_history.csv

| Column | Description |
|---------|-------------|
| amfi_code | Unique AMFI scheme code |
| date | NAV date |
| nav | Net Asset Value of the scheme |

## 08_investor_transactions.csv

| Column | Description |
|---------|-------------|
| investor_id | Unique investor identifier |
| transaction_date | Date of transaction |
| amfi_code | Mutual fund scheme code |
| transaction_type | SIP, Lumpsum, or Redemption |
| amount_inr | Transaction amount in INR |
| kyc_status | Investor KYC verification status |

## 07_scheme_performance.csv

| Column | Description |
|---------|-------------|
| amfi_code | Mutual fund scheme code |
| return_1yr_pct | One-year return percentage |
| return_3yr_pct | Three-year return percentage |
| return_5yr_pct | Five-year return percentage |
| expense_ratio_pct | Annual expense ratio percentage |
| aum_crore | Assets under Management (Crore INR) |