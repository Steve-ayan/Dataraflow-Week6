"""
Assignment: Grouping & Aggregating Data — Part 1 (2023 Dataset)
Course: Dataraflow Week 8
Description: Loads UN Comtrade 2023 trade data, unifies monetary value columns (primary, cif, fob),
             aggregates annual trade totals by partner, and outputs top 10 lists.
"""

import pandas as pd
from pathlib import Path

# --- STEP 1: LOAD THE 2023 COMTRADE CSV DATA ---
script_dir = Path(__file__).parent
csv_filename = "comtrade_milk_uk_2023.csv"
csv_path = script_dir / csv_filename

try:
    milk_2023 = pd.read_csv(
        csv_path, 
        dtype=str,  
        encoding='ISO-8859-1'
    )
    print("--- Step 1: Data Loaded Successfully ---")
    print(f"Total rows loaded: {len(milk_2023)}")
except FileNotFoundError:
    print(f"[ERROR] Could not find '{csv_filename}' at path: {csv_path}")
    milk_2023 = pd.DataFrame()


if not milk_2023.empty:
    # Clean up hidden BOM characters from headers if present
    milk_2023.columns = milk_2023.columns.str.replace('ï»¿', '')

    # --- STEP 2: UNIFY MONETARY VALUE COLUMNS ---
    flow_col = 'flowCode'         # Contains 'Import' or 'Export'
    partner_col = 'partnerISO'    # Contains country names

    # Convert potential value columns to numeric
    for col in ['primaryValue', 'cifvalue', 'fobvalue']:
        if col in milk_2023.columns:
            milk_2023[col] = pd.to_numeric(milk_2023[col], errors='coerce').fillna(0)
        else:
            milk_2023[col] = 0.0

    # Create a unified trade value by taking the maximum or sum across available value fields
    milk_2023['trade_value'] = milk_2023[['primaryValue', 'cifvalue', 'fobvalue']].max(axis=1)


    # --- STEP 3: SEPARATE WORLD SUMMARY FROM INDIVIDUAL COUNTRIES ---
    is_world = milk_2023['partnerDesc'].isin(['World', 'W00']) | milk_2023['partnerISO'].isin(['World', 'W00'])
    milk_countries = milk_2023[~is_world]

    print(f"\n--- Step 3: Row Breakdown ---")
    print(f"Individual Country Partner Rows: {len(milk_countries)}")


    # --- STEP 4: FILTER BY TRADE FLOW (IMPORTS & EXPORTS) ---
    milk_countries_imports = milk_countries[milk_countries[flow_col].str.contains('Import', case=False, na=False)]
    milk_countries_exports = milk_countries[milk_countries[flow_col].str.contains('Export', case=False, na=False)]


    # --- STEP 5: GROUP & AGGREGATE ANNUAL IMPORTS BY PARTNER ---
    import_agg = milk_countries_imports.groupby(partner_col, as_index=False)['trade_value'].sum()
    top_import_partners = import_agg.sort_values(by='trade_value', ascending=False).head(10)

    print("\n--- Step 5: Top 10 Overall Import Partners (2023 Annual Total) ---")
    print(top_import_partners.to_string(index=False))


    # --- STEP 6: GROUP & AGGREGATE ANNUAL EXPORTS BY PARTNER ---
    export_agg = milk_countries_exports.groupby(partner_col, as_index=False)['trade_value'].sum()
    top_export_partners = export_agg.sort_values(by='trade_value', ascending=False).head(10)

    print("\n--- Step 6: Top 10 Overall Export Partners (2023 Annual Total) ---")
    print(top_export_partners.to_string(index=False))


    # --- STEP 7: EXPORT PROCESSED DATA ---
    output_filename = script_dir / "country_milk_2023_processed.csv"
    milk_countries.to_csv(output_filename, index=False)
    print(f"\n[INFO] Successfully saved processed data to '{output_filename.name}'")