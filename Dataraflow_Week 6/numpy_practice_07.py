import numpy as np

print("--- Practice 1: Advanced Arithmetic & Broadcasting ---")
a = np.arange(9, dtype=np.float_).reshape(3, 3)
b = np.array([10, 10, 10])
print("Original Matrix a:\n", a)
print("Addition with b:\n", np.add(a, b))
print("Power (a^2):\n", np.power(a, 2))

print("\n--- Practice 2: Statistical Functions ---")
data = np.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])
print("Array:\n", data)
print("Minimum along axis 1 (rows):", np.amin(data, axis=1))
print("Peak-to-peak (ptp) overall:", np.ptp(data))
print("Median along axis 0 (columns):", np.median(data, axis=0))

print("\n--- Practice 3: Weighted Average ---")
arr = np.array([1, 2, 3, 4])
weights = np.array([4, 3, 2, 1])
weighted_avg, total_weights = np.average(arr, weights=weights, returned=True)
print("Weighted Average:", weighted_avg)
print("Sum of Weights:", total_weights)