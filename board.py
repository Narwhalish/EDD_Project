#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants

class Uno:
    uno = Pymata3()
    ultraTrigPin = 9
    ultraEchoPin = 10


    def __init__(self):
        self.uno.set_pin_mode(ultraTrigPin, Constants.OUTPUT)
        self.uno.set_pin_mode(ultraEchoPin, Constants.INPUT)

    def measure(self):
        self.uno.digital_write(ultraTrigPin, LOW)
        self.uno.digital_write()


#
# def clean():
#     pass
