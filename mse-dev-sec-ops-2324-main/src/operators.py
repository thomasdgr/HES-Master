#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2024, School of Engineering and Architecture of Fribourg
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

__author__ = 'Michael Mader'
__date__ = "2023-03-12"
__version__ = "0.2"
__email__ = "michael.maeder@hefr.ch"


# file containing the operations for the calculator

# addition: returns x+y
def addition(x, y):
    return x+y


# subtraction: returns x-y
def subtraction(x, y):
    return x-y


# multiplication: returns x*y
def multiplication(x, y):
    return x*y


# division: returns x/y
#   returns None if the divisor is zero
#   the result might be of float type
def division(x, y):
    if y == 0:
        return None
    return x/y
