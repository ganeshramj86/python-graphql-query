import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.getcwd()}/person.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)