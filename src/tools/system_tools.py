#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports:
import os

###############################################################################
#================================ SYSTEM TOOLS ===============================#
###############################################################################

def run_command(command):
    """
    Runs the specified command in the input string and returns a string with
    the output.
    """
    
    call = os.popen(command)
    output = call.read()
    call.close()
    return output

def clear():
    """
    Clears the Python terminal both on Windows and Linux.    
    """

    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux(here, os.name is 'posix')run java 
    else:
        _ = os.system('clear')
