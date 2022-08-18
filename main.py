from flask import Flask, render_template, url_for, redirect, request, session
from flask_sqlalchemy import SQLAlchemy
from datetime import  timedelta

contact_finder = Flask(__name__)

contact_finder.config["SECRET_KEY"] = "5b67e0f2050ef0afe2737e9d8320e6e1"
contact_finder.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
contact_finder.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)

db = SQLAlchemy(contact_finder)

test = ["John", "006900000", "6969", "john@freedom.free", "Finance Department"]

class employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"employee('{self.id}','{self.email}', '{self.password}')"


@contact_finder.route("/", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        eml = request.form.get("email")
        psw = request.form.get("password")
        existing_employee = employee.query.filter_by(email=eml).first()
        if existing_employee and existing_employee.password == psw:
            session['existing_employee'] = eml
            session.permanent = True
            return redirect(url_for("search"))
        else:
            return redirect(url_for("login"))
    else:
        if "existing_employee" in session:
            return redirect(url_for("search"))
        else:
            return render_template("login.html")


@contact_finder.route("/search", methods=['POST', 'GET'])
def search():
    if 'existing_employee' in session:
        if request.method == "POST" and request.form.get("checkbox") == "name":
            print(5)
            return redirect(url_for("search"))
        elif request.method == "POST" and request.form.get("checkbox") == "department":
            print(10)
            return redirect(url_for("search"))
        return render_template("search.html",test=test)
    else:
        return redirect(url_for("login"))





if __name__ == '__main__':
    contact_finder.run(debug=True)
