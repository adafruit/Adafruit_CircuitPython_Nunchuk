# SPDX-FileCopyrightText: 2021 David Glaude
#
# SPDX-License-Identifier: MIT
import board
import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_nunchuk.udraw import UDraw

udraw = UDraw(board.I2C())

m = Mouse(usb_hid.devices)

zDown = False
pDown = False

oldx = 4095
oldy = 4095

while True:

    px, py, pen, C, Z, pressure = udraw.values

    P = pen or C  # Both the C button and pen button work as LEFT mouse

    # Handeling the button to create mouse click
    if P and not pDown:
        m.press(Mouse.LEFT_BUTTON)
        pDown = True
    elif not P and pDown:
        m.release(Mouse.LEFT_BUTTON)
        pDown = False

    if Z and not zDown:
        m.press(Mouse.RIGHT_BUTTON)
        zDown = True
    elif not Z and zDown:
        m.release(Mouse.RIGHT_BUTTON)
        zDown = False

    # Values (4095,4095) mean the pen is not near the tablet
    if px == 4095 or py == 4095:
        oldx = 4095
        oldy = 4095
        continue  # We remember that the pen was raised UP

    # If we reach here, the pen was UP and is now DOWN
    if oldx == 4095 or oldy == 4095:
        oldx = px
        oldy = py
        continue

    if (px != oldx) or (py != oldy):  # PEN has moved we move the HID mouse
        m.move((px - oldx), (oldy - py), 0)
        oldx = px
        oldy = py
