from flask import Flask, render_template, url_for
from forms import RegistrateForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '21ddb45fed31c83f3f4a16a736f5ae4d'

posts = [
{
	'athlete': 'Sam',
	'workout': '3 x 4 reps of 325lbs',
	'content': 'First Post Content',
	'date_posted' : 'May 3, 2020'
},
{
	'athlete': 'Nick',
	'workout': '3 x 1 reps of 1000lbs',
	'content': 'Second post content',
	'date_posted' : 'May 5, 2020'
}
]

@app.route("/")
@app.route("/homepage")
def homepage():
	return render_template('home.html', posts = posts)


@app.route("/info")
def information():
	return render_template('info.html', title = 'Information')

@app.route("/login")
def login():
	form = LoginForm()
	return render_template('login.html', title = "Login", form = form)

@app.route("/register")
def register():
	form = RegistrateForm()
	return render_template('register.html', title = "Register", form = form)


if __name__ == '__main__':
	app.run(debug=True)