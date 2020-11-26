from random import randint
from flask import Flask, render_template
application = Flask(__name__)

@application.route('/')
def hello():
    return render_template('index.html')

@application.route('/d4')
def four():
    return render_template('roll.html', roll=str(rollDie(4)), bone="d4")

@application.route('/d6')
def six():
    return render_template('roll.html', roll=str(rollDie(6)), bone="d6")

@application.route('/d8')
def eight():
    return render_template('roll.html', roll=str(rollDie(8)), bone="d8")

@application.route('/d10')
def ten():
    return render_template('roll.html', roll=str(rollDie(10)), bone="d10")

@application.route('/2d6')
def twoD6():
    first = rollDie(6)
    second = rollDie(6)
    return render_template('roll.html', roll=str(first) + " & " +  str(second), bone="2d6")


@application.route('/d12')
def twelve():
    return render_template('roll.html', roll=str(rollDie(12)), bone="d12")

@application.route('/d20')
def twenty():
    return render_template('roll.html', roll=str(rollDie(20)), bone="d20")

@application.route('/d100')
def hundred():
    return render_template('roll.html', roll=str(rollDie(100)), bone="d100")

def rollDie(sides):
    die = Die(sides)
    return die.result

class Die():
    def __init__(self, sides):
        self.MAX = sides
        self.min = 1
        self.output = self.roll()
    def roll(self):
        self.result = randint(self.min, self.MAX)
        return self.result

if __name__ == '__main__':
    application.run()
