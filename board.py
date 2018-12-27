#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants

class Uno:
    uno = PyMata3()
    TRIG_PIN = 9
    ECHO_PIN = 10
    MOTOR_PIN = 3
    current_distance = 0
    #should have a variable here for desired volume that's sent from pi

    def __init__(self):
        self.uno.set_pin_mode(self.MOTOR_PIN, Constants.PWM)
        self.uno.sonar_config(self.TRIG_PIN, self.ECHO_PIN, cb=self.set_distance, ping_interval=33, max_distance=50)

    def set_distance(self, data):
        self.current_distance = data

    def pour(self, desired_height):
        if self.current_distance:
            while self.current_distance <= desired_height:
                self.uno.analog_write(self.MOTOR_PIN, 127)
        self.uno.analog_write(self.MOTOR_PIN, 0)

    def clean(self):
        pass

board = Uno()
print(board.current_distance)
board.pour(30)
print(board.current_distance)
