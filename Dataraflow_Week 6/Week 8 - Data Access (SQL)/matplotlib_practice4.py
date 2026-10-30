"""
Practice Script: Matplotlib Part 4 — Setting X and Y Axis Limits
Course: Dataraflow Week 8
Description: Demonstrates zooming in on a chart using plt.xlim() and plt.ylim().
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

# Set custom limits for X and Y axes (zooming in)
plt.xlim(1, 5)          # Show days 1 through 5 only
plt.ylim(100, 900)      # Show view counts from 100 to 900 only

# Display the customized chart window
plt.show()