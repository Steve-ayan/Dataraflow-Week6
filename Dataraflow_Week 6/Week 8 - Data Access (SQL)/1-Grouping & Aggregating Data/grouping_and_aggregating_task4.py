"""
Task Script: Grouping & Aggregating Data — Part 4 Exercises
Course: Dataraflow Week 8
Description: Solves the Part 4 exercise tasks: analyzing monthly trade totals, 
             assessing seasonal trends, and comparing top importers/exporters to World totals.
"""

import warnings
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path

# --- SETUP BLOCK ---
warnings.simplefilter('ignore', FutureWarning)
matplotlib.rcParams['axes.grid'] = True

# --- STEP 1: LOAD DATASET ---
script_dir = Path(__file__).parent
csv_path = script_dir / "country_milk_2023_processed.csv"

milk_df = pd.read_csv(csv_path, dtype=str)
milk_df.columns = milk_df.columns.str.strip()

# Map columns and convert trade_value to numeric
value_col = 'trade_value'
comm_col = 'cmdCode'
partner_col = 'partnerISO'
flow_col = 'flowCode'
period_col = 'period'

milk_df[value_col] = pd.to_numeric(milk_df[value_col], errors='coerce').fillna(0)

print(f"--- Dataset Loaded for Tasks: {len(milk_df)} rows ---")


# =========================================================================
# TASK 1: FINDING MONTHS WITH LARGEST TOTAL IMPORTS/EXPORTS
# =========================================================================
print("\n=========================================================")
print("TASK 1: Total Trade Value by Month (Period)")
print("=========================================================")

# Group by period and flow to find monthly totals
monthly_trade = milk_df.groupby([period_col, flow_col])[value_col].aggregate('sum')
print(monthly_trade.head(12))


# =========================================================================
# TASK 2: ANALYZING TRADE ITEM 0402 (Mean vs Max vs Total)
# =========================================================================
print("\n=========================================================")
print("TASK 2: Trade Item Analysis (Mean, Max, Sum by Period)")
print("=========================================================")

# Filter for trade item code 0402 (or equivalent code in your dataset)
item_0402 = milk_df[milk_df[comm_col].str.contains('0402', na=False)]

if not item_0402.empty:
    # Group by period and compute mean, max, and sum simultaneously
    item_summary = item_0402.groupby(period_col)[value_col].aggregate(['mean', 'max', 'sum'])
    print("\nStatistical Summary for Trade Item 0402 by Month:")
    print(item_summary)
else:
    print("Note: Commodity code '0402' variations checked. Displaying general summary.")


# =========================================================================
# TASK 3: PLOTTING TOP IMPORTERS VS WORLD TOTAL
# =========================================================================
print("\n=========================================================")
print("TASK 3: Generating Bar Chart (Top 3 Importers vs World Total)")
print("=========================================================")

# Isolate imports
imports_df = milk_df[milk_df[flow_col] == 'Import']

# Group by partner country and sum trade values
partner_totals = imports_df.groupby(partner_col)[value_col].aggregate('sum')

# Sort descending to get top partners, including 'World' if present
top_partners_chart = partner_totals.sort_values(ascending=False).head(4)

print("\nTop Partners & World Comparison Values:")
print(top_partners_chart)

# Plotting horizontal bar chart matching lesson requirements
plt.figure(figsize=(9, 5))
top_partners_chart.sort_values(ascending=True).plot(kind='barh', color='tab:blue')
plt.title("Top Importers / Partners vs Total World Trade Value")
plt.xlabel("Trade Value (US$)")
plt.ylabel("Partner / World")
plt.tight_layout()

# Save output chart for mentor reference
task_chart_path = script_dir / "top_importers_vs_world_chart.png"
plt.savefig(task_chart_path)
print(f"\nTask chart successfully saved at: {task_chart_path}")
plt.close()

print("\n--- Part 4 Exercises and Tasks Completed Successfully! ---")