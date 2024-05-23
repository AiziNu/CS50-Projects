import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
import sqlite3 

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
         # Get data from form
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")

        # Insert the new birthday into the database
        conn = sqlite3.connect("birthdays.db")
        db = conn.cursor()
        db.execute("INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)", (name, month, day))
        conn.commit()
        conn.close()

        return redirect("/")

    else:
        # Query the database for all birthdays
        conn = sqlite3.connect("birthdays.db")
        db = conn.cursor()
        db.execute("SELECT name, month, day FROM birthdays")
        birthdays = db.fetchall()
        conn.close()

        # Render the template with the birthdays data
        return render_template("index.html", birthdays=birthdays)

if __name__ == "__main__":
    app.run(debug=True)


