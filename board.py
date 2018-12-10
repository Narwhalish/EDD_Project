#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants

class Uno:
    uno = PyMata3()
    TRIG_PIN = 9
    ECHO_PIN = 10
    MOTOR_PIN = 3

    #should have a variable here for desired volume that's sent from pi

    def __init__(self):
        self.uno.set_pin_mode(self.MOTOR_PIN, Constants.PWM)
        self.uno.sonar_config(self.TRIG_PIN, self.ECHO_PIN)

    def get_distance(self):
        return self.uno.sonar_data_retrieve(self.TRIG_PIN)
        # pass

    def pour(self, desired_height):
        self.uno.analog_write(self.MOTOR_PIN, 50)
        if self.get_distance()

    def clean(self):


if __name__ == '__main__':
    board = Uno()
    while True:
        if board.get_distance() and board.get_distance() < 20:
            board.pour(1)
        else:
            board.pour(2)
