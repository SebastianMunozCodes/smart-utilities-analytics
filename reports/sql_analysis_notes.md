## SQL Setup Notes

The cleaned CSV was loaded into a SQLite database named `utilities.db`.

The main table is `electricity_sales`.

A test query confirmed that the database contains the expected number of rows: 9,894.

An initial SQL aggregation query for total electricity sales by state matched the earlier Pandas analysis, with Texas appearing as the highest total electricity sales state.