import numpy as np

print("--- Practice 1: Splitting 1-D Arrays ---")
arr = np.array([1, 2, 3, 4, 5, 6])
split_3 = np.array_split(arr, 3)
print("Split into 3 parts:", split_3)
print("Access first split:", split_3[0])

print("\n--- Practice 2: Splitting 2-D Arrays Along Columns (axis=1) ---")
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
split_cols = np.array_split(matrix, 3, axis=1)
print("Split along columns (axis=1):\n", split_cols)


print("\n--- Practice 3: Split Helper Functions (hsplit) ---")
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
print("Horizontal split into 3:\n", np.hsplit(matrix, 3))

print("\n--- Practice 4: Searching with where() ---")
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print("Indices where value is 4:", x)

print("\n--- Practice 5: searchsorted() ---")
sorted_arr = np.array([6, 7, 8, 9])
print("Insertion index for 7:", np.searchsorted(sorted_arr, 7))
print("Insertion index for 7 (side='right'):", np.searchsorted(sorted_arr, 7, side='right'))

print("\n--- Practice 6: Sorting Arrays ---")
unsorted = np.array([3, 2, 0, 1])
print("Sorted numeric array:", np.sort(unsorted))

unsorted_2d = np.array([[3, 2, 4], [5, 0, 1]])
print("Sorted 2-D array (row-by-row):\n", np.sort(unsorted_2d))