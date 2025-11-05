from flask import Flask, request, render_template
import pymysql

app = Flask(__name__)

db = pymysql.connect(
    host="localhost",
    user="root",
    password="hsnbrfdhkn",
    database="test"
)

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]

    cursor = db.cursor()
    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    cursor.execute(sql, (name, email))
    db.commit()

    return f"<h3>Thanks, {name} Your Data Saved successfully</h3>"

if __name__ == "__main__":
    app.run(debug=True)