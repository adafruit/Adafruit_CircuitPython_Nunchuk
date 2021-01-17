# SPDX-FileCopyrightText: Copyright (c) 2021 John Furcean
#
# SPDX-License-Identifier: MIT
import board
from adafruit_nunchuk.classic_controller import ClassicController

controller = ClassicController(board.I2C())

while True:

    # Right Joystick: (0-31,0-31), middle is (16,16)
    if controller.joystick_R != (16, 16):
        print(f"Right Joystick (x,y): {controller.joystick_R}")

    # Left Joystick: (0-63,063), middle is (32,32)
    if controller.joystick_L != (32, 32):
        print(f"Left Joystick (x,y): {controller.joystick_L}")

    # Triggers: 0-31
    if controller.trigger_R > 0:
        print(f"Right Trigger: {controller.trigger_R}")
    if controller.trigger_L > 0:
        print(f"Left Trigger: {controller.trigger_L}")

    # DPad: True or False
    if controller.dpad_D:
        print("D-Pad Down Pressed")
    if controller.dpad_U:
        print("D-Pad Up Pressed")
    if controller.dpad_L:
        print("D-Pad Left Pressed")
    if controller.dpad_R:
        print("D-Pad Right Pressed")

    # Buttons: True of False
    if controller.button_ZR:
        print("Button Pressed: ZR")
    if controller.button_ZL:
        print("Button Pressed: ZL")
    if controller.button_A:
        print("Button Pressed: A")
    if controller.button_B:
        print("Button Pressed: B")
    if controller.button_X:
        print("Button Pressed: X")
    if controller.button_Y:
        print("Button Pressed: Y")
    if controller.button_home:
        print("Button Pressed: Home")
    if controller.button_start:
        print("Button Pressed: Start")
    if controller.button_select:
        print("Button Pressed: Select")
    if controller.button_plus:
        print("Button Pressed: Plus")
    if controller.button_minus:
        print("Button Pressed: Minus")
