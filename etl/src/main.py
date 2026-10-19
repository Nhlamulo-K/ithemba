"""ETL entry point: ingest -> transform -> load -> export insights.json"""
from src.ingest import load_crime_stats
from src.transform import split_categories
from src.load import load_dataframe, get_connection

def main():
    df = load_crime_stats()
    conn = get_connection()
    load =load_dataframe(df, conn)
    print("Done")
    return load


if __name__ == "__main__":
    main()
