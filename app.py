import os
from flask import Flask,render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("database")

db = SQLAlchemy(app)

migrate = Migrate(app, db)

class Process(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    firstName = db.Column(db.String(250))

    lastName = db.Column(db.String(250))

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName



@app.route('/')
def index():
    fullNames = Process.query.all()

    return render_template('index.html', fullNames=fullNames)


@app.route('/add', methods=['POST'])
def add():
    firstName = request.form['firstName']
    lastName = request.form['lastName']

    fullName = Process(firstName, lastName)


    db.session.add(fullName)
    db.session.commit()



    return redirect(url_for('index'))


def get_process(id):
    fullName = Process.query.get(id)

    if fullName is None:
        print("error not found")

    return fullName

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    fullName = get_process(id)

    firstName = request.form['firstName']
    lastName = request.form['lastName']

    fullName.firstName = firstName
    fullName.lastName = lastName

    db.session.commit()

    return redirect(url_for('index'))


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    fullName = get_process(id)

    firstName = request.form['firstName']
    lastName = request.form['lastName']

    db.session.delete(fullName)

    db.session.commit()

    return redirect(url_for('index'))






if __name__== "__main__":
    app.run(debug=True, port=5000)
