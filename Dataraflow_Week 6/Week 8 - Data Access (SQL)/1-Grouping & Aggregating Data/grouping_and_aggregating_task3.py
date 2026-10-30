"""
Assignment Task: Grouping & Aggregating Data — Part 3
Course: Dataraflow Week 8
Description: Applies single and multi-column grouping on the processed milk dataset 
             (country_milk_2023_processed.csv) to answer the lesson task questions 
             regarding trade partners, commodities, and split-apply-combine logic.
"""

import warnings
import pandas as pd
from pathlib import Path

# --- SETUP BLOCK ---
warnings.simplefilter('ignore', FutureWarning)

# --- STEP 1: LOAD THE PROCESSED DATASET ---
script_dir = Path(__file__).parent
csv_path = script_dir / "country_milk_2023_processed.csv"

try:
    milk_df = pd.read_csv(csv_path, dtype=str)
    print(f"--- Dataset Loaded Successfully: {len(milk_df)} rows ---")
except FileNotFoundError:
    print(f"[ERROR] Could not find file at: {csv_path}")
    milk_df = pd.DataFrame()

if not milk_df.empty:
    milk_df.columns = milk_df.columns.str.strip()

    # Map necessary columns based on your dataset schema
    value_col = 'trade_value'
    comm_col = 'cmdCode'
    partner_col = 'partnerISO'
    flow_col = 'flowCode'
    period_col = 'period'

    # Convert trade values to numeric for proper sorting and aggregation
    milk_df[value_col] = pd.to_numeric(milk_df[value_col], errors='coerce').fillna(0)


    # =========================================================================
    # TASK REFLECTION 1: SINGLE-COLUMN GROUPING (By Commodity Code)
    # =========================================================================
    print("\n=========================================================")
    print("TASK REFLECTION 1: Grouping by Commodity Code")
    print("=========================================================")
    
    comm_grouped = milk_df.groupby(comm_col)
    print(f"Available Commodity Groups: {list(comm_grouped.groups.keys())}")
    
    # Find the top partner for the commodity
    for comm in comm_grouped.groups.keys():
        subset = comm_grouped.get_group(comm)
        top_partner = subset.sort_values(by=value_col, ascending=False).iloc[0]
        print(f"-> Commodity '{comm}': Major Partner is '{top_partner[partner_col]}' with trade value {top_partner[value_col]}")


    # =========================================================================
    # TASK REFLECTION 2: MULTI-COLUMN GROUPING (Flow, Commodity, Period)
    # =========================================================================
    print("\n=========================================================")
    print("TASK REFLECTION 2: Multi-Column Grouping (Flow, Commodity, Period)")
    print("=========================================================")
    
    multi_grouped = milk_df.groupby([flow_col, comm_col, period_col])
    print(f"Total unique multi-level group combinations: {len(multi_grouped.groups.keys())}")
    
    # Inspect top partners across these multi-level subgroups
    for key in list(multi_grouped.groups.keys())[:3]:  # Show first few groups
        sub_df = multi_grouped.get_group(key)
        top_sub_partner = sub_df.sort_values(by=value_col, ascending=False).iloc[0]
        print(f"-> Group Key {key}: Top Partner = '{top_sub_partner[partner_col]}' (Value: {top_sub_partner[value_col]})")


    # =========================================================================
    # TASK REFLECTION & MENTOR NOTES
    # =========================================================================
    """
    Mentor Review Answers for Lesson Task Prompts:
    
    1. How did you group the data and what questions did you ask of it?
       - Grouped the dataset using both single-column grouping (by commodity code) and 
         multi-column grouping (by trade flow, commodity code, and period).
       - Asked: What are the distinct trade categories, and how do trade volumes break down 
         across specific temporal and directional trade channels?
         
    2. Which countries were the major partners of your reporter country for the different groupings?
       - For commodity-level exports/imports, 'Areas, nes' and key bilateral partners 
         recorded the largest transaction volumes in the processed dataset.
         
    3. What other sorts of questions would you like to be able to ask?
       - With easy grouping, we can extend this to calculate month-on-month growth rates, 
         annual running totals, and comparative trade deficits/surpluses across partner countries.
    """
    print("\n--- Task Reflection Analysis Complete ---")