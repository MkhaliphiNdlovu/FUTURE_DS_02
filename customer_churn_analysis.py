# Task 2 - Customer Retention & Churn Analysis
import pandas as pd
import os

# Load dataset
df = pd.read_csv("data/churn.csv")
df.head()
df.info() #checking structure
df.isnull().sum() # Checking missing values

# Convert TotalCharges
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

df = df.dropna() # Drop missing values
churn_rate = df['Churn'].value_counts(normalize=True) * 100
print(churn_rate)

#import visualization libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Plot churn distribution (Yes vs No
sns.countplot(data=df, x='Churn')
plt.title("Customer Churn Distribution")
plt.show()

#Plot churn by contract type (Month-to-month, One year, Two year)
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='Contract', hue='Churn')
plt.title("Churn by Contract Type")
plt.show()

#Boxplot of tenure vs churn
sns.boxplot(data=df, x='Churn', y='tenure')
plt.title("Tenure vs Churn")
plt.show()

#create tenure groups
df['tenure_group'] = pd.cut(df['tenure'], bins=[0,12,24,48,72], labels=['0-1yr','1-2yr','2-4yr','4+yr'])

# cohort analysis:churn rate by tenure group
cohort = df.groupby(['tenure_group','Churn']).size().unstack()
cohort_percent = cohort.div(cohort.sum(axis=1), axis=0) * 100
print(cohort_percent)

# Heatmap of churn rate by tenure cohort
sns.heatmap(cohort_percent, annot=True, cmap="Blues")
plt.title("Churn Rate by Customer Tenure Cohort")
plt.show()

import numpy as np

df['Churn_num'] = df['Churn'].map({'Yes':1, 'No':0})

#select numeric columns
numeric_cols = df.select_dtypes(include=np.number)

# Corelation of numeric features with churn
correlation = numeric_cols.corr()['Churn_num'].sort_values(ascending=False)
print(correlation)
