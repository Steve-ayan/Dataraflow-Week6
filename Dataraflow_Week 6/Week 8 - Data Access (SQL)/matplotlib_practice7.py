"""
Practice Script: Matplotlib Part 7 — Scatter Plots
Course: Dataraflow Week 8
Description: Demonstrates creating scatter plots using plt.scatter() with customized limits and grids.
"""

import matplotlib.pyplot as plt

# Define multi-platform dataset variables
y_views = [534, 690, 258, 402, 724, 689, 352]
f_views = [123, 342, 700, 305, 406, 648, 325]
t_views = [202, 209, 176, 415, 824, 389, 550]
days = [1, 2, 3, 4, 5, 6, 7]

# Create scatter plots instead of line plots
plt.scatter(days, y_views, label='Youtube views', marker='o')
plt.scatter(days, f_views, label='Facebook views', marker='o')
plt.scatter(days, t_views, label='Twitter views', marker='o')

# Add labels, title, and legend
plt.xlabel('Days')
plt.ylabel('Views')
plt.title('Social media views for a channel')
plt.legend()

# Set custom limits and gridlines
plt.xlim(1, 5)
plt.ylim(100, 900)
plt.grid(True, color='r', linestyle='--')

# Save the plot image to disk with 500 DPI
plt.savefig('img_3.png', dpi=500)

# Display the scatter plot window
plt.show()