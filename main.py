from flask import Flask, render_template, url_for, redirect, request, session
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
import random
contact_finder = Flask(__name__)

contact_finder.config["SECRET_KEY"] = "5b67e0f2050ef0afe2737e9d8320e6e1"
contact_finder.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
contact_finder.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)

db = SQLAlchemy(contact_finder)


class employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    department = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(30), nullable=False)


    def __repr__(self):
        return f"employee('{self.id}','{self.name}','{self.surname}','{self.email}', '{self.department}')"


@contact_finder.route("/", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        eml = request.form.get("email")
        psw = request.form.get("password")
        existing_employee = employee.query.filter_by(email=eml).first()
        print(existing_employee)
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
            names_found = employee.query.filter_by(name=request.form.get("search_for").lower())
            return render_template("search.html",test=names_found)
        elif request.method == "POST" and request.form.get("checkbox") == "department":
            employees_in_dep = employee.query.filter_by(department=request.form.get("search_for").lower())
            return render_template("search.html",test=employees_in_dep)
        else:
            return render_template("search.html")
    else:
        return redirect(url_for("login"))


# names = ["James", "Robert", "John", "Michael", "David",
#          "Mary", "Patricia", "Jennifer", "Linda", "Elizabeth"]
# surnames = ["Martinez", "Anderson", "Taylor", "Thomas", "Hernandez", "Moore", "Martin", "Jackson", "Thompson", "White",
#             "Lopez", "Lee", "Gonzalez", "Harris", "Clark", "Lewis", "Robinson", "Walker", "Perez", "Hall"]
#
# x=0
# for namee in names:
#     surnamee = surnames[random.randint(4,13)].lower()
#     addd = employee( name=namee.lower(), surname=surnamee, email=namee+surnamee+str(x+7*x+4)+'@dell.com',
#                      department='sales', password='123456')
#     db.session.add(addd)
#     db.session.commit()
#     print(addd)
#     x=x+1



if __name__ == '__main__':
    contact_finder.run(debug=True)
