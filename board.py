#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants

class Uno:
    uno = Pymata3()
    ultraTrigPin = 9
    ultraEchoPin = 10

    #should have a variable here for desired volume that's sent from pi

    def __init__(self):
        # self.uno.set_pin_mode(ultraTrigPin, Constants.OUTPUT)
        # self.uno.set_pin_mode(ultraEchoPin, Constants.INPUT)
        self.uno.sonar_config(ultraTrigPin, ultraEchoPin, )

    def measure(self):
        # clear Trig Pin
        self.uno.digital_write(ultraTrigPin, 0)
        self.uno.sleep(0.002)

        # set Trig Pin on High for 10 microseconds
        self.uno.digital_write(ultraTrigPin, 1)
        self.uno.sleep(0.010)
        self.uno.digital_write(ultraTrigPin, 0)

    def pour(self):
        #write motor speed
        #if area x sensed height = desired volume, stop motor





#
# def clean():
#     pass
