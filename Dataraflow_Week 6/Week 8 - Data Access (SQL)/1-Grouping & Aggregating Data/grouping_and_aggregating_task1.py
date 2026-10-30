import sys
from pathlib import Path
import pandas as pd

# --- STEP 1: DYNAMIC PATH SETUP ---
# Locate the root workspace directory by walking up parent folders
# until we find the 'db/dataraflow_db.py' utility module.
_p = Path.cwd()
while _p != _p.parent and not (_p / "db" / "dataraflow_db.py").exists():
    _p = _p.parent
sys.path.insert(0, str(_p))

# Import the database query runner function from course utilities
from db.dataraflow_db import run_query


# --- STEP 2: LOAD DATA FROM COHORT DATABASE ---
# Load the monthly UK Comtrade milk trade data from the week09 schema.
# Commodity/Reporter codes are stored as text to preserve leading zeros.
milk = run_query("SELECT * FROM week09.comtrade_milk_uk_monthly_14")

print("--- Step 2: Raw Data Sample ---")
print(milk.head(3))


# --- STEP 3: LIMIT COLUMNS TO A USABLE SUBSET ---
# Select a subset of relevant columns to make the DataFrame easier to work with
COLUMNS = [
    'Year', 
    'Period', 
    'Trade Flow', 
    'Reporter', 
    'Partner', 
    'Commodity', 
    'Commodity Code', 
    'Trade Value (US$)'
]
milk = milk[COLUMNS]

print("\n--- Step 3: Filtered Columns Sample ---")
print(milk.head(3))


# --- STEP 4: DERIVE SUBSETS FOR WORLD VS. INDIVIDUAL COUNTRIES ---
# Separate out rows where the partner is 'World' versus individual partner countries
milk_world = milk[milk['Partner'] == 'World']
milk_countries = milk[milk['Partner'] != 'World']

print(f"\n--- Step 4: Row Counts ---")
print(f"World Partner Rows: {len(milk_world)}")
print(f"Individual Country Partner Rows: {len(milk_countries)}")


# --- STEP 5: SUBSETTING DATA BY TRADE FLOW (IMPORTS) ---
# Filter specifically for 'Imports' across the dataset and country subsets
milk_imports = milk[milk['Trade Flow'] == 'Imports']
milk_countries_imports = milk_countries[milk_countries['Trade Flow'] == 'Imports']
milk_world_imports = milk_world[milk_world['Trade Flow'] == 'Imports']


# --- STEP 6: SORTING AND ANALYZING TOP IMPORT PARTNERS ---
# Find the most valuable import partners during January 2014 (Period '201401')
# by sorting the data in descending order of Trade Value.
period_to_check = 201401
milk_imports_in_jan = milk_countries_imports[
    milk_countries_imports['Period'] == period_to_check
]

# Sort by Trade Value in descending order and select the top 10 partners
top_import_partners = milk_imports_in_jan.sort_values(
    by='Trade Value (US$)', 
    ascending=False
).head(10)

print(f"\n--- Step 6: Top 10 Import Partners for Period {period_to_check} ---")
print(top_import_partners[['Period', 'Trade Flow', 'Partner', 'Commodity', 'Commodity Code', 'Trade Value (US$)']])


# --- STEP 7: EXPORTING DATA AS CSV (OPTIONAL LOCAL BACKUP) ---
# Store a local copy of the country-level milk trade dataset as a CSV file
milk_countries.to_csv("countrymilk.csv", index=False)
print("\n[INFO] Successfully saved country-level data to countrymilk.csv")