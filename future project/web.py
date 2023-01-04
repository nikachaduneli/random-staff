from logging import debug
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/user/<name>/<surname>')
def user(name,surname):
  return render_template('hello_user.html', fname = name, lname = surname)


@app.route('/<int:cyear>/<int:byear>')
def year(cyear, byear):
  return f'{cyear-byear} years old'
app.run(debug=True)