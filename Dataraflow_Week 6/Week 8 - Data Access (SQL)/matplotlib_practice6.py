"""
Practice Script: Matplotlib Part 6 — Saving Plots to File
Course: Dataraflow Week 8
Description: Demonstrates saving plots to disk using plt.savefig() with custom DPI and background color.
"""

import matplotlib.pyplot as plt

# Define multi-platform dataset variables
y_views = [534, 690, 258, 402, 724, 689, 352]
f_views = [123, 342, 700, 305, 406, 648, 325]
t_views = [202, 209, 176, 415, 824, 389, 550]
days = [1, 2, 3, 4, 5, 6, 7]

# Plot multiple datasets
plt.plot(days, y_views, label='Youtube views', marker='o')
plt.plot(days, f_views, label='Facebook views', marker='o')
plt.plot(days, t_views, label='Twitter views', marker='o')

# Add labels, title, and legend
plt.xlabel('Days')
plt.ylabel('Views')
plt.title('Social media views for a channel')
plt.legend()

# Set custom limits and gridlines
plt.xlim(1, 5)
plt.ylim(100, 900)
plt.grid(True, color='r', linestyle='--')

# Save the plot image to disk with 500 DPI and a cyan background color
plt.savefig('img_2.png', dpi=500, facecolor='cyan')

# Display the chart window
plt.show()