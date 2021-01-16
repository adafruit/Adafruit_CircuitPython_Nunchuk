# SPDX-FileCopyrightText: Copyright (c) 2021 John Furcean
#
# SPDX-License-Identifier: MIT
import board
from adafruit_nunchuk.classic_controller import ClassicController

controller = ClassicController(board.I2C())

while True:

    # Right Joystick: (0-31,0-31), middle is (16,16)
    if controller.joystick_right != (16, 16):
        print(f"Right Joystick (x,y): {controller.joystick_right}")

    # Left Joystick: (0-63,063), middle is (32,32)
    if controller.joystick_left != (32, 32):
        print(f"Left Joystick (x,y): {controller.joystick_left}")

    # Triggers: 0-31
    if controller.trigger_right > 0:
        print(f"Right Trigger: {controller.trigger_right}")
    if controller.trigger_left > 0:
        print(f"Left Trigger: {controller.trigger_left}")

    # DPad: True or False
    if controller.dpad_down:
        print("D-Pad Down Pressed")
    if controller.dpad_up:
        print("D-Pad Up Pressed")
    if controller.dpad_left:
        print("D-Pad Left Pressed")
    if controller.dpad_right:
        print("D-Pad Right Pressed")

    # Buttons: True of False
    if controller.button_zr:
        print("Button Pressed: Zr")
    if controller.button_zl:
        print("Button Pressed: Zl")
    if controller.button_a:
        print("Button Pressed: A")
    if controller.button_b:
        print("Button Pressed: B")
    if controller.button_x:
        print("Button Pressed: X")
    if controller.button_y:
        print("Button Pressed: Y")
    if controller.button_home:
        print("Button Pressed: HOME")
    if controller.button_start:
        print("Button Pressed: START")
    if controller.button_select:
        print("Button Pressed: SELECT")
