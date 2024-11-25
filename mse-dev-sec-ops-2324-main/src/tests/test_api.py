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

from urllib.parse import urlencode
import json

__author__ = 'Michael Mader'
__date__ = "2023-03-12"
__version__ = "0.2"
__email__ = "michael.maeder@hefr.ch"


def call(client, path, params):
    """calling function that simulates an API webcall of a specific route

    Args:
        client: this is the client object used by pytest to 'simulate'
                the API without running the webserver
        path:   route of the API to use
        params: GET parameter that are passed to the function

    Returns:
        json:   the result of the client call
    """
    url = path + '?' + urlencode(params)
    response = client.get(url)
    return json.loads(response.data.decode('utf-8'))


# increment test 1
def test_plus_one1(client):
    result = call(client, '/inc', {'x': 2})
    assert result['x'] == 3


# increment test 1
def test_plus_one2(client):
    result = call(client, '/inc', {'x': -2})
    assert result['x'] == -1


# adding test with negative value
def test_plus_y(client):
    result = call(client, '/add', {'x': -2, 'y': 7})
    assert result['result'] == 5


# multiplication test
def test_multiply(client):
    result = call(client, '/mul', {'x': -2, 'y': 7})
    assert result['result'] == -14


# division test
def test_division(client):
    result = call(client, '/div', {'x': 35, 'y': 7})
    assert result['result'] == 5


# *****************************************************************************
#                  Test cases for Q1.1
# *****************************************************************************

# Test increment with string input
def test_inc_with_string_input(client):
    result = call(client, '/inc', {'x': 'string'})
    assert 'error' in result
    msg = 'Invalid input. Please provide integer values for x and y.'
    assert result['error'] == msg


# Test increment without input
def test_inc_without_input(client):
    result = call(client, '/inc', {})
    assert 'error' in result
    msg = 'Invalid input. x parameter is required.'
    assert result['error'] == msg


# Test addition with one missing parameter
def test_add_missing_parameter(client):
    result = call(client, '/add', {'x': 5})
    assert 'error' in result
    msg = 'Invalid input. Both x and y parameters are required.'
    assert result['error'] == msg


# Test addition with non-numeric parameters
def test_add_non_numeric(client):
    result = call(client, '/add', {'x': 'foo', 'y': 'bar'})
    assert 'error' in result
    msg = 'Invalid input. Please provide integer values for x and y.'
    assert result['error'] == msg


# Test multiplication with float inputs
def test_mul_float_input(client):
    result = call(client, '/mul', {'x': '3.5', 'y': '2'})
    assert 'error' in result
    msg = 'Invalid input. Please provide integer values for x and y.'
    assert result['error'] == msg


# Test multiplication with special characters
def test_mul_special_chars(client):
    result = call(client, '/mul', {'x': '@', 'y': '!'})
    assert 'error' in result
    msg = 'Invalid input. Please provide integer values for x and y.'
    assert result['error'] == msg


# Test division by zero
def test_div_by_zero(client):
    result = call(client, '/div', {'x': 10, 'y': 0})
    assert 'error' in result
    msg = 'Division by zero is not allowed.'
    assert result['error'] == msg


# Test division with missing y parameter
def test_div_missing_y(client):
    result = call(client, '/div', {'x': 10})
    assert 'error' in result
    msg = 'Invalid input. Both x and y parameters are required.'
    assert result['error'] == msg
