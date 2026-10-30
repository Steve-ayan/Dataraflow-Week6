"""
Practice Script: Matplotlib Part 1 — Basic Line Plot
Course: Dataraflow Week 8
Description: Recreates the tutorial script to plot daily YouTube views using matplotlib.
"""

import matplotlib.pyplot as plt

# Define sample data
x = [1, 2, 3, 4, 5, 6, 7]                  # Week days[cite: 9]
y = [964, 287, 42, 390, 64, 800, 523]       # Views[cite: 9]

# Create line plot with labels and titles
plt.plot(x, y, label='Youtube views')       #[cite: 9]
plt.xlabel('Week days')                     #[cite: 9]
plt.ylabel('Views')                         #[cite: 9]
plt.title('Youtube views on daily basis')   #[cite: 9]
plt.legend(loc='upper left')                #[cite: 9]

# Display the chart window
plt.show()                                  #[cite: 9]