"""
Practice Script: Matplotlib Part 8 — Bar Charts
Course: Dataraflow Week 8
Description: Demonstrates creating bar charts using plt.bar() with multiple datasets.
"""

import matplotlib.pyplot as plt

# Define dataset variables for bar charts
y_views = [200, 50, 250, 300, 100, 150, 350]
fb_views = [160, 200, 40, 240, 80, 120, 280]
days = [1, 2, 3, 4, 5, 6, 7]

# Create bar charts for YouTube and Facebook views
plt.bar(days, y_views, label='Youtube views')
plt.bar(days, fb_views, label='Facebook views')

# Add labels, title, and legend
plt.xlabel('Days')
plt.ylabel('Views')
plt.title('Social media views for a channel')
plt.legend()

# Save the plot image to disk with 500 DPI
plt.savefig('bar_2.png', dpi=500)

# Display the bar chart window
plt.show()