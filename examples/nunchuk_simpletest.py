# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_nunchuk

nc = adafruit_nunchuk.Nunchuk(board.I2C())

while True:
    values = nc.values
    print("joystick = {},{}".format(values.sx, values.sy))
    print("accceleration ax={}, ay={}, az={}".format(values.ax, values.ay, values.az))
    if values.bc:
        print("button C")
    if values.bz:
        print("button Z")

    time.sleep(0.5)
