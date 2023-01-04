
from flask import Flask, render_template, request

app = Flask('__name__',)

def letter4search(phrase,letters):
  return set(phrase) & set(letters)


@app.route('/')
def home():
  return render_template('home.html', title = 'entry')

@app.route('/search', methods = ['POST'] )
def search():
  phrase = request.form['phrase']
  letters = request.form['letters']
  result = list(letter4search(phrase,letters))
  result_final = ''
  for i in range(len(result)):
    if i != 0:
      result_final +=f',{result[i]}' 
    else: result_final +=result[i]
  return render_template('search.html', title = 'search', result = result_final, phrase = phrase, letters = letters)




if __name__ == '__main__':
  app.run(debug=True)