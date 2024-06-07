from flask import Flask
from flask_mysqldb import MySQL
from config import Config
from routes import *

app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)

if __name__ == '__main__':
    app.run(debug=True)

