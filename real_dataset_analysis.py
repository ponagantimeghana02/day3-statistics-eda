import pandas as pd
import matplotlib.pyplot as plt

# Read Dataset
df = pd.read_csv("customers.csv")

print("========== CUSTOMER DATA ==========")
print(df.head())

# -----------------------------------
# DATA CLEANING
# -----------------------------------

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== DUPLICATES ==========")
print("Duplicate Records:", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values (if any)
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Annual_Income_(k$)"] = df["Annual_Income_(k$)"].fillna(
    df["Annual_Income_(k$)"].mean()
)
df["Spending_Score"] = df["Spending_Score"].fillna(
    df["Spending_Score"].mean()
)

print("\nData Cleaning Completed!")

# -----------------------------------
# STATISTICAL SUMMARY
# -----------------------------------

print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())

# -----------------------------------
# CORRELATION ANALYSIS
# -----------------------------------

print("\n========== CORRELATION MATRIX ==========")

correlation = df[
    ["Age", "Annual_Income_(k$)", "Spending_Score"]
].corr()

print(correlation)

# -----------------------------------
# VISUALIZATION 1
# AGE DISTRIBUTION
# -----------------------------------

plt.figure(figsize=(8, 5))
plt.hist(df["Age"], bins=10)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.show()

# -----------------------------------
# VISUALIZATION 2
# INCOME VS SPENDING SCORE
# -----------------------------------

plt.figure(figsize=(8, 5))
plt.scatter(
    df["Annual_Income_(k$)"],
    df["Spending_Score"]
)
plt.title("Income vs Spending Score")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score")
plt.show()

# -----------------------------------
# VISUALIZATION 3
# GENDER DISTRIBUTION
# -----------------------------------

plt.figure(figsize=(6, 6))
df["Genre"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.title("Gender Distribution")
plt.ylabel("")
plt.show()

# -----------------------------------
# INSIGHTS REPORT
# -----------------------------------

print("\n========== INSIGHTS REPORT ==========")

print(f"Total Customers: {len(df)}")

print(
    f"Average Age: {df['Age'].mean():.2f}"
)

print(
    f"Average Annual Income: {df['Annual_Income_(k$)'].mean():.2f} k$"
)

print(
    f"Average Spending Score: {df['Spending_Score'].mean():.2f}"
)

highest_spender = df.loc[
    df["Spending_Score"].idxmax()
]

print("\nHighest Spending Customer:")
print(highest_spender)

print("\nProject Completed Successfully!")