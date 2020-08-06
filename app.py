import os
from flask import Flask,render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import  Marshmallow
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("database")

db = SQLAlchemy(app)

ma = Marshmallow(app)

migrate = Migrate(app, db)

class Process(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    firstName = db.Column(db.String(250))

    lastName = db.Column(db.String(250))

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

class ProcessSchema(ma.Schema):
    class Meta:
        fields = ("firstName", "lastName")


process_schema = ProcessSchema()
processes_schema = ProcessSchema(many=True)


@app.route('/')
def signUp():
    return render_template('index.html')


@app.route('/process',methods=['POST'])
def add_process():


    firstName = request.form['firstName']

    lastName = request.form['lastName']

    fullName = Process(firstName, lastName)


    db.session.add(fullName)
    db.session.commit()
    result = process_schema.dump(fullName)


    return jsonify(result)

@app.route('/process', methods=['GET'] )
def get_process():
    fullName = Process.query.all()

    result = processes_schema.dump(fullName)

    return jsonify(result)



if __name__== "__main__":
    app.run(debug=True)
