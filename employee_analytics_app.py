import pandas as pd

employees = {
"id":[1,2,3,4,5,6,7,8,9,10],
"age":[22,25,28,30,35,40,26,29,32,45],
"salary":[25000,30000,35000,45000,50000,70000,38000,42000,52000,85000],
"experience":[1,2,3,5,7,12,2,4,6,15]
}

df = pd.DataFrame(employees)

while True:

    print("\n1. Dataset Summary")
    print("2. Salary Statistics")
    print("3. Correlation Analysis")
    print("4. Visualizations")
    print("5. Export Report")
    print("6. Exit")

    choice = input("Choice: ")

    if choice == "1":
        print(df.describe())

    elif choice == "2":
        print(df["salary"].describe())

    elif choice == "3":
        print(df.corr(numeric_only=True))

    elif choice == "4":
        print("Run visualizations.py")

    elif choice == "5":
        df.describe().to_csv(
            "dataset_summary.csv"
        )
        print("Report Exported")

    elif choice == "6":
        break