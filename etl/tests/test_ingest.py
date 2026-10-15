from src.ingest import load_crime_stats

def test_load_crime_stats():
    df = load_crime_stats()
    assert df.shape == (324, 4)
    assert list(df.columns) == ["province", "year", "crime_category", "reported_count"]
