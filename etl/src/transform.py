import pandas as pd
from src.ingest import load_crime_stats

def split_categories(df):
    categories = ["Rape", "Sexual assault", "Attempted sexual offences", "Contact sexual offences"]
    mask = df["crime_category"].isin(categories)
    details = df[mask]

    category = ["Sexual offences"]
    masks = df["crime_category"].isin(category)
    total = df[masks]

    another = ["Sexual offences detected as a result of police action"]
    maskss = df["crime_category"].isin(another)
    detection = df[maskss]

    return details, total, detection

if __name__ == "__main__":
    df = load_crime_stats()
    print(split_categories(df))
