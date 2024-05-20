-- Keep a log of any SQL queries you execute as you solve the mystery.
sqlite3 fiftyville.db
sqlite> .tables
sqlite> .schema crime_scene_reports

sqlite> SELECT *
FROM crime_scene_reports
WHERE month = 7 AND day = 28 AND street = 'Humphrey Street';
.schema interviews
SELECT *
FROM interviews;.tables

SELECT * FROM interviews WHERE LOWER(transcript) LIKE '%bakery%';
