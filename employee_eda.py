import pandas as pd

employees = {
"id":[1,2,3,4,5,6,7,8,9,10],
"age":[22,25,28,30,35,40,26,29,32,45],
"salary":[25000,30000,35000,45000,50000,70000,38000,42000,52000,85000],
"experience":[1,2,3,5,7,12,2,4,6,15]
}

df = pd.DataFrame(employees)

print("Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicates:")
print(df.duplicated().sum())