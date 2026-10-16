from src.ingest import load_crime_stats
from src.transform import split_categories

def test_split_categories():
    df = load_crime_stats()
    details, total, detection = split_categories(df)
    assert details.shape == (216, 4)
    assert total.shape == (54, 4)
    assert detection.shape == (54, 4)