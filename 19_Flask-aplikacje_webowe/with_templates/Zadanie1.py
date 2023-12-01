# Zadanie: Stworzyć aplikację która nas wita po podaniu z formularza swojego imienia
# bazuje na app6.py

# flask --app Zadanie1 run

from flask import Flask, render_template, request

app = Flask(__name__)

data = []


@app.route('/')
def hello():
    return render_template('Zadanie1_form.html', data=data, tytul="To jest tytul z parametru")


@app.route('/add')
def add():
    args = request.args
    print(args)

    return render_template('Zadanie1_form.html', data=data, tytul=f'Witaj {args["name"]}')
