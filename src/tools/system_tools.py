#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 11:25:59 2019

@author: noel
"""

import os
from time import sleep
from os import system, name

def run_command(command):
    call = os.popen(command)
    output = call.read()
    call.close()
    return output

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
