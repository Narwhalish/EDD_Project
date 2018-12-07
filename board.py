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
        self.uno.set_pin_mode(self.MOTOR_PIN, Constants.OUTPUT)
        self.uno.sonar_config(self.TRIG_PIN, self.ECHO_PIN, self.set_distance)

    def get_distance(self):
        return self.uno.sonar_data_retrieve(self.TRIG_PIN)

    def pour(self):
        self.uno.analog_write(self.MOTOR_PIN, 255)

if __name__ == '__main__':
    board = Uno()
    while True:
        if board.measure():
            print(board.measure())
            board.pour()
