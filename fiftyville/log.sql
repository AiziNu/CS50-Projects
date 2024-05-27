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
--found id of fiftyville which is 8, now need to find flights
SELECT f.*, origin.full_name AS origin_airport, destination.full_name AS destination_airport
FROM flights f
JOIN airports origin ON f.origin_airport_id = origin_id
JOIN airports destination ON f.destination_airport_id = destination_id
WHERE origin.id = 8 AND f.year = 2023 AND f.month = 7 AND f.day = 29 ORDER BY f.hour, f.minute;

--we have ainfo we need to combine all info together
SELECT p.name
FROM bakery_security_logs bls
JOIN people p ON p.license_plate = bls.license_plate
JOIN bank_accounts ba ON ba.person_id = p.id
JOIN atm_transactions at ON at.account_number = ba.account_number
JOIN phone_calls pc ON pc.caller = p.phone_number
WHERE bls.year = 2023 AND bls.month = 7 AND bls.day = 28 AND bls.hour = 10 AND bls.minute BETWEEN 10 AND 15
AND at.atm_location = "Leggett Street" AND at.year = 2023 AND at.month = 7 AND at.day = 28 AND at.transaction_type = "withdraw"
AND pc.year = 2023 AND pc.month = 7 AND pc.day = 28 AND pc.duration < 60;

--check who is in the flight
SELECT p.name
FROM people p
JOIN passengers ps ON p.passport_number = ps.passport_number
WHERE ps.flight_id = 36
AND p.name IN ('Diana', 'Bruce')
--we find thief now need to find who Bruce called
SELECT p2.name AS receiver
FROM phone_calls pc
JOIN people p1 ON pc.caller = p1.phone_number
JOIN people p2 ON pc.receiver = p2.phone_number
WHERE p1.name = 'Bruce' AND pc.year = 2023 AND pc.month = 7 AND pc.day = 28 AND pc.duration < 60;
