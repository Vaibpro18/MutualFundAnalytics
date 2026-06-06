# Mutual Fund Analytics

Capstone Project - Bluestock Fintech

# Day 1

## Project Setup & Data Ingestion (ETL)

### Work Completed

* Created project structure and Git repository
* Loaded and explored mutual fund datasets
* Fetched live NAV data using MFAPI
* Validated AMFI codes and scheme data
* Generated data quality summary

### Deliverables

* data_ingestion.py
* live_nav_fetch.py
* amfi_validation.py
* requirements.txt

### Key Findings

* Successfully collected and validated mutual fund data.
* Verified AMFI mappings and NAV availability.


# Day 2

## Data Cleaning & SQL Database Design

### Work Completed

* Cleaned and standardized datasets
* Handled missing values and duplicates
* Designed SQLite database schema
* Loaded cleaned data into SQLite
* Created analytical SQL queries
* Prepared data dictionary

### Deliverables

* data_cleaning.py
* data_cleaning_transactions.py
* schema.sql
* queries.sql
* data_dictionary.md

### Key Findings

* Improved data quality and consistency.
* Built a structured database for analysis.


# Day 3

## Exploratory Data Analysis (EDA)

### Work Completed

* Performed comprehensive EDA on mutual fund datasets
* Analyzed NAV and SIP trends
* Conducted AUM growth analysis
* Examined investor demographics and geographic distribution
* Analyzed fund category and sector allocation patterns
* Performed risk vs return analysis
* Studied top holdings across mutual funds
* Generated correlation and distribution analyses
* Created interactive reports and visualizations
* Documented insights and conclusions

### Deliverables

* EDA_Analysis.ipynb
* 15+ Charts and Visualizations
* PNG Reports
* Interactive HTML Reports

### Key Findings

* Equity funds dominated overall AUM growth.
* SIP inflows showed consistent long-term growth.
* Risk-return profiles varied significantly across fund categories.
* Sector allocation and top holdings revealed portfolio concentration trends.


# Day 4

## Performance Analytics

Performed advanced mutual fund performance evaluation using risk-adjusted metrics and benchmark comparison.

### Analysis Completed

- CAGR (Compound Annual Growth Rate) analysis
- Maximum Drawdown analysis
- Sharpe Ratio analysis
- Sortino Ratio analysis
- Alpha and Beta calculation
- Benchmark comparison against NIFTY50 and NIFTY100
- Tracking Error analysis
- Fund performance scorecard generation
- Risk-adjusted performance evaluation
- Generated performance reports and visualizations

### Deliverables

- Performance_Analytics.ipynb
- alpha_beta.csv
- sharpe_ratio.csv
- sortino_ratio.csv
- tracking_error.csv
- fund_scorecard.csv
- benchmark_comparison.png
- alpha_comparison.png
- beta_comparison.png
- cagr_comparison.png
- max_drawdown.png

### Key Insights

- Kotak Bluechip and Nippon Largecap showed strong long-term growth.
- Benchmark comparison highlighted differences between active fund management and passive indices.
- Tracking error analysis measured benchmark-following efficiency.
- Risk-adjusted metrics provided a more complete picture than returns alone.