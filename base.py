# Anthony Constante, Andy Espinoza, Abel Plascencia, Emily Grimaldo
# CST205
# Japanese Car Canvas
# This file was created by Andy
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from car_databank import info_bank
#from car_databank_copy import info_bank

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    #Setting the variables to the car names and picture names and returning it so that it can be used
    # within the html template.
    Cars = ['firstCar', 'secondCar', 'thirdCar', 'fourthCar', 'fifthCar', 'sixthCar', 'seventhCar', 'eigthCar', 'ninthCar', 'tenthCar', 'eleventhCar', 'twelvethCar', 'thirteenthCar', 'fourteenthCar', 'fifteenthCar', 'lastCar']
    logo = 'NightKids'
    stars = 'gold'
    lines = 'lines'
    return render_template('homePage.html', lines = lines, stars = stars, logo = logo, CN = info_bank, CIM = Cars)

@app.route('/carInformation/<choice>')
def carInformation(choice):
    #same as before except using different pictures this time. Also choice for whatever car the user wants to click.
    Cars = ['rx7Manga', 'gtrManga', '240sxManga', 'supraManga', 's2kManga', 'rsxManga', '300zxManga', 'nsxManga', 'integraManga', '350zManga', 'preludeManga', 'lancerManga', 'imprezaManga', 'miataManga', 'civicManga', 'mr2Manga']
    lines = 'lines'
    return render_template('carInformation.html',choice = choice, lines = lines, CIM = Cars, CN = info_bank)