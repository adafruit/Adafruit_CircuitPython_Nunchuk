# SPDX-FileCopyrightText: 2021 David Glaude
#
# SPDX-License-Identifier: MIT
import board
from adafruit_nunchuk.udraw import UDraw

controller = UDraw(board.I2C())

while True:

    # Pressure: (8-248)
    if controller.pressure != 8:
        print("Pen pressure: ", controller.pressure)

    if controller.position != (4095, 4095):
        print("Pen (x,y): ", controller.position)

    # Buttons: True of False
    if controller.button_pen:
        print("Button Pressed: Pen")
    if controller.button_C:
        print("Button Pressed: C")
    if controller.button_Z:
        print("Button Pressed: Z")
