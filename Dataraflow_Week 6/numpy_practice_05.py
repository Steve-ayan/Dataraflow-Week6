import numpy as np

print("--- Practice 1: In-place Resizing with .shape ---")
a = np.array([[1, 2, 3], [4, 5, 6]])
print("Original shape:", a.shape)
a.shape = (3, 2)
print("Resized in-place to (3, 2):\n", a)

print("\n--- Practice 2: arange and ndim ---")
seq_arr = np.arange(24)
print("1-D sequence length:", len(seq_arr), "Dimensions:", seq_arr.ndim)

tensor_3d = seq_arr.reshape(2, 4, 3)
print("Reshaped to 3-D (2, 4, 3) with ndim:", tensor_3d.ndim)

print("\n--- Practice 3: Zeros and Ones ---")
print("Zeros (default float):\n", np.zeros(5))
print("Ones (default float):\n", np.ones(5))

print("--- Practice 4: np.asarray and Element-wise Math ---")
py_list = [1, 2, 3]
arr_as = np.asarray(py_list)
print("Using asarray:", arr_as)

matrix = np.array([[1, 2, 3], [4, 1, 5]])
print("Original Matrix:\n", matrix)
print("Matrix + 3:\n", matrix + 3)
print("Matrix * 2:\n", matrix * 2)

print("\n--- Practice 5: Explicit slice() Object ---")
a = np.arange(10)
s = slice(2, 7, 2)
print("Using explicit slice object (a[2:7:2]):", a[s])