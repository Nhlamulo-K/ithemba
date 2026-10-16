-- Create a new table 'TableName' with a primary key and columns
CREATE TABLE crime_stats (
    id SERIAL PRIMARY KEY,
    province TEXT NOT NULL,
    year INTEGER NOT NULL,
    crime_category TEXT NOT NULL,
    reported_count INTEGER NOT NULL,

    UNIQUE (province, year, crime_category)
);
