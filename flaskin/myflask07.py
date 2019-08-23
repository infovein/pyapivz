#!/usr/bin/python3

from flask import Flask, session, render_template, redirect, url_for, escape, request

app = Flask(__name__)

app.secret_key = "any random string"

## if user hits root of api
@app.route("/")
def index():
    if "username" in session:
        username = session.get("username")
        if 'visits' in session:
            session['visits'] = session.get('visits') + 1
        else:
            session['visits'] = 1
        visitno = f"total visits: {session.get('visits')}"
        return "<center>Logged in as " + username + "<br>You have visited " + visitno + " times<br><b><a href = '/logout'>click here to log out</a></center></b>"

    # if key 'username' does not exist in session
    return "<center>You are not logged in <br><a href = '/login'><b>click here to log in</b></a></center>"

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form.get("username")
        return redirect(url_for("index"))
    else:
        return """
        <form action = "/login" method = "post">
        <p><input type = "text" name = username></p>
        <p><input type = "submit" value = Login></p>
        </form>
        """

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))

@app.route("/delete-visits")
def delete_visits():
    if "username" in session:
        session.pop("visits", None)
        return "Visits Deleted"
    else:
        return "<center>Logged in as " + username + "<br> + <b><a href = '/logout'>click here to log out</a></center></b>"

if __name__ == "__main__":
    app.run(port=5006)



