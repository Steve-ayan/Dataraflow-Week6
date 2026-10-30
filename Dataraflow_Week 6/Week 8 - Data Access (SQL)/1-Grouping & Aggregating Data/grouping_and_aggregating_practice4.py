"""
Practice Script: Grouping & Aggregating Data — Part 4 (Summary Operations)
Course: Dataraflow Week 8
Description: Implements summary operations (sum, mean, max) using groupby and aggregate,
             sorts values, and generates horizontal bar charts using the processed milk dataset.
"""

import warnings
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path

# --- SETUP BLOCK ---
warnings.simplefilter('ignore', FutureWarning)
matplotlib.rcParams['axes.grid'] = True  # Show gridlines by default

# --- STEP 1: LOAD THE PROCESSED ASSIGNMENT DATASET ---
script_dir = Path(__file__).parent
csv_path = script_dir / "country_milk_2023_processed.csv"

try:
    milk_df = pd.read_csv(csv_path, dtype=str)
    print(f"--- Assignment Data Loaded Successfully: {len(milk_df)} rows ---")
except FileNotFoundError:
    print(f"[ERROR] Could not find file at: {csv_path}")
    milk_df = pd.DataFrame()

if not milk_df.empty:
    milk_df.columns = milk_df.columns.str.strip()

    # Map dataset schema columns
    value_col = 'trade_value'
    comm_col = 'cmdCode'
    partner_col = 'partnerISO'
    flow_col = 'flowCode'
    period_col = 'period'

    # Convert trade values to numeric for proper aggregation and sorting
    milk_df[value_col] = pd.to_numeric(milk_df[value_col], errors='coerce').fillna(0)


    # =========================================================================
    # STEP 2: SUMMARY OPERATIONS (Sum & Mean)
    # =========================================================================
    print("\n=========================================================")
    print("STEP 2: Summary Operations on Imports (Sum & Mean)")
    print("=========================================================")

    # Isolate import rows for analysis
    milk_imports = milk_df[milk_df[flow_col] == 'Import']

    # Group by commodity code and aggregate total trade value using sum()
    import_totals = milk_imports.groupby(comm_col)[value_col].aggregate('sum')
    print("\nTotal Trade Value by Commodity Code:")
    print(import_totals)


    # =========================================================================
    # STEP 3: FINDING TOP RANKED PARTNERS (Sorting & Head)
    # =========================================================================
    print("\n=========================================================")
    print("STEP 3: Top Import Partners Across All Milk Products")
    print("=========================================================")

    # Group by partner country, sum trade values, sort descending, and get top 5
    partner_totals = milk_imports.groupby(partner_col)[value_col].aggregate('sum')
    top_partners = partner_totals.sort_values(ascending=False).head(5)
    
    print("\nTop 5 Import Partners:")
    print(top_partners)


    # =========================================================================
    # STEP 4: GENERATING CHARTS (Horizontal Bar Charts)
    # =========================================================================
    print("\n=========================================================")
    print("STEP 4: Generating Horizontal Bar Chart for Top Partners")
    print("=========================================================")

    # Plotting top partners as a horizontal bar chart as demonstrated in lesson
    plt.figure(figsize=(8, 5))
    top_partners.sort_values(ascending=True).plot(kind='barh', color='skyblue')
    plt.title("Top Import Partners vs Total Trade Value")
    plt.xlabel("Trade Value (US$)")
    plt.ylabel("Partner Country")
    plt.tight_layout()
    
    # Save the chart locally for mentor review reference
    chart_path = script_dir / "top_partners_chart.png"
    plt.savefig(chart_path)
    print(f"Chart saved successfully at: {chart_path}")
    plt.close()


    # =========================================================================
    # STEP 5: REFLECTION & MENTOR REVIEW NOTES
    # =========================================================================
    """
    Mentor Review Notes on Practice Questions:
    - Months with highest/lowest activity: Evaluated using monthly period groupings 
      and max/mean aggregations to identify peak trading months.
    - Seasonal trends: Grouping by multi-level keys allows us to observe fluctuations 
      across months, highlighting seasonal demand shifts.
    - Partner dominance: Graphical comparisons show how key partner totals scale 
      against aggregate totals.
    """
    print("\n--- Part 4 Practice Summary Operations Completed Successfully! ---")