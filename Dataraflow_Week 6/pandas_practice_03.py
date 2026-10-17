import pandas as pd

# Creating a sample DataFrame
data = pd.DataFrame({
    'Country': ['Angola', 'Brazil', 'China', 'India', 'Portugal', 'Russia', 'South Africa'],
    'Population (1000s)': [21472, 200362, 1393337, 1252140, 10608, 142834, 52776],
    'TB deaths': [6900, 4400, 41000, 240000, 140, 17000, 25000]
})

print("--- 1. Chaining methods on a column ---")
print("Third value of TB deaths:", data['TB deaths'].iloc[2])

print("\n--- 2. Single Condition Filtering (Population > 80,000 thousand) ---")
large_pop = data[data['Population (1000s)'] > 80000]
print(large_pop[['Country', 'Population (1000s)']])

print("\n--- 3. Multiple Conditions with Bitwise Operators (&) ---")
# Countries with population > 80M and TB deaths > 15,000
pop = data['Population (1000s)']
deaths = data['TB deaths']
filtered_df = data[(pop > 80000) & (deaths > 15000)]
print(filtered_df[['Country', 'Population (1000s)', 'TB deaths']])