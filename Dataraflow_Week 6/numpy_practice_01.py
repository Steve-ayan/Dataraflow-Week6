import numpy as np

print("--- Challenge 1: Version Check ---")
print("NumPy Version:", np.__version__)

print("\n--- Challenge 2: 0-D Array (Scalar) ---")
scalar_arr = np.array(100)
print("Value:", scalar_arr)
print("Type:", type(scalar_arr))
print("Dimensions (.ndim):", scalar_arr.ndim)

print("\n--- Challenge 3: 1-D Array from a Tuple ---")
my_tuple = (10, 20, 30, 40, 50)
tuple_arr = np.array(my_tuple)
print("Array from tuple:", tuple_arr)
print("Type:", type(tuple_arr))

print("\n--- Challenge 4: Type Inspection ---")
my_list = [1, 2, 3]
my_arr = np.array([1, 2, 3])
print("Python list type:", type(my_list))
print("NumPy array type:", type(my_arr))

print("\n--- Challenge 5: 2-D and 3-D Arrays ---")
# 2-D Array
matrix_arr = np.array([[1, 2, 3], [4, 5, 6]])
print("2-D Array:\n", matrix_arr)
print("2-D Dimensions (.ndim):", matrix_arr.ndim)

# 3-D Array
tensor_arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("3-D Array:\n", tensor_arr)
print("3-D Dimensions (.ndim):", tensor_arr.ndim)


print("\n--- Challenge 6: ndim and ndmin ---")
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print("Dimensions of a:", a.ndim)
print("Dimensions of b:", b.ndim)
print("Dimensions of c:", c.ndim)
print("Dimensions of d:", d.ndim)

# Forcing a 5-D array
high_dim_arr = np.array([1, 2, 3, 4], ndmin=5)
print("Forced 5-D Array:\n", high_dim_arr)
print("Verified Dimensions:", high_dim_arr.ndim)