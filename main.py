from flask import Flask, render_template, url_for, redirect, request, session
from flask_sqlalchemy import SQLAlchemy

contact_finder = Flask(__name__)

@contact_finder.route("/")
def login():
    return render_template("login.html")


if __name__ == '__main__':
    contact_finder.run(debug=True)
