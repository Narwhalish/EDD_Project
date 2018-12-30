#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
import time

class Uno:
    uno = PyMata3()
    dispense_rate = 2
    motor_spd = 100
    MOTOR_PIN = 3

    desired_amount = 510

    def __init__(self):
        self.uno.set_pin_mode(self.MOTOR_PIN, Constants.PWM)

    def set_amount(self, amount):
        self.desired_amount = amount
        # print(f'the amount is {self.desired_amount}')

    def pour_amount(self):
        print('pouring')
        self.uno.analog_write(self.MOTOR_PIN, self.motor_spd)
        time.sleep(3)
        self.uno.analog_write(self.MOTOR_PIN, 0)
        # time.sleep(self.desired_amount / self.dispense_rate)
        # self.uno.analog_write(self.MOTOR_PIN, 0)

    def clean_container(self):
        self.uno.analog_write(self.MOTOR_PIN, 255)

#board = Uno()
#while True:
#    board.pour_amount()
