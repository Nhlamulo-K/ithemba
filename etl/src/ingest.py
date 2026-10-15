import pandas as pd

def load_crime_stats():
    df = pd.read_csv("../../data/insights/gbv_crime_stats_by_province_year.csv")
    return df

if __name__ == "__main__":
    df = load_crime_stats()
    print(df.head())
    print(df.shape)