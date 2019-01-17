#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
import time
# Create Uno class
class Uno:
    # Initialize PyMata3 and set motor_spd and MOTOR_PIN
    uno = PyMata3()
    motor_spd = 255
    MOTOR_PIN = 9

    dispense_rate = 5 # units in mL/second
    desired_amount = 0 # default value for desired_amount

    def __init__(self): # initialize class
        self.uno.set_pin_mode(self.MOTOR_PIN, Constants.PWM)

    def set_amount(self, amount): # set value for desired_amount
        self.desired_amount = amount

    def pour_amount(self): # begin pouring desired_amount at motor_spd for 5 mL/second
        self.uno.analog_write(self.MOTOR_PIN, self.motor_spd)
        time.sleep(self.desired_amount / self.dispense_rate)
        self.uno.analog_write(self.MOTOR_PIN, 0)

    def clean_container(self): # clean container by running pump at full speed for 10 seconds
        self.uno.analog_write(self.MOTOR_PIN, self.motor_spd)
        time.sleep(10)
        self.uno.analog_write(self.MOTOR_PIN, 0)

    def stop_pour(self): # end pouring, only used during testing functionality
        self.uno.analog_write(self.MOTOR_PIN, 0)

#board = Uno()
#while True:
#    board.pour_amount()
#    if input() == 'q':
#        break
#board.stop_pour()
#exit()
