-- Keep a log of any SQL queries you execute as you solve the mystery.
sqlite3 fiftyville.db
sqlite> .tables
sqlite> .schema crime_scene_reports

SELECT *
FROM crime_scene_reports
WHERE month = 7 AND day = 28 AND street = 'Humphrey Street';
-- Check three witnesses
SELECT * FROM interviews WHERE transcript LIKE '%bakery%';
--Witness1 Ruth, bakery footage
SELECT * FROM bakery_security_logs WHERE year = 2023 AND month = 7 AND day = 28 AND hour = 10 AND minute BETWEEN 10 AND 15;
--license_plate 13FNH73
