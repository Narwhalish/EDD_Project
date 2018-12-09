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
        # self.uno.sonar_config(self.TRIG_PIN, self.ECHO_PIN)

    def get_distance(self):
        # return self.uno.sonar_data_retrieve(self.TRIG_PIN)
        pass

    def pour(self):
        for i in range(0, 256, 20):
            self.uno.analog_write(self.MOTOR_PIN, i)
            self.uno.sleep(0.25)
        for i in range(0, 256, 20):
            self.uno.analog_write(self.MOTOR_PIN, 255 - i)
            self.uno.sleep(0.25)
        # self.uno.analog_write(self.MOTOR_PIN, 300)
        # self.uno.sleep(2)
        # self.uno.analog_write(self.MOTOR_PIN, 127)
        # self.uno.sleep(2)

if __name__ == '__main__':
    board = Uno()
    while True:
        board.pour()
    # while True:
    #     distance = board.get_distance()
    #     if distance and distance > 10:
    #         # print(distance)
    #         board.pour()
