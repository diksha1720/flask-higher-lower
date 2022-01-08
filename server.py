from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def guess():
    return '<center><h1>Guess a number</h1>' \
           '<img src="https://media.giphy.com/media/zJWAkCpWNrd6w/giphy-downsized-large.gif"/></center>'


@app.route('/<int:num>')
def check_num(num):
    if num == random_number:
        return '<center><h1>You guessed it right!!</h1>' \
               '<img src="https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif"/></center>'
    elif num < random_number:
        return '<center><h1>Your guessed number is too low!!</h1>' \
               '<img src="https://media.giphy.com/media/P8jmgo10wMngFsPG2V/giphy.gif"/></center>'
    else:
        return '<center><h1>Your guessed number is too high!!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"/></center>'


random_number = random.randint(1, 10)


if __name__ == '__main__':
    app.run(debug=True)

