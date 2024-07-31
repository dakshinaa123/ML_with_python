import numpy as np

# Creating a 1D array
arr1 = np.array([1,2,3,4,5])
print(arr1)

# Creating a 2D array
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2)

# Creating zero array
zeros_aray = np.zeros((3, 3))
print(zeros_aray)

# Arange function
range_array = np.arange(0,10,2)
print(range_array)

# Linspace
linspace_array = np.linspace(0,1,5)
print(linspace_array)

# Identity matrix
identity_matrix = np.eye(3)
print(identity_matrix)

# Random.Rand and Random.RandInt
random_array = np.random.rand(3)
print(random_array)
random_array1 = np.random.randint(3)
print(random_array1)

# Basic Operation
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

# ADDITION
result_add = arr1 + arr2
print(result_add)

# SUBTRACTION
result_subtract = arr1 - arr2
print(result_subtract)

# MULTIPLICATION
result_multiply = arr1 * arr2
print(result_multiply)

# DIVISION
result_division = arr1 / arr2
print(result_division)

# Basic Functions
import numpy as np
arr = np.array([1,2,3,4,5])
sqrt = np.sqrt(arr)
exp = np.exp(arr)
mean = np.mean(arr)
add = np.sum(arr)
sin = np.sin(arr)
print(sqrt)
print(exp)
print(mean)
print(add)
print(sin)

# Dot and Element Multiplication
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,0])
dot = np.dot(arr1,arr2)
ele_mult = arr1 * arr2
print(dot)
print(ele_mult)

