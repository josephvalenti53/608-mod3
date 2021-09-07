import statistics

print('Data Set = 1,3,4,2,6,5,3,4,5,2')

pop_variance = statistics.pvariance([1, 3, 4, 2, 6, 5, 3, 4, 5, 2])

print('Population Variance =', pop_variance)

pop_std_dev = statistics.pstdev([1, 3, 4, 2, 6, 5, 3, 4, 5, 2])

print('Population Standard Deviation =', pop_std_dev)
