"""
Practice Script: Grouping & Aggregating Data — Part 2 Walkthrough
Course: Dataraflow Week 8
Description: Implements lesson setup (warnings, matplotlib grid style), 
             database connection via run_query(), single grouping, 
             multi-column grouping, and subgroup extraction with get_group().
"""

import sys
import pathlib
import warnings
import pandas as pd
import matplotlib

# --- LESSON SETUP BLOCK ---
# Ignore future warnings as shown in the lesson material
warnings.simplefilter('ignore', FutureWarning)

# Set matplotlib to show gridlines by default (matching lesson configuration)
matplotlib.rcParams['axes.grid'] = True


# --- STEP 1: ESTABLISH DATABASE CONNECTION & LOAD DATA ---
# Dynamically locate project root and import run_query from the cohort database module
_p = pathlib.Path.cwd()
while _p != _p.parent and not (_p / "db" / "dataraflow_db.py").exists():
    _p = _p.parent
sys.path.insert(0, str(_p))
from db.dataraflow_db import run_query

# Query the monthly UK milk trade table from the week09 schema
milk = run_query("SELECT * FROM week09.comtrade_milk_uk_monthly_14")
print(f"--- Data Loaded Successfully from Database: {len(milk)} rows ---")


if not milk.empty:
    # Clean up column names to remove any accidental whitespace
    milk.columns = milk.columns.str.strip()

    # --- STEP 2: SEPARATE WORLD TOTALS FROM INDIVIDUAL COUNTRIES ---
    # Isolate global aggregate rows ('World') from individual country trade partner rows
    milk_world = milk[milk['Partner'] == 'World']
    milk_countries = milk[milk['Partner'] != 'World']
    print(f"Individual Country Partner Rows: {len(milk_countries)}")


    # --- STEP 3: SINGLE GROUPING BY TRADE FLOW ---
    # The groupby() method splits rows into separate groups based on unique values in 'Trade Flow'
    flow_groups = milk_countries.groupby('Trade Flow')
    
    print("\n--- Available Trade Flow Groups ---")
    print(list(flow_groups.groups.keys()))

    # Retrieve and inspect the first few rows of the 'Imports' group using get_group()
    print("\n--- Sample Rows for 'Imports' Group ---")
    print(flow_groups.get_group('Imports')[['Year', 'Period', 'Trade Flow', 'Partner', 'Trade Value (US$)']].head(3))


    # --- STEP 4: MULTI-COLUMN GROUPING (COMMODITY CODE & TRADE FLOW) ---
    # Create composite groups based on multiple key columns by passing a list
    GROUPING_COMMFLOW = ['Commodity Code', 'Trade Flow']
    comm_flow_groups = milk_countries.groupby(GROUPING_COMMFLOW)
    
    print("\n--- Multi-Column Group Keys (Commodity Code & Trade Flow) ---")
    print(list(comm_flow_groups.groups.keys()))


    # --- STEP 5: MULTI-LEVEL GROUPING AND TUPLE RETRIEVAL ---
    # Group by Partner and Trade Flow to analyze specific bilateral trade relationships
    GROUPING_PARTNERFLOW = ['Partner', 'Trade Flow']
    partner_flow_groups = milk_countries.groupby(GROUPING_PARTNERFLOW)

    # Retrieve a specific subgroup by passing a tuple matching the multi-level keys
    target_group_key = ('France', 'Imports')
    if target_group_key in partner_flow_groups.groups:
        france_imports_group = partner_flow_groups.get_group(target_group_key)
        print(f"\n--- Retrieved Group Slice for: {target_group_key} ---")
        print(france_imports_group[['Year', 'Period', 'Trade Flow', 'Partner', 'Commodity Code', 'Trade Value (US$)']].head(3))


    # --- STEP 6: GROUPING BY COMMODITY AND FINDING LEADING PARTNERS ---
    # Group by commodity code string to isolate specific product categories
    commodity_groups = milk_countries.groupby('commodityCode' if 'commodityCode' in milk_countries.columns else 'Commodity Code')
    
    available_commodities = list(commodity_groups.groups.keys())
    print(f"\n--- Available Commodity Keys ---")
    print(available_commodities)

    # Dynamically select an available commodity code to find its top trade partners
    if available_commodities:
        target_commodity = available_commodities[0]
        
        top_partners_comm = (
            commodity_groups.get_group(target_commodity)
            .sort_values(by='Trade Value (US$)', ascending=False)
            .head(5)
        )
        print(f"\n--- Top 5 Leading Trade Partners for Commodity Code {target_commodity} ---")
        print(top_partners_comm[['Period', 'Trade Flow', 'Partner', 'Trade Value (US$)', 'Commodity Code']].to_string(index=False))