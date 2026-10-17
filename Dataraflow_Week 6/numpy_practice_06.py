import numpy as np

print("--- Practice 1: 2-D Subsetting & Slicing ---")
a = np.array([[1, 2, 3], [3, 4, 5]])
print("Original 2-D Array:\n", a)

print("First row (a[0]):", a[0])
print("First element of first row (a[0][0]):", a[0][0])
print("Slicing elements in first row (a[0][1:2]):", a[0][1:2])

print("\n--- Practice 2: 2-D Arithmetic ---")
print("Array + 3:\n", a + 3)
print("Array * 2:\n", a * 2)