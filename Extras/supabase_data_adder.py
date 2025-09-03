import pandas as pd
from supabase import create_client, Client

# === CONFIG ===
SUPABASE_URL = "https://nznkmywjszxssasreots.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im56bmtteXdqc3p4c3Nhc3Jlb3RzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTIzMDUxNTAsImV4cCI6MjA2Nzg4MTE1MH0.lImhAMvEIAc6kkIzLRwmDRkUgwH6qhj3YS9qqIHndro"
EXCEL_FILE = "C:/Users/Arin Dhimar/Documents/FergussonCollege/Extras/stud-data.xlsx"
TARGET_TABLE = "students_duplicate"

# === Supabase Connection ===
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# === Load All Sheets ===
all_sheets = pd.read_excel(EXCEL_FILE, sheet_name=None)

for sheet_name, sheet_df in all_sheets.items():
    print(f"\nProcessing sheet: {sheet_name}")
    df = pd.DataFrame(sheet_df)

    # Rename Excel columns to match DB
    if 'Name' in df.columns:
        df.rename(columns={'Name': 'full_name'}, inplace=True)
    if 'Stream' in df.columns:
        df.rename(columns={'Stream': 'branch'}, inplace=True)

    # Ensure needed columns exist
    if 'full_name' not in df.columns or 'branch' not in df.columns:
        print(f"  Skipping '{sheet_name}' — missing 'full_name' or 'branch'.")
        continue

    # Filter for CS students (case-insensitive)
    df_cs = df[df['branch'].str.strip().str.upper() == 'IMCA']
    if df_cs.empty:
        print(f"  No CS students found in '{sheet_name}'.")
        continue

    # Prepare data
    df_cs = df_cs[['full_name']].dropna()
    df_cs['graduation_year'] = 2026
    df_cs['course_id'] = 3

    records = df_cs.to_dict(orient="records")

    try:
        res = supabase.table(TARGET_TABLE).insert(records).execute()

        # If res is a dict-like response
        error = None
        data = None

        if isinstance(res, dict):
            error = res.get("error")
            data = res.get("data")
        else:
            # Fallback if it's an object with attributes
            error = getattr(res, "error", None)
            data = getattr(res, "data", None)

        if error:
            print(f"  Failed to insert records from '{sheet_name}': {error}")
        else:
            count = len(data) if data else len(records)
            print(f"  Successfully inserted {count} records from '{sheet_name}'.")
    except Exception as e:
        print(f"  Exception inserting records from '{sheet_name}': {e}")
