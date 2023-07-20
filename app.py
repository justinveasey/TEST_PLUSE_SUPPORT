from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] ='thisisasecretkey'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/', methods=['POST','GET'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        new_item = User(
            name=name,
            email=email,
            password=password
        )
        try:
            db.session.add(new_item)
            db.session.commit()
            return redirect('/users')
        except:
            return 'There was an issue adding your task'
    else: 
        return render_template('index.html')

if __name__ == "__main__":
        app.run(debug=True)