"""
Practice Script: Matplotlib Part 9 — Histograms
Course: Dataraflow Week 8
Description: Demonstrates creating histograms using plt.hist() with custom bins.
"""

import matplotlib.pyplot as plt

# Define dataset variables for ages and bin intervals
ages = [22, 55, 62, 45, 21, 22, 99, 34, 42, 4, 102, 110, 27, 48, 99, 84]
bins = [0, 20, 40, 60, 80, 100, 120]

# Create the histogram
plt.hist(ages, bins)

# Add labels and title
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Current ages of people')

# Save the plot image to disk with 500 DPI
plt.savefig('hist.png', dpi=500)

# Display the histogram window
plt.show()