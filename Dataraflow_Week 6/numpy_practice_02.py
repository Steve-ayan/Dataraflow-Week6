import numpy as np

print("--- Practice 1: Accessing 1-D Elements ---")
arr = np.array([10, 20, 30, 40, 50])

# TODO: Print the first element (index 0) of 'arr'


# TODO: Print the fourth element (index 3) of 'arr'


print("\n--- Practice 2: Arithmetic with Indexes ---")
# TODO: Add the second element and the fifth element together and print the result

print("\n--- Practice 3: 2-D and 3-D Indexing ---")
# 2-D Array Access
matrix = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("2nd element on 1st row:", matrix[0, 1])  # Output: 2
print("5th element on 2nd row:", matrix[1, 4])  # Output: 10

# 3-D Array Access
tensor = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("Element at [0, 1, 2]:", tensor[0, 1, 2])  # Output: 6

print("\n--- Practice 4: Negative Indexing and Slicing ---")
# Negative Indexing
matrix = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("Last element from 2nd row:", matrix[1, -1])  # Output: 10

# 1-D Slicing
arr_1d = np.array([1, 2, 3, 4, 5, 6, 7])
print("Index 1 to 5:", arr_1d[1:5])       # Output: [2 3 4 5]
print("Every other element:", arr_1d[::2])  # Output: [1 3 5 7]

# 2-D Slicing
print("Row 1, columns 1 to 4:", matrix[1, 1:4])  # Output: [7 8 9]
print("Both rows, column index 2:", matrix[0:2, 2]) # Output: [3 8]
print("Sub-matrix (both rows, cols 1-4):\n", matrix[0:2, 1:4])


print("--- Practice 5: Data Types and astype() ---")
arr_float = np.array([1.1, 2.2, 3.3])
arr_int = arr_float.astype(int)
print("Original Float Array:", arr_float, arr_float.dtype)
print("Casted Int Array:", arr_int, arr_int.dtype)

print("\n--- Practice 6: Copy vs. View ---")
original = np.array([1, 2, 3, 4, 5])
c = original.copy()
v = original.view()

# Modify original
original[0] = 99
print("Original modified to 99:", original)
print("Copy (unaffected):", c)
print("View (affected):", v)

# Check .base attribute
print("Copy base (should be None):", c.base)
print("View base (should show original):", v.base)