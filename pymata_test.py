#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants

BOARD_LED = 13
board = PyMata3()


def setup():
    board.set_pin_mode(BOARD_LED, Constants.OUTPUT)
    
def loop():
    print("LED On")
    board.digital_write(BOARD_LED, 1)
    board.sleep(1.0)
    print("LED Off")
    board.digital_write(BOARD_LED, 0)
    board.sleep(1.0)


if __name__ == "__main__":
    setup()
    while True:
        loop()
