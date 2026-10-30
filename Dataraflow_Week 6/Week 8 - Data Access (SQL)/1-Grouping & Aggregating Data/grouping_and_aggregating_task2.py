"""
Assignment: Grouping & Aggregating Data — Part 2
Course: Dataraflow Week 8
Description: Performs single and multi-level groupings on country_milk_2023_processed.csv 
             using correct commodity and trade flow keys.
"""

import warnings
import pandas as pd
from pathlib import Path

# --- SETUP BLOCK ---
warnings.simplefilter('ignore', FutureWarning)

# --- STEP 1: LOAD THE PROCESSED ASSIGNMENT DATASET ---
script_dir = Path(__file__).parent
csv_path = script_dir / "country_milk_2023_processed.csv"

try:
    milk_countries = pd.read_csv(csv_path, dtype=str)
    print(f"--- Assignment Data Loaded Successfully: {len(milk_countries)} rows ---")
except FileNotFoundError:
    print(f"[ERROR] Could not find file at: {csv_path}")
    milk_countries = pd.DataFrame()

if not milk_countries.empty:
    milk_countries.columns = milk_countries.columns.str.strip()

    # Map exact columns from your dataset schema
    value_col = 'trade_value'
    comm_col = 'cmdCode' if 'cmdCode' in milk_countries.columns else 'commodityCode'
    flow_col = 'flowCode'
    period_col = 'period'
    partner_col = 'partnerISO'

    # Convert trade values to numeric for proper sorting
    milk_countries[value_col] = pd.to_numeric(milk_countries[value_col], errors='coerce').fillna(0)


    # =========================================================================
    # TASK PART A: GROUP BY COMMODITY
    # =========================================================================
    print("\n=========================================================")
    print(f"TASK PART A: Grouping by Commodity ('{comm_col}')")
    print("=========================================================")

    commodity_groups = milk_countries.groupby(comm_col)
    available_commodities = list(commodity_groups.groups.keys())
    print(f"Available Commodity Groups: {len(available_commodities)} found")

    if available_commodities:
        target_comm = available_commodities[0]
        top_partner_comm = (
            commodity_groups.get_group(target_comm)
            .sort_values(by=value_col, ascending=False)
            .head(1)
        )
        print(f"\nMost Significant Trade Partner for Commodity Group:")
        cols_to_show = [c for c in [period_col, flow_col, partner_col, value_col] if c in milk_countries.columns]
        print(top_partner_comm[cols_to_show].to_string(index=False))


    # =========================================================================
    # TASK PART B: GROUP BY TRADE FLOW, COMMODITY, AND PERIOD
    # =========================================================================
    print("\n=========================================================")
    print("TASK PART B: Multi-Level Grouping (Trade Flow, Commodity, Period)")
    print("=========================================================")

    MULTI_GROUP_KEYS = [flow_col, comm_col, period_col]
    multi_groups = milk_countries.groupby(MULTI_GROUP_KEYS)
    all_keys = list(multi_groups.groups.keys())
    print(f"Total unique multi-level group combinations created: {len(all_keys)}")

    if all_keys:
        sample_key = all_keys[0]
        significant_subset = multi_groups.get_group(sample_key)
        
        top_partner_subset = (
            significant_subset
            .sort_values(by=value_col, ascending=False)
            .head(1)
        )
        print(f"\nMost Significant Trade Partner for Group Slice:")
        print(f"Key details -> Flow: {sample_key[0]} | Commodity: {sample_key[1][:30]}... | Period: {sample_key[2]}")
        cols_to_show = [c for c in [partner_col, value_col] if c in milk_countries.columns]
        print(top_partner_subset[cols_to_show].to_string(index=False))