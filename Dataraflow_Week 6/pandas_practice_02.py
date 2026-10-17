import pandas as pd

# Creating a sample DataFrame to practice inspection attributes and methods
data = pd.DataFrame({
    'Country': ['Angola', 'Brazil', 'China', 'India', 'Portugal', 'Mozambique', 'South Africa'],
    'Population (1000s)': [21472, 200362, 1393337, 1252140, 10608, 25834, 52776],
    'TB deaths': [6900, 4400, 41000, 240000, 140, 18000, 25000]
})

print("--- 1. DataFrame Columns Attribute ---")
print(data.columns)

print("\n--- 2. Inspecting Rows with iloc[] ---")
print("First row (index 0):\n", data.iloc[0])

print("\n--- 3. Using head() and tail() ---")
print("First 3 rows:\n", data.head(3))
print("Last 2 rows:\n", data.tail(2))

print("\n--- 4. Series vs DataFrame Extraction ---")
print("Extracting as Series (single brackets):\n", type(data['Country']), "\n", data['Country'].head(2))
print("\nExtracting as DataFrame (double brackets):\n", type(data[['Country']]), "\n", data[['Country']].head(2))