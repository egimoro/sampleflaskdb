import os
from flask import Flask,render_template, request, redirect, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]= os.environ.get('database')

db = SQLAlchemy(app)

migrate = Migrate(app, db)

ma = Marshmallow(app)

class Process(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(255))
    lastName = db.Column(db.String(255))

class ProcessSchema(ma.Schema):
    class Meta:
        fields = ("id", "firstName", "lastName")

process_schema = ProcessSchema()
processes_schema = ProcessSchema(many=True)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_process')
def add_process():

    firstName = request.args.get('firstName', 0, type=str)

    lastName = request.args.get('lastName', 0, type=str)

    fullName = Process(firstName=firstName, lastName=lastName)

    db.session.add(fullName)

    db.session.commit()

    result = process_schema.dump(fullName)


    return jsonify(result)


@app.route('/get_process')
def get_process():

    fullNames = Process.query.all()

    result = processes_schema.dump(fullNames)

    return jsonify(result)



if __name__== "__main__":
    app.run(debug=True, port=5000)
