# Customer Retention & Churn Analysis

## Project Overview

This project analyzes customer retention and churn behavior for a subscription-based business. The goal is to identify patterns associated with customer loss, understand retention drivers, estimate customer lifetime trends, and provide actionable business recommendations.

Customer retention is a critical metric for SaaS, fintech, edtech, and subscription-based companies because reducing churn directly improves revenue and long-term growth.

---

## Business Problem

Businesses need to understand:

* Why customers leave the platform
* Which customer segments are most likely to churn
* How long customers remain active
* What actions can improve retention and reduce customer loss

This analysis aims to provide data-driven insights that support strategic decision-making.

---

## Dataset

The project uses a customer subscription dataset containing:

* Customer demographics
* Subscription contract information
* Service usage details
* Billing information
* Customer tenure
* Churn status (Yes/No)

### Key Features

| Feature         | Description                       |
| --------------- | --------------------------------- |
| customerID      | Unique customer identifier        |
| gender          | Customer gender                   |
| SeniorCitizen   | Indicates senior citizen status   |
| tenure          | Number of months with the company |
| Contract        | Subscription contract type        |
| InternetService | Type of internet service          |
| MonthlyCharges  | Monthly subscription cost         |
| TotalCharges    | Total revenue generated           |
| Churn           | Customer churn status             |

---

## Project Objectives

* Perform data cleaning and preparation
* Analyze customer churn rates
* Investigate retention trends
* Conduct cohort analysis
* Explore customer lifetime patterns
* Identify major churn drivers
* Provide actionable business recommendations

---

## Tools & Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn (optional)
* VS Code

---

## Project Structure

```text
customer-retention-analysis/
│
├── data/
│   └── churn.csv
│
├── notebooks/
│   └── Customer_Retention_Analysis.ipynb
│
├── output/
│   ├── churn_distribution.png
│   ├── contract_churn.png
│   ├── tenure_analysis.png
│   └── cohort_heatmap.png
│
├── task.py
├── README.md
└── requirements.txt
```

---

## Analysis Performed

### 1. Data Cleaning

* Checked for missing values
* Converted numerical fields
* Removed invalid records
* Verified data consistency

### 2. Exploratory Data Analysis

* Customer churn distribution
* Customer demographics
* Service usage patterns
* Revenue analysis

### 3. Retention Analysis

* Customer tenure analysis
* Retention trend evaluation
* Churn segmentation

### 4. Cohort Analysis

Customers were grouped by tenure cohorts to evaluate retention performance over time.

### 5. Customer Lifetime Analysis

Estimated customer lifetime value using:

Estimated CLV = Average Monthly Revenue × Average Customer Tenure

### 6. Churn Driver Analysis

Investigated factors associated with churn, including:

* Contract type
* Monthly charges
* Internet service
* Customer tenure

---

## Key Findings

### Customer Churn

* Customers on month-to-month contracts exhibited the highest churn rates.
* Long-term contracts demonstrated stronger retention.

### Customer Tenure

* New customers were more likely to churn.
* Longer-tenure customers showed significantly higher retention.

### Revenue Insights

* Higher monthly charges were associated with increased churn risk.
* Retained customers generated substantially more lifetime value.

### Retention Drivers

* Long-term subscriptions improved retention.
* Customer longevity was strongly linked to reduced churn.

---

## Business Recommendations

### 1. Promote Long-Term Contracts

Offer discounts and incentives for annual or multi-year subscriptions.

### 2. Improve Customer Onboarding

Focus on customer engagement during the first 90 days when churn risk is highest.

### 3. Implement Retention Campaigns

Identify at-risk customers and provide personalized offers before cancellation.

### 4. Increase Customer Engagement

Develop loyalty programs and value-added services to strengthen customer relationships.

### 5. Monitor High-Risk Segments

Create dashboards that continuously track churn indicators and customer health metrics.

---

## Expected Business Impact

If customer churn is reduced:

* Revenue retention increases
* Customer lifetime value improves
* Acquisition costs decrease
* Long-term business growth becomes more sustainable

---

## Future Improvements

* Build a machine learning churn prediction model
* Develop an interactive Power BI dashboard
* Incorporate customer support and engagement data
* Implement automated churn risk scoring

---

## Author

Data Science & Analytics Internship Project

Customer Retention & Churn Analysis
