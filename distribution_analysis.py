import numpy as np
import matplotlib.pyplot as plt
 
np.random.seed(42) 

salaries = np.random.normal(
    loc=50000,      
    scale=10000,    
    size=100
)

salaries = salaries.astype(int)


mean_salary = np.mean(salaries)
median_salary = np.median(salaries)
std_salary = np.std(salaries)


z_scores = np.abs((salaries - mean_salary) / std_salary)
outliers = salaries[z_scores > 2]


plt.figure(figsize=(8, 5))
plt.hist(salaries, bins=10)
plt.axvline(mean_salary, linestyle='--', linewidth=2, label=f"Mean: {mean_salary:.2f}")
plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.legend()
plt.tight_layout()


plt.savefig("salary_distribution.png")
plt.close()

# Report
print("===== Salary Distribution Analysis =====")
print(f"Total Employees      : {len(salaries)}")
print(f"Mean Salary          : {mean_salary:.2f}")
print(f"Median Salary        : {median_salary:.2f}")
print(f"Standard Deviation   : {std_salary:.2f}")
print(f"Outliers Detected    : {len(outliers)}")

if len(outliers) > 0:
    print("Outlier Salaries:")
    print(outliers)
else:
    print("No Outliers Found")

print("\nChart saved as salary_distribution.png")