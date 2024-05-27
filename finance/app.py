import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]
    stocks = db.execute("SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = ? GROUP BY symbol HAVING total_shares > 0", user_id)
    holdings = []
    total_value = 0

    for stock in stocks:
        quote = lookup(stock["symbol"])
        total = quote["price"] * stock["total_shares"]
        holdings.append({
            "symbol": stock["symbol"],
            "shares": stock["total_shares"],
            "price": usd(quote["price"]),
            "total": usd(total)
        })
        total_value += total

    cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
    total_value += cash

    return render_template("index.html", holdings=holdings, cash=usd(cash), total=usd(total_value))

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not symbol:
            return apology("must provide symbol")
        if not shares or int(shares) <= 0:
            return apology("must provide a positive number of shares")

        stock = lookup(symbol)
        if not stock:
            return apology("invalid symbol")

        shares = int(shares)
        user_id = session["user_id"]
        cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
        cost = shares * stock["price"]

        if cash < cost:
            return apology("can't afford")

        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)", user_id, stock["symbol"], shares, stock["price"])
        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", cost, user_id)

        return redirect("/")
    else:
        return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    user_id = session["user_id"]
    transactions = db.execute("SELECT symbol, shares, price, timestamp FROM transactions WHERE user_id = ? ORDER BY timestamp DESC", user_id)
    return render_template("history.html", transactions=transactions)

@app.route("/login", methods=["GET", "POST"])
def login():
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""
    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("must provide symbol")

        stock = lookup(symbol)
        if not stock:
            return apology("invalid symbol")

        return render_template("quoted.html", name=stock["name"], symbol=stock["symbol"], price=usd(stock["price"]))
    else:
        return render_template("quote.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    #forget all user_id
    session.clear()

    #User reahed Post method
    if request.method == "POST":

        #make sure that username is submitted username
        if not request.form.get("username"):
            return apology("must provide username", 400)
        #make sure that password is submitted username
        elif not request.form.get("password"):
            return apology("must provide password", 400)
        #make sure that password is submitted username
        elif not request.form.get("confirmation"):
            return apology("passwords must match", 400)
        #make sure that password and confirmation match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords do not match", 400)

        #Query database for username
        row = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        #Check Username isnot exist
        if len(row) != 0
            return apology("username already exist", 400)
        #insert new user to database
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)",
                   request.form.get("username"), generate_password_hash(request.form.get("password")))
        #Query for new user
        row = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        #Remember which user logged
        seesion["user_id"] = row[0]["id"]
        return redirect("/")
    #for Get method
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    user_id = session["user_id"]

    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))

        if not symbol:
            return apology("must provide symbol")
        if shares <= 0:
            return apology("must provide a positive number of shares")

        stock = lookup(symbol)
        if not stock:
            return apology("invalid symbol")

        user_shares = db.execute("SELECT SUM(shares) as total_shares FROM transactions WHERE user_id = ? AND symbol = ? GROUP BY symbol", user_id, symbol)[0]["total_shares"]
        if shares > user_shares:
            return apology("too many shares")

        price = stock["price"]
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)", user_id, symbol, -shares, price)
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", shares * price, user_id)

        return redirect("/")
    else:
        stocks = db.execute("SELECT symbol FROM transactions WHERE user_id = ? GROUP BY symbol", user_id)
        return render_template("sell.html", stocks=stocks)
