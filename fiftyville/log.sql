-- Keep a log of any SQL queries you execute as you solve the mystery.
sqlite3 fiftyville.db
sqlite> .tables
sqlite> .schema crime_scene_reports

SELECT *
FROM crime_scene_reports
WHERE month = 7 AND day = 28 AND street = 'Humphrey Street';

SELECT * FROM interviews WHERE transcript LIKE '%bakery%';

SELECT * FROM atm_transactions WHERE date = '2023-07-28' AND location = 'Leggett Street';
