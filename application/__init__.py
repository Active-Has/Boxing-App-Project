from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Password@34.142.75.134:3306/flask_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = str(os.getenv('SECRET_KEY'))

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True)