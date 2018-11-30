#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from pymata_aio.pymata3 import PyMata3

uno = PyMata3(2)

uno.set_pin_mode(13, OUTPUT)
while True:
    uno.digital_write(13, 1)
    uno.sleep(2)
    uno.digital_write(13, 0)
    uno.sleep(2)
