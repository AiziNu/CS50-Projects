-- Keep a log of any SQL queries you execute as you solve the mystery.
sqlite3 fiftyville.db
sqlite> .tables
sqlite> .schema crime_scene_reports

sqlite> SELECT *
FROM crime_scene_reports
WHERE date = 'YYYY-MM-DD' AND location = 'Crime Location';
