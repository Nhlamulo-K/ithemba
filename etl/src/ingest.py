import pandas as pd
from pathlib import Path

def load_crime_stats():
    path = Path(__file__).parent.parent.parent / "data" / "insights" / "gbv_crime_stats_by_province_year.csv"
    df = pd.read_csv(path)
    return df

if __name__ == "__main__":
    df = load_crime_stats()
    print(df.head())
    print(df.shape)