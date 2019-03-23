from flask import Flask, render_template, url_for, flash, redirect
from forms import SignUp, LogIn

app = Flask(__name__)
app.config['SECRET_KEY']='7d130f7e6d0dda5cd0b904339b2113e36f33990c7118693fef344909c24320f7'

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
		flash(f'Successfully Account Created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	else:
		print('INVALID')
	return render_template('signup.html',title='Sign Up', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	form=LogIn()
	return render_template('login.html',title='Log In', form=form)

if __name__ == '__main__':
    app.run(debug=True)
