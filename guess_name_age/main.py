from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import requests

app = Flask(__name__)  

AGE_URL = "https://api.agify.io?name="
GENDER_URL = "https://api.genderize.io?name="

@app.route('/')
def starter():
    # Render a starter page with a form to enter your name
    return render_template("starter.html")

@app.route('/guess', methods=['GET'])
def guess():
    name = request.args.get('name')
    if not name:
        return redirect(url_for('starter'))
    
    current_year = datetime.now().year

    response_age = requests.get(AGE_URL + name)
    data_age = response_age.json()
    age = data_age.get('age', 'N/A')

    response_gender = requests.get(GENDER_URL + name)
    data_gender = response_gender.json()
    gender = data_gender.get('gender', 'N/A')

    return render_template("result.html", user=name, user_age=age, user_gender=gender, year=current_year)

if __name__ == "__main__":
    app.run(debug=True)
