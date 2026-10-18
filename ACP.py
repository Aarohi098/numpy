import numpy as np
data_type = int
nums = [5, 7, 3, 6]
array = np.array(nums, dtype=data_type)
print("Original Array: ")
print(array)
print("All numbers added up: ")
print(np.sum(array))
print("All numbers multiplied: ")
print(np.prod(array))
print("Average of this array: ")
print(np.mean(array))
