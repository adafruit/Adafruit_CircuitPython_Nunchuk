# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_nunchuk

nc = adafruit_nunchuk.Nunchuk(board.I2C())

while True:
    joystick, buttons, acceleration = nc.values
    print("joystick = {},{}".format(joystick.x, joystick.y))
    print(
        "accceleration ax={}, ay={}, az={}".format(
            acceleration.x, acceleration.y, acceleration.z
        )
    )
    if buttons.C:
        print("button C")
    if buttons.Z:
        print("button Z")
    time.sleep(0.5)
