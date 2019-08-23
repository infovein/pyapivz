#!/usr/bin/python3

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/hello/<name>")
def hello(name):
    return f"Hello {name} glad you could join us"
@app.route("/")
def hello_world():
    with open("helloworld.txt", "w") as hello:
        hello.write("you just wrote this line")
    return "File Created"

if __name__ == "__main__":
    app.run(port=5006)

