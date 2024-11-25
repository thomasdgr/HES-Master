#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2023, School of Engineering and Architecture of Fribourg
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import request, Flask, url_for, render_template, redirect
import operators
import json


__author__ = 'Michael Mader'
__date__ = "2024-03-12"
__version__ = "0.4"
__email__ = "michael.maeder@hefr.ch"


"""
DevSecOps lab

A little web application that offers API calls for arithmetic operations
"""


# creation of the Flask application
app = Flask(__name__)

# super secure key against CSRF attacks
app.config['SECRET_KEY'] = 'the best secret ever'
# would be better to use an environment variable
# app.config['SECRET_KEY'] = os.environ['SECRET_KEY']


# global variable containing the name of the login user
global_data = {'username': 'no_user'}


# incrementation route
@app.route('/inc')
def plus_one():
    x_arg = request.args.get('x')
    y_arg = request.args.get('y')
    if x_arg is None:
        msg = 'Invalid input. x parameter is required.'
        return json.dumps({'error': msg}), 400
    x, y = validate_input(x_arg, y_arg)
    return (x, y) if isinstance(x, str) else \
        (json.dumps({'x': operators.addition(x, 1)}), 200)


# addition route, the parameters will be passed with 'x' and 'y'
@app.route('/add')
def plus_y():
    x_arg = request.args.get('x')
    y_arg = request.args.get('y')
    if x_arg is None or y_arg is None:
        msg = 'Invalid input. Both x and y parameters are required.'
        return json.dumps({'error': msg}), 400
    x, y = validate_input(x_arg, y_arg)
    return (x, y) if isinstance(x, str) or y is None else \
        (json.dumps({'result': operators.addition(x, y)}), 200)


# multiplication route, the parameters will be passed with 'x' and 'y'
@app.route('/mul')
def multiply_y():
    x_arg = request.args.get('x')
    y_arg = request.args.get('y')
    if x_arg is None or y_arg is None:
        msg = 'Invalid input. Both x and y parameters are required.'
        return json.dumps({'error': msg}), 400
    x, y = validate_input(x_arg, y_arg)
    return (x, y) if isinstance(x, str) or y is None else \
        (json.dumps({'result': operators.multiplication(x, y)}), 200)


# division route, the parameters will be passed with 'x' and 'y'
@app.route('/div')
def division_y():
    x_arg = request.args.get('x')
    y_arg = request.args.get('y')
    if x_arg is None or y_arg is None:
        msg = 'Invalid input. Both x and y parameters are required.'
        return json.dumps({'error': msg}), 400
    x, y = validate_input(x_arg, y_arg)
    msg = 'Division by zero is not allowed.'
    return (x, y) if isinstance(x, str) or y is None else \
        (json.dumps({'error': msg}), 400) if y == 0 else \
        (json.dumps({'result': operators.division(x, y)}), 200)


# help route, giving some information about the API
@app.route('/help')
def unused():
    return "Super calculator API"


# default route, just showing the main page
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', app_data=global_data, )


# login route, the given username will be used to welcome the user
@app.route('/login', methods=['GET', 'POST'])
def login():
    # handle the POST request
    if request.method == 'POST':
        username = request.form["username"]
        print(f"got: {username}")
        if username is None or username == '':
            msg = 'Invalid input. Please provide a username.'
            return (json.dumps({'error': msg}), 400)
        global_data['username'] = request.form.get('username')
        return redirect(url_for('index'))
    # otherwise handle the GET request
    return render_template('login.html', title='Sign In',)


# function to validate the input, it should be an integer
def validate_input(x, y):
    try:
        x_int = int(x)
        if y is not None:
            y_int = int(y)
        else:
            return x_int, None
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
        msg = 'Invalid input. Please provide integer values for x and y.'
        return json.dumps({'error': msg}), 400
    return x_int, y_int
