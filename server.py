from flask import Flask
import random


app = Flask(__name__)

number_to_guess = 0

@app.route('/')
def home():
    global number_to_guess
    number_to_guess = random.randint(0,9)
    return '<h1>Guess a number between 0 and 9</h1>\
            <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'



@app.route('/<int:number>')
def guess(number):

    if number < number_to_guess:
        return '<h1>TOO LOW</h1>\
                <img src="https://media.giphy.com/media/wdh1SvEn0E06I/giphy.gif">'
    elif number > number_to_guess:
        return '<h1>TOO HIGH</h1>\
                <img src="https://media.giphy.com/media/2cei8MJiL2OWga5XoC/giphy.gif">'
    else:
        return '<h1>YOU GUESSED IT</h1>\
                <img src="https://media.giphy.com/media/3oGRFp0AqM0BY4axjO/giphy.gif">'
















if __name__ == "__main__":
    app.run(debug=True)
