from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
