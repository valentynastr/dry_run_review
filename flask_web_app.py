from flask import Flask           # import class Flask 
import json                       # import module json
import random                     # import module random

app = Flask(__name__)    # creating instance of the Flask class


@app.route('/')                         # decorator of python to bind a function to a URL
def index():                            # creating index() function
    return "Testing rolling two dice"   # returning string from function

@app.route('/dice')             # decorator of python to bind a function dice()to a URL
def dice():                     # creating dice() function
    count = 2                   # number of rolling two dice
    sum= 0                      
    for i in range(0,count):    # start rolling two dice
        first = dice_roll()
        second = dice_roll()
        sum += first + second
        if i == 0:
            fr_fd = first
            fr_sd = second
        if i == 1:
            sr_fd = first
            sr_sd = second
    d = {                      # create dictionary
        'first roll first dice': fr_fd,
        'first roll second dice': fr_sd,
        'second roll first dice': sr_fd,
        'second roll second dice': sr_sd,
        'Total result of rolling two dice': sum, 
        } 
    return (json.dumps(d))      # return result in JSON

def dice_roll():    # simulation of rolling dice
    return random.randint(1,6)

if __name__ == "__main__":    # application running
    app.debug = True          # turn on debugging mode
    app.run()                 # running local server
