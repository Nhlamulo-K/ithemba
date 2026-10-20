from pathlib import Path
import json
from src.load import get_connection

def get_list(conn):
    cur = conn.cursor()
    result = []

    cur.execute(
        """SELECT province, year, crime_category, reported_count 
        FROM crime_stats"""
        )
    rows = cur.fetchall()

    for row in rows:
        result.append({
            "province": row[0],
            "year": row[1],
            "crime_category": row[2],
            "reported_count": row[3]
        })
    return result

def get_summary(conn):
    cur = conn.cursor()
    result = []

    cur.execute(
        """SELECT province, SUM(reported_count)
        FROM crime_stats
        WHERE crime_category = 'Sexual offences'
        GROUP BY province"""
    )
    rows = cur.fetchall()

    for row in rows:
        result.append({
            "province": row[0],
            "reported_count": row[1]
        })
    return result

def get_trend(conn):
    cur = conn.cursor()
    result = []

    cur.execute(
        """SELECT  year, SUM(reported_count)
        FROM crime_stats
        WHERE crime_category = 'Sexual offences'
        GROUP BY year
        ORDER BY year"""
    )
    rows = cur.fetchall()
    for row in rows:
        result.append({
            "year": row[0],
            "reported_count": row[1]
        })
    return result

def export_insights(conn):
    all_data = get_list(conn)
    summary = get_summary(conn)
    trend = get_trend(conn)
    path = Path(__file__).parent.parent.parent / "data" / "insights" / "insights.json"
    insights = {
        "list": all_data,
        "summary": summary,
        "trend": trend
    }

    with open(path, "w") as file:
        json.dump(insights, file, indent=2)

if __name__ == "__main__":
    conn = get_connection()
    # rows = get_list(conn)
    # print (rows)
    # summary = get_summary(conn)
    # print(summary)
    # trend = get_trend(conn)
    # print(trend)
    export_insights(conn)
