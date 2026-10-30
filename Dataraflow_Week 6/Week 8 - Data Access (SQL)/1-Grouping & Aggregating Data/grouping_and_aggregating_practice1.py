import sys
from pathlib import Path

# --- STEP 1: DYNAMIC PATH SETUP ---
# Dynamically locate the root workspace directory by walking up parent folders
# until we find the 'db/dataraflow_db.py' utility module.
_p = Path.cwd()
while _p != _p.parent and not (_p / "db" / "dataraflow_db.py").exists():
    _p = _p.parent
sys.path.insert(0, str(_p))

# Import the database query runner function from course utilities
from db.dataraflow_db import run_query


# --- STEP 2: DATA CONNECTION & INSPECTION ---
# Query the monthly UK milk trade table from the week09 schema to verify the connection
milk = run_query("SELECT * FROM week09.comtrade_milk_uk_monthly_14")

# Display the first 3 rows to confirm columns and data types
print("--- First 3 Rows of Raw Milk Data ---")
print(milk.head(3))


# --- STEP 3: SQL AGGREGATION USING GROUP BY ---
# Aggregate total trade value grouped by Trade Flow and Commodity Code.
# Note: Column names with spaces/symbols are bracket-quoted in SQL ([Trade Value (US$)]).
summary = run_query("""
    SELECT [Trade Flow], [Commodity Code], SUM([Trade Value (US$)]) AS total_value
    FROM week09.comtrade_milk_uk_monthly_14
    GROUP BY [Trade Flow], [Commodity Code]
    ORDER BY total_value DESC
""")

print("\n--- Summary Aggregation by Trade Flow and Commodity ---")
print(summary.head())


# --- STEP 4: FILTERED SQL AGGREGATION (MONTHLY EXPORTS) ---
# Filter specifically for 'Exports' and calculate total trade value by Period (monthly)
monthly = run_query("""
    SELECT [Period], SUM([Trade Value (US$)]) AS exports
    FROM week09.comtrade_milk_uk_monthly_14
    WHERE [Trade Flow] = 'Exports'
    GROUP BY [Period]
    ORDER BY [Period]
""")

print("\n--- Monthly Export Totals ---")
print(monthly.head())


# --- STEP 5: PANDAS PIVOT TABLE ALTERNATIVE ---
# Alternatively, pull raw data and perform aggregation using pandas pivot_table
pivot = milk.pivot_table(
    index="Period",
    columns="Trade Flow",
    values="Trade Value (US$)",
    aggfunc="sum",
)

print("\n--- Pandas Pivot Table Summary ---")
print(pivot.head())


# --- STEP 6: EXPORT RESULTS FOR ASSIGNMENT DELIVERABLES ---
# Save the summary DataFrame to a CSV file for the take-home submission
summary.to_csv("milk_trade_summary.csv", index=False)
print("\n[INFO] Successfully saved summary to milk_trade_summary.csv")