import statistics

scores = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

mean_value = statistics.mean(scores)
median_value = statistics.median(scores)
try:
    mode_value = statistics.mode(scores)
except statistics.StatisticsError:
    mode_value = "No unique mode"

variance_value = statistics.variance(scores)
std_dev_value = statistics.stdev(scores)

print("Scores:", scores)
print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)
print("Variance:", variance_value)
print("Standard Deviation:", std_dev_value)