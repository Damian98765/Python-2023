# Zadanie: Stworzyć aplikację która nas wita po podaniu z formularza swojego imienia
# bazuje na app6.py

# flask --app Zadanie1 run

from flask import Flask, render_template, request

app = Flask(__name__)

data = []


@app.route('/')
def hello():
    return render_template('Zadanie2_form.html', data=data)


@app.route('/add', methods=['POST'])
def add():
    received = request.form
    print(received)
    print(received['name'])

    return render_template('Zadanie2_form.html', data=data, tytul=received["name"])
