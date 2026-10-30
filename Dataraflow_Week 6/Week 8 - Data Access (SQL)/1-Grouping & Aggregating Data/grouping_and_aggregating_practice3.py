"""
Practice Script: Grouping & Aggregating Data — Part 3 Walkthrough
Course: Dataraflow Week 8
Description: Implements the exact lesson walkthrough: setup configuration, 
             creating the sample DataFrame, single-column grouping, 
             multi-column grouping, and group retrieval using pandas.
"""

import warnings
import pandas as pd
import matplotlib

# --- STEP 1: LESSON SETUP ---
# Ignore future warnings as demonstrated in the lesson material[cite: 8]
warnings.simplefilter('ignore', FutureWarning)

# Configure matplotlib to display gridlines by default[cite: 8]
matplotlib.rcParams['axes.grid'] = True
print("--- Step 1: Lesson setup and configurations applied successfully ---")


# --- STEP 2: CREATING THE SAMPLE DATAFRAME ---
# Constructing the sample dataset matching the lesson diagram and walkthrough
data = [
    ['A', 10, 2014], ['A', 15, 2014], ['A', 5, 2015], ['A', 20, 2015],
    ['B', 10, 2014], ['B', 10, 2015], ['B', 5, 2014],
    ['C', 20, 2015], ['C', 30, 2015]
]

df = pd.DataFrame(data, columns=["Commodity", "Amount", "Year"])

print("\n--- Step 2: Full Sample DataFrame Created ---")
print(df)


# --- STEP 3: SINGLE-COLUMN GROUPING & ACCESS ---
# Group the DataFrame rows based on unique values in the single 'Commodity' key column[cite: 10]
grouped_commodity = df.groupby('Commodity')

# Inspect the unique group keys identified in the dataset[cite: 10]
print("\n--- Step 3: Available Single Group Keys ---")
print(grouped_commodity.groups.keys())

# Retrieve and inspect all rows associated specifically with group 'B' using get_group()[cite: 10]
print("\n--- Step 3: Retrieved Rows for Commodity Group 'B' ---")
print(grouped_commodity.get_group('B'))


# --- STEP 4: MULTI-COLUMN GROUPING & TUPLE RETRIEVAL ---
# Group the DataFrame against multiple key columns ('Commodity' and 'Year')[cite: 11]
grouped_multi = df.groupby(['Commodity', 'Year'])

# Inspect the resulting multi-level tuple keys[cite: 11]
print("\n--- Step 4: Multi-Column Group Keys ---")
print(grouped_multi.groups.keys())

# Retrieve rows corresponding to a specific multi-level tuple key (Commodity 'A' in Year 2014)[cite: 11]
print("\n--- Step 4: Retrieved Rows for Multi-Level Group ('A', 2014) ---")
print(grouped_multi.get_group(('A', 2014)))