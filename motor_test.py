#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants

motor_pin = 9
uno = PyMata3(1)

def setup():
    uno.set_pin_mode(13, Constants.OUTPUT)

def loop():
    uno.digital_write(13, Constants.HIGH)
    uno.sleep(1)
    uno.digital_write(13, Constants.LOW)
    uno.sleep(1)


# def setup():
#     uno.set_pin_mode(motor_pin, Constants.OUTPUT)
#
# def loop():
#     uno.analog_write(motor_pin, 255)

if __name__ == "__main__":
    setup()
    while True:
        loop()