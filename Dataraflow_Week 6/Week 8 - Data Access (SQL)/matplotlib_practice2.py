"""
Practice Script: Matplotlib Part 2 — Styling Lines & Markers
Course: Dataraflow Week 8
Description: Customizes line plots with colors, markers, line styles, and widths.
"""

import matplotlib.pyplot as plt

# Define sample data
x = [1, 2, 3, 4, 5, 6, 7]                  # Week days
y = [964, 287, 42, 390, 64, 800, 523]       # Views

# Create styled line plot
plt.plot(x, y, label='Youtube views',
         color='r',             # Red line
         marker='o',            # Circle markers on data points
         markerfacecolor='g',   # Green fill inside the markers
         linestyle='--',        # Dashed line style
         linewidth=3)           # Line thickness of 3

# Add labels, title, and legend
plt.xlabel('Week days')
plt.ylabel('Views')
plt.title('Youtube views on daily basis')
plt.legend(loc='upper left')

# Display the styled chart window
plt.show()