import numpy as np
data_type = [('name', 'S15'), ('class', int), ('height', float)]
student_details = [('James', 5, 48.5), ('Nail', 6, 52.2), ('Paul', 5, 42.1), ('Pit', 5, 40.11)]
#create a structured array
students = np.array(student_details, dtype=data_type)
print("Original Array: ")
print(students)
print("Sorted by height: ")
print(np.sort(students, order='height'))