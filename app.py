from flask import Flask, render_template, request, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
import requests


app = Flask(__name__)
app.config["SECRET_KEY"] = "converter"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

toolbar = DebugToolbarExtension(app)

@app.route('/')
def home_page():

    return render_template("converter.html")


@app.route('/convert', methods=['GET','POST'])
def converter():
    if request.method == 'POST':
        from_currency = request.form['from']
        to_currency = request.form['to']
        amount = float(request.form['amount'])

        url = f'https://api.exchangerate.host/latest?base={from_currency}&symbols={to_currency}'
        response = requests.get(url)

        if response.ok:
            flash("You have successfully sent a request!")
            exchange_rate = response.json()['rates'][to_currency]
            converted_amount = amount * exchange_rate
            result = f'{to_currency} {converted_amount: .2f}'
            return result
        else:
            flash("You have sent an invalid request!")
            error = f'Error: {response.status_code}'
            return error
    else:
        return "Invalid request method. Please use the POST method to submit the form."
