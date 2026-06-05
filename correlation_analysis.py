import pandas as pd
import matplotlib.pyplot as plt


employees = {
    "id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "age": [22, 25, 28, 30, 35, 40, 26, 29, 32, 45],
    "salary": [25000, 30000, 35000, 45000, 50000, 70000, 38000, 42000, 52000, 85000],
    "experience": [1, 2, 3, 5, 7, 12, 2, 4, 6, 15]
}

df = pd.DataFrame(employees)


correlation_matrix = df[["age", "salary", "experience"]].corr()

print("===== CORRELATION MATRIX =====")
print(correlation_matrix)


correlation_matrix.to_csv("correlation_matrix.csv")


plt.figure(figsize=(6, 5))
plt.imshow(correlation_matrix, cmap="coolwarm")

plt.colorbar(label="Correlation")

plt.xticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns
)

plt.yticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns
)

for i in range(len(correlation_matrix)):
    for j in range(len(correlation_matrix)):
        plt.text(
            j,
            i,
            f"{correlation_matrix.iloc[i, j]:.2f}",
            ha="center",
            va="center"
        )

plt.title("Employee Correlation Matrix")
plt.tight_layout()


plt.savefig("correlation_matrix.png")
plt.show()

print("\nFiles Generated:")
print("1. correlation_matrix.csv")
print("2. correlation_matrix.png")