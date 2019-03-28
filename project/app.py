import requests
from flask import Flask, render_template, url_for, flash, redirect, request
from forms import SignUp, LogIn
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SECRET_KEY']='7d130f7e6d0dda5cd0b904339b2113e36f33990c7118693fef344909c24320f7'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db' #sets path for db

db=SQLAlchemy(app) #sql alchemy db instance

class user(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	username=db.Column(db.String(20), unique=True, nullable=False)
	email=db.Column(db.String(120), unique=True, nullable=False)
	image=db.Column(db.String(20), nullable=False, default='default.jpg')
	password=db.Column(db.String(60), nullable=False)
	posts=db.relationship('post', backref='author', lazy=True)
	def __repre__(self):
		return f"user('{self.username}','{self.email}','{self.image}')"

class Post(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	title=db.Column(db.String(100),nullable=False)
	date_posted=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content=db.Column(db.Text, nullable=False)
	user_id=db.Column(db.Integer, db.ForeignKey('user.id', nullable=False))
	def __repre__(self):
		return f"user('{self.title}','{self.date_posted}')"

posts=[
	{
	'user':'shivali joshi',
	'title':'pav bhaji',
	'price':'120',
	'content':'xyz',
	'date_posted':'21 March 2019'
	},
	{
	'user':'shivali joshi',
	'title':'pav bhaji',
	'price':'120',
	'content':'xyz',
	'date_posted':'21 March 2019'
	},
	{
	'user':'shivali joshi',
	'title':'pav bhaji',
	'price':'120',
	'content':'xyz',
	'date_posted':'21 March 2019'
	}
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home',  posts=posts)


@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/signup", methods=['GET', 'POST'])
def signup():
	form=SignUp()
	if form.validate_on_submit():
		option =form.options.data
		print(option)
		if option=='1':
			return redirect(url_for('buyerprofile'))
		else:
			return redirect(url_for('sellerprofile'))
		flash(f'Successfully Account Created for {form.username.data}!', 'success')
	else:
		return render_template('signup.html',title='Sign Up', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	form=LogIn()
	return render_template('login.html',title='Log In', form=form)

@app.route("/buyerprofile")
def buyerprofile():
	form=buyerprofileform()
	return render_template('buyerprofile.html',title='Buyer Profile', form=form)

@app.route("/sellerprofile")
def sellerprofile():
	form=sellerprofileform()
	return render_template('sellerprofile.html',title='Seller Profile', form=form)



if __name__ == '__main__':
    app.run(debug=True)
