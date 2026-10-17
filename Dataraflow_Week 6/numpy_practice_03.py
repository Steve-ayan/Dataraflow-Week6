import numpy as np

print("--- Practice 1: Inspecting Shape ---")
arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("Shape of 2-D array:", arr_2d.shape)  # Output: (2, 4)

print("\n--- Practice 2: Reshaping 1-D to 2-D and 3-D ---")
arr_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Reshape to 4x3 matrix
matrix_4x3 = arr_1d.reshape(4, 3)
print("Reshaped to (4, 3):\n", matrix_4x3)

# Reshape to 3D (2, 3, 2)
tensor_232 = arr_1d.reshape(2, 3, 2)
print("Reshaped to (2, 3, 2):\n", tensor_232)

print("\n--- Practice 3: Check if Reshape is a View ---")
print("Base of reshaped array:", matrix_4x3.base)  # Returns original arr_1d

print("\n--- Practice 4: Unknown Dimension & Flattening ---")
arr_8 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
auto_reshaped = arr_8.reshape(2, 2, -1)
print("Reshaped with -1 (2, 2, 2):\n", auto_reshaped)

matrix = np.array([[1, 2, 3], [4, 5, 6]])
flat_arr = matrix.reshape(-1)
print("Flattened array:", flat_arr)

print("\n--- Practice 5: Iterating Multi-dimensional Arrays ---")
print("Iterating 2-D scalar elements with nested loops:")
for row in matrix:
    for scalar in row:
        print(scalar, end=" ")
print()


print("\n--- Practice 6: Advanced Iteration with nditer & ndenumerate ---")
tensor_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print("Using nditer to loop through all scalars:")
for x in np.nditer(tensor_3d):
    print(x, end=" ")
print()

print("\nUsing ndenumerate on a 2-D array:")
matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, val in np.ndenumerate(matrix):
    print(f"Index {idx} -> Value {val}")

print("\n--- Practice 7: Joining and Stacking ---")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Concatenate
concat_arr = np.concatenate((arr1, arr2))
print("Concatenated:", concat_arr)

# Hstack vs Vstack
print("Horizontal Stack (hstack):", np.hstack((arr1, arr2)))
print("Vertical Stack (vstack):\n", np.vstack((arr1, arr2)))