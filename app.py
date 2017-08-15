from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.errorhandler(404)
def page_not_found(error):
    return "Sorry, this page was not found", 404 

if __name__ == "__main__":
    app.run(host="0.0.0.0")

