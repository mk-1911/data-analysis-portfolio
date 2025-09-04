import sqlite3
import pandas as pd
from pathlib import Path

# --- Config ---
DB_PATH = "cars.db"
SQL_DIR = Path("../sql")
RESULTS_DIR = Path("../../results")

RESULTS_DIR.mkdir(exist_ok=True)

# --- Connect to DB ---
conn = sqlite3.connect(DB_PATH)

# --- Iterate over all SQL files ---
for sql_file in sorted(SQL_DIR.glob("*.sql")):
    query_name = sql_file.stem   # e.g. q01_avg_mpg_by_make
    print(f"Running {query_name} ...")

    # read query
    with open(sql_file, "r") as f:
        query = f.read()

    try:
        df = pd.read_sql_query(query, conn)
        out_path = RESULTS_DIR / f"{query_name}.csv"
        df.to_csv(out_path, index=False)
        print(f"✅ Saved {out_path}")
    except Exception as e:
        print(f"❌ Error in {query_name}: {e}")

conn.close()