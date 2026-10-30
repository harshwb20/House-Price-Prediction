from flask import Flask, render_template, request, redirect, session, url_for
import mysql.connector
import joblib
import numpy as np

app = Flask(__name__)
app.secret_key = "secret_key"   # Required for session

# ---------------- LOAD MODEL ----------------
model = joblib.load("house_model.pkl")

# ---------------- DATABASE CONNECTION ----------------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="housepriceprediction_app"
)

cursor = db.cursor()

# ---------------- HOME ----------------
@app.route("/")
def home():
    return redirect(url_for("login"))

# ---------------- SIGNUP ----------------
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        sql = "INSERT INTO users (username, email, password) VALUES (%s,%s,%s)"
        cursor.execute(sql, (username, email, password))
        db.commit()

        return redirect(url_for("login"))

    return render_template("signup.html")

# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        sql = "SELECT * FROM users WHERE email=%s AND password=%s"
        cursor.execute(sql, (email, password))
        user = cursor.fetchone()

        if user:
            session['user_id'] = user[0]   # store user id in session
            session['username'] = user[1]  # optional
            return redirect(url_for("dashboard"))
        else:
            return "Invalid Email or Password"

    return render_template("login.html")

# ---------------- DASHBOARD ----------------
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():

    if 'user_id' not in session:
        return redirect(url_for("login"))

    user_id = session['user_id']

    if request.method == "POST":
        medinc = float(request.form["MedInc"])
        houseage = float(request.form["HouseAge"])
        rooms = float(request.form["AveRooms"])
        bedrooms = float(request.form["AveBedrms"])
        population = float(request.form["Population"])
        occup = float(request.form["AveOccup"])
        lat = float(request.form["Latitude"])
        lon = float(request.form["Longitude"])

        features = np.array([[medinc, houseage, rooms, bedrooms,
                              population, occup, lat, lon]])

        price = model.predict(features)[0] * 100000

        sql = """INSERT INTO predictions
                 (user_id, medinc, houseage, rooms, bedrooms,
                  population, occup, latitude, longitude, price)
                 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        cursor.execute(sql, (
            user_id, medinc, houseage, rooms,
            bedrooms, population, occup, lat, lon, price
        ))

        db.commit()

        return render_template("result.html",
                               price=round(price, 2))

    # GET request
    sql = """SELECT medinc, houseage, rooms, bedrooms,
             population, occup, latitude, longitude, price
             FROM predictions WHERE user_id=%s"""

    cursor.execute(sql, (user_id,))
    data = cursor.fetchall()

    return render_template("dashboard.html",
                           predictions=data,
                           username=session['username'])
# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)