"""
Practice Script: Matplotlib Part 3 — Multiple Datasets on a Single Plot
Course: Dataraflow Week 8
Description: Plots multiple lines (YouTube, Facebook, Twitter) on the same chart with markers.
"""

import matplotlib.pyplot as plt

# Define multi-platform dataset variables
y_views = [534, 690, 258, 402, 724, 689, 352]
f_views = [123, 342, 700, 305, 406, 648, 325]
t_views = [202, 209, 176, 415, 824, 389, 550]
days = [1, 2, 3, 4, 5, 6, 7]

# Plot multiple datasets on a single set of axes
plt.plot(days, y_views, label='Youtube views', marker='o')
plt.plot(days, f_views, label='Facebook views', marker='o')
plt.plot(days, t_views, label='Twitter views', marker='o')

# Add labels, title, and legend
plt.xlabel('Days')
plt.ylabel('Views')
plt.title('Social media views for a channel')
plt.legend()

# Display the multi-line chart window
plt.show()