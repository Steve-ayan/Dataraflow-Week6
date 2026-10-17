import pandas as pd

# 1. Define the DataFrame FIRST so it exists for all tasks
data = pd.DataFrame({
    'Country': ['Angola', 'Brazil', 'China', 'India', 'Portugal'],
    'Population (1000s)': [21472, 200362, 1393337, 1252140, 10608],
    'TB deaths': [6900, 4400, 41000, 240000, 140]
})

print("--- Original DataFrame ---")
print(data)

print("\n--- Task 1 & 2: Population Column Methods ---")
# Task 1: Select the population column
populationColumn = data['Population (1000s)']

# Task 2: Practise column methods
print("Total Population:", populationColumn.sum())
print("Smallest Population:", populationColumn.min())
print("Largest Population:", populationColumn.max())
print("Average (Mean) Population:", populationColumn.mean())
print("Median Population:", populationColumn.median())

print("\n--- Task 3: Sorting by Population ---")
print(data.sort_values('Population (1000s)'))

print("\n--- Vectorised Operations: Creating a New Column ---")
deathsColumn = data['TB deaths']
rateColumn = (deathsColumn * 100) / populationColumn
data['TB deaths (per 100,000)'] = rateColumn
print(data)