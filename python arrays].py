import numpy as np

a2d = np.random.randint(0,101, size=(5,5), dtype=int)
print("Random 5x5 2D array:")
print(a2d)
print(a2d[1, 2])
array_sum = np.sum(a2d)
print("sum of array: ", array_sum)
array_mean = np.mean(a2d, axis = 1)
print("mean rows in array: ", array_mean)
array_max = np.max(a2d, axis = 1)
print("max rows in array: ", array_max)