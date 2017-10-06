from __future__ import division
from flask import Flask, render_template, request, jsonify
from math import sqrt
from model import DataModel
import random

app = Flask(__name__)
data_model = DataModel()

@app.route('/')
def index():
    equations = data_model.get_prior_equations()
    return render_template('twitterhandlegenerator.html', equations = equations)
	
@app.route('/solve', methods=['POST'])
def solve():
    user_data = request.json
    userfirstname = user_data['firstname']
    animals = ['cat','dogg','moose','mole','shrimp','mongoose','octopus','dino','chimp','tostido','slug','burrito','thewoogirl','andtea', 'makesitrain','lovessleep','criesalone','isahuman','butt']
    handle = _create_handle(userfirstname, animals)
    return jsonify({'handle': handle})


def _create_handle(firstname, animals):
    handle = firstname + random.choice(animals)
    return handle

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
