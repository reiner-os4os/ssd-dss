# BTPK and Flask imports
from BPTK_Py import BptkServer
from flask_cors import CORS
from flask import Flask, redirect, url_for, request, make_response, jsonify, Response, render_template

# Functions from the flask tutorial
# See here https://flask.palletsprojects.com/en/3.0.x/quickstart/
from markupsafe import escape
import json

# Functions to interact with SD maodel and client
from scenarioclass import ScenarioClass
from maininteract import take_request

# System dynamics model
from food_security import bptk_factory

# Calling the BptkServer class
application = BptkServer(__name__, bptk_factory)
CORS(application)

if __name__ == "__main__":
    application.run()

    
@application.route('/write_scenario', methods=['GET', 'POST'])
def run_function():
    inputjson = request.json
    scenariostring = take_request(inputjson)
    return scenariostring
