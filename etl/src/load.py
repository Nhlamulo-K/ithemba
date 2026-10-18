import psycopg2
import os
from dotenv import load_dotenv
from src.ingest import load_crime_stats
from src.transform import split_categories

load_dotenv()

def get_connection():
    conn = psycopg2.connect(
        host=os.environ.get("POSTGRES_HOST"),
        port=int(os.environ.get("POSTGRES_PORT")),
        dbname=os.environ.get("POSTGRES_DB"),
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASSWORD"),
    )
    return conn

def load_dataframe(df, conn):
    details, total, detection = split_categories(df)
    cur = conn.cursor()

    for row in details.itertuples():
        cur.execute(
            """INSERT INTO crime_stats (province, year, crime_category, reported_count) 
            VALUES (%s, %s, %s, %s) 
            ON CONFLICT (province, year, crime_category) DO NOTHING""",
            (row.province, row.year, row.crime_category, row.reported_count)
        )
    
    for row in total.itertuples():
        cur.execute(
            """INSERT INTO crime_stats (province, year, crime_category, reported_count) 
            VALUES (%s, %s, %s, %s) 
            ON CONFLICT (province, year, crime_category) DO NOTHING""",
            (row.province, row.year, row.crime_category, row.reported_count)
        )
    
    for row in detection.itertuples():
        cur.execute(
            """INSERT INTO crime_stats (province, year, crime_category, reported_count) 
            VALUES (%s, %s, %s, %s) 
            ON CONFLICT (province, year, crime_category) DO NOTHING""",
            (row.province, row.year, row.crime_category, row.reported_count)
        )
    
    conn.commit()

if __name__ == "__main__":
    df = load_crime_stats()
    conn = get_connection()
    load_dataframe(df, conn)
    print("Done")
