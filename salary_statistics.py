import statistics

salaries = [
    25000,
    30000,
    35000,
    40000,
    45000,
    50000,
    55000,
    60000,
    65000,
    70000
]

mean_salary = statistics.mean(salaries)
median_salary = statistics.median(salaries)
variance_salary = statistics.variance(salaries)
std_deviation = statistics.stdev(salaries)
highest_salary = max(salaries)
lowest_salary = min(salaries)

# Report
print("===== Salary Statistics Report =====")
print(f"Mean Salary          : {mean_salary:.2f}")
print(f"Median Salary        : {median_salary:.2f}")
print(f"Variance             : {variance_salary:.2f}")
print(f"Standard Deviation   : {std_deviation:.2f}")
print(f"Highest Salary       : {highest_salary}")
print(f"Lowest Salary        : {lowest_salary}")