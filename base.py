from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from car_api import models, info_bank

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def home():

    firstCar = info_bank[0]['model']



    return render_template('homePage.html')


@app.route('/carInformation')
def detail():


    return render_template('carInformation.html')