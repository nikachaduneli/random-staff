from flask import Flask, render_template, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("home.html", title ='home')

@app.route('/result',methods=['POST'])
def results():

    result = ''


    first_num = request.form['first_num']
    sec_num = request.form['sec_num']
    operation = request.form['operation']

    if first_num.isdigit():
        first_num = int(first_num)
    else:
        result = "შეიყვანეთ რიცხვები!!! "
        return render_template("result.html", title ='result', result = result)

    if operation !='√':
        if sec_num.isdigit():
            sec_num = int(sec_num)
        else:
            result = "შეიყვანეთ რიცხვები!!! "
            return render_template("result.html", title ='result', result = result)



    if operation in ['+',"-", '/', '*', "√"]:
        if operation == '+':
            result = f'{first_num} {operation} {sec_num} = {first_num + sec_num}'
        elif operation == '-':
            result = f'{first_num} {operation} {sec_num} = {first_num - sec_num}'
        elif operation == '/':
            result = f'{first_num} {operation} {sec_num} = {first_num / sec_num}'
        elif operation == '*':
            result = f'{first_num} {operation} {sec_num} = {first_num * sec_num}'
        elif operation == "√":
            if sec_num != '':
                result = 'მეორე რიცვი საჭირო აღარაა'
            else:
                result = f'√{first_num} = {sqrt(first_num)}'
                return render_template("result.html", title ='result', result = result)
   
    return render_template("result.html", title ='result', result = result)


if __name__ == '__main__':
  app.run()