#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants

TRIG_PIN = 9
ECHO_PIN = 10
board = PyMata3()

def setup():
    board.sonar_config(9, 10)

def loop():
    distance = board.sonar_data_retrieve(9)
    print(distance)

if __name__ == "__main__":
    setup()
    while True:
        loop()
