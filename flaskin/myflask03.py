#!/usr/bin/python3

from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route("/success/<name>")
def success(name):
    return f"Welcome {name}"

@app.route("/start")
def start():
    return render_template("postmaker.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("success", name = user))

    elif request.method == "GET":

        user = request.args.get("nm")
        return redirect(url_for("success", name = user))

if __name__ == "__main__":
    app.run(port=5006)

