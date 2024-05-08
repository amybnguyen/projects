import os
import datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session.__init__ import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

UPLOAD_FOLDER = './static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///365.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
@login_required
def portfolio():
    """Show portfolio of photos"""
    user_id = session["user_id"]
    images = db.execute("SELECT filepath, caption, date FROM images WHERE user_id = ? ORDER BY date", user_id)

    if request.method == "GET":
        return render_template(
            "home.html", database = images
        )
    else:
        return render_template(
            "home.html", database = images
        )

def delete():
    user_id = session["user_id"]


@app.route("/delete", methods=["GET", "POST"])
@login_required
def organize():
    """Allow photo deletion"""
    user_id = session["user_id"]

    if request.method == "GET":
        return render_template("delete.html")
    else:
        date = request.form.get("date")

    if not date:
        flash("Date must be selected.")
        return redirect("/delete")

    count = db.execute("SELECT COUNT(*) FROM images WHERE user_id = ? AND date = ?", user_id, date)
    if 0 in count[0].values():
        flash("No photo exists for that date.")
    else:
        path = db.execute("SELECT filepath FROM images WHERE user_id = ? AND date = ?", user_id, date)
        d = path[0]
        filepath = d.get('filepath')
        os.remove(filepath)

        try:
            new_upload = db.execute(
                "DELETE FROM images WHERE user_id = ? AND date = ?", user_id, date
            )
        except:
            return f'Error'

        flash('Deleted!')

    return redirect("/delete")

@app.route("/upload", methods=["GET", "POST"])
@login_required
def upload():
    """Allow photo upload"""
    user_id = session["user_id"]

    if request.method == "GET":
        return render_template("upload.html")

    else:
        file = request.files.get("image")
        date = request.form.get("date")
        caption = request.form.get("caption")
        timestamp = datetime.datetime.now()

        if not file:
            flash("Must select file.\n")
        elif not date:
            flash("Must select date.")
        elif not caption:
            flash("Must enter caption.")
        else:
            path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(path)

            count = db.execute("SELECT COUNT(*) FROM images WHERE user_id = ? AND date = ?", user_id, date)
            if 0 in count[0].values():
                try:
                    new_upload = db.execute(
                        "INSERT INTO images (date, filepath, caption, datetime, user_id) VALUES (?, ?, ?, ?, ?)", date, path, caption, timestamp, user_id
                    )
                    return redirect("/")
                except:
                    flash("Error")
            else:
                flash("Image already exists for that date.")
        return redirect("/upload")



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

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
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
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


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # if request method is GET, go to registration page
    if request.method == "GET":
        return render_template("register.html")

    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # ensure username was submitted
        if not username:
            return apology("must provide username", 400)

        # ensure password was submitted
        if not password:
            return apology("must provide password", 400)

        # ensure confirmation was submitted
        if not confirmation:
            return apology("must confirm password", 400)

        # ensure password and confirmation do not match
        if password != confirmation:
            return apology("passwords do not match", 400)

        # get hash for password
        hash = generate_password_hash(password)

        # add user to db
        try:
            new_user = db.execute(
                "INSERT INTO users (username, hash) VALUES (?, ?)", username, hash
            )
        except:
            return apology("username already exists")

        session["user_id"] = new_user

        # Redirect user to home page
        return redirect("/")


@app.route("/addcash", methods=["GET", "POST"])
@login_required
def add_cash():
    user_id = session["user_id"]

    return render_template(
        "portfolio.html"
    )

if __name__ == "__main__":
    app.run(debug=True)
