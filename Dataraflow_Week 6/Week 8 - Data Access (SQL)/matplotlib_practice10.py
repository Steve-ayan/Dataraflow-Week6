"""
Practice Script: Matplotlib Part 10 — Pie Charts
Course: Dataraflow Week 8
Description: Demonstrates creating pie charts using plt.pie() with labels, autopct, explode, and shadow.
"""

import matplotlib.pyplot as plt

# Define platform labels, view counts, and explosion offsets
labels_1 = ['Facebook', 'Instagram', 'Youtube', 'linked-in']
views = [300, 350, 400, 450]
explode_1 = [0, 0, 0, 0.2]  # Pop out the last slice (linked-in) by 20%

# Create the pie chart
plt.pie(
    views,
    labels=labels_1,
    autopct='%1.1f%%',
    explode=explode_1,
    shadow=True
)

# Save the plot image to disk with 500 DPI
plt.savefig('pie.png', dpi=500)

# Display the pie chart window
plt.show()