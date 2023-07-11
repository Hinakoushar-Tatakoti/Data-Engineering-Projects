sql="""CREATE TABLE IF NOT EXISTS twitter_etl_table(
      id SERIAL PRIMARY KEY,
      datetime DATE NOT NULL,
      username VARCHAR(200) NOT NULL,
      text TEXT,
      source VARCHAR(200),
      location VARCHAR(200)
    );