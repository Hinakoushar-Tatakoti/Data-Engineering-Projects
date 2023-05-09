### PlugSurfing Coding Challenge ##

To run the code navigate to plugSurfing-coding-challenge/src/ folder on a terminal then run the below command
```bash
python extract_pipe.py 
```

To run the test cases navigate to plugSurfing-coding-challenge/test/ folder on a terminal then run below command 
```bash
pytest test_extract_pipe.py
```

As I'm already using AWS CLI (AWS credentials already being setup in the machine), so it directly authenticated and wrote data into specified s3 bucket.
The charger_models_UK.csv file is available under the folder listings-dp/ , the link will expire after 12 hours
```bash 
https://listings-dp.s3.eu-west-1.amazonaws.com/charger_models_UK.csv?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaDGV1LWNlbnRyYWwtMSJIMEYCIQDxjX5jGdVMa35v6fZ7MtiFrPR5Z2ZOhCIcpJ4HrtUfLgIhAPNGd9QNz8ePh9W6%2FXelZaIqiMmo%2B8NB1UazjB9rUr67KvUCCHEQAhoMNTYwMTU0NzAzODY4IgxAEwgy2lTuhyxQfqYq0gLk0%2BpGVU4uxMobu%2FNT5WTwIfvGkLRZnbN4rxOzZr66kt%2Fl50mopiWgFIjkMsXGH7IJECiFGgLcD81PlopHG1m7%2FtEd6ic%2FXrmu89n%2B0grvSlsPm2PpTaplDof0%2Fm65x3O%2B1zbc%2BHzFDNPR7DjYH9%2BQnjrIgLUAEUzdtfITh056TPkh78STQXZNmOHRBCR6y0I6%2FrwkIiPbZFGrfb%2BX7DHtkzbr1EcZLbM3LB8bKMCU%2FGWKznWqEnrQUijRwqCH7NCRi5Z8gqwrKk%2BfbsZL63SvS1b0cVftcgFg3npQD%2FMzcykJoUp66cEFEKm2xhvSfyRLwLbBKNpJEiTzs0xz3M9AVXkcFa4I2vTljALbBTwg8OvfnI%2Bkij10UrYCJz9IqqXXzc0n0ESOufz9U7H6HDXYEqtTjKVRFbbckQ5kqYFFAlV0rI0tF%2Bwzual%2F3kVJlrCfCzC58ueiBjqGAlVWibMDPVrvTlo8G30dPaAOcCI2LQ5Lk0CBxB5rGcyU4Kg8p9wZsbxretDSlfS4Ji04sUg8UHLzwBg17g2o2PBC9sSXPn%2B8D6AG%2FlzHZfHUPnyCZMXqCnQ9EhP9iQa3QL%2FQGel3xLSlFb7033uwtDy4QtAETnWqZiBjMvX2WqztKJRl9p662fQLNyPYjXNFm5UA41LAhcYc3TLFkMtiU1beUXj51dxyLusaJkmvGCxZDXqmUHLVyh9py399UT4vebxJHSKHRinu2o03faiz5aCOKBLAv%2Fqqi5YnwNubvwDamdJpiGDJah9NaKTliGG8W%2F4Krl8jEp%2FCTUGKxhRE9M2d6Wr1uHY%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20230509T114001Z&X-Amz-SignedHeaders=host&X-Amz-Expires=43200&X-Amz-Credential=ASIAYE26SO76B3EPDSXU%2F20230509%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Signature=de755b5152e122fbf23495c0ce0a8b9bbb1c8299d83ed2d317960adc110a08a6

```

Proposal for using the file in AWS with an RDMS:

Assuming that the data will be updated regularly, we can create an ETL (Extract, Transform, Load) pipeline using any orchestration tool such as Airflow that periodically retrieves the data from the source(json data), processes it using the same Python program, and loads it into the AWS S3 (CSV file) then this can be loaded into PostgreSQL(RDBMS) using below schema. The pipeline can be scheduled to run at a specific time interval, such as once a day or once a week, depending on the frequency of the updates.

To use the charger_models_UK.csv file in AWS with a relational database management system (RDMS), such as MySQL or PostgreSQL, we would first need to create a database with a table that has columns for each of the fields in the CSV file:
* id (auto-increment integer, primary key)
* ChargeDeviceManufacturer (varchar)
* LocationType (varchar)
* ChargeDeviceModel (varchar)
* PostCode (varchar)
* MonthUpdated (date)
* count (integer)

We could then use an AWS service such as AWS Glue or AWS Lambda to read the CSV file from S3, transform the data as necessary, and insert it into the RDMS table. For example, we could use AWS Glue to define a job that reads the CSV file, converts it to a DataFrame using pandas, and writes the DataFrame to the RDMS using a JDBC connection

In case the source data suffers regular changes, it required to modify the ETL pipeline to handle the regular updates. One way to do this is to compare the new data with the existing data in the PostgreSQL(RDBMS) and insert or update the rows accordingly. This can be done using SQL commands like INSERT INTO and UPDATE.
We also need to ensure that the schema of the CSV file remains consistent with the schema of the database table, otherwise it may need to modify the table schema or program accordingly.

Overall, the proposed solution involves using Python, AWS S3, an RDBMS, and data visualization tools to collect, process, store, and analyze data on electric vehicle charging points in the UK. The solution is scalable, maintainable, and extensible, and can provide valuable insights for many users or use cases in the field of sustainable transportation.