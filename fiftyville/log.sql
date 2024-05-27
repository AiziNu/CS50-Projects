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
--Witness2 Eugene, ATM transactions
SELECT * FROM atm_transactions WHERE atm_location = "Leggett Street" AND year = 2023 AND month = 7 AND day = 28;
--add name of withdraws
SELECT a.*, p.name FROM atm_transactions a JOIN bank_accounts b ON a.account_number = b.account_number JOIN people p ON b.person_id = p.id WHERE a.atm_location = "Leggett Street" AND a.year = 2023 AND a.month = 7 AND a.day = 28 AND a.transaction_type = "withdraw";
--Witness3 RAymond, phone calls
SELECT * FROM phone_calls WHERE year = 2023 AND month = 7 AND day = 28 AND duration < 60;
--add names to call list
SELECT p.name, pc.caller, pc.receiver, pc.year, pc.month, pc.day, pc.duration FROM phone_calls pc JOIN people p ON pc.caller = p.phone_number WHERE pc.year = 2023 AND pc.month = 7 AND pc.day = 28 AND pc.duration < 60;
--airport to search fiftyville
SELECT * FROM airports;
