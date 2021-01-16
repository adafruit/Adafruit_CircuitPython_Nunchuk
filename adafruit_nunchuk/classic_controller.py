# SPDX-FileCopyrightText: Copyright (c) 2021 John Furcean
#
# SPDX-License-Identifier: MIT
"""
`adafruit_nunchuk.classic_controller`
================================================================================
CircuitPython library for the Nintendo Wii Classic Controller

* Author(s): John Furcean

Implementation Notes
--------------------

**Hardware:**

* Wii Classic Controller http://wiibrew.org/wiki/Wiimote/Extension_Controllers/Classic_Controller

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases
"""
from adafruit_nunchuk import NunchukBase


_DEFAULT_ADDRESS = 0x52
_I2C_INIT_DELAY = 0.1
_I2C_READ_DELAY = 0.01


class ClassicController(NunchukBase):
    """Class which provides interface to the Nintendo Classic controller."""

    def __init__(self, i2c, address=_DEFAULT_ADDRESS):
        super().__init__(i2c, address=address)

    @property
    def joystick_right(self):
        """Return tuple of current right joystick position."""
        self.read_data()
        x = (self.buffer[0] & 0xC0) >> 3
        x |= (self.buffer[1] & 0xC0) >> 5
        x |= (self.buffer[2] & 0x80) >> 7

        return (x, self.buffer[2] & 0x1F)

    @property
    def joystick_left(self):
        """Return tuple of current left joystick position."""
        self.read_data()
        return (self.buffer[0] & 0x3F, self.buffer[1] & 0x3F)

    @property
    def trigger_right(self):
        """Return reading right trigger position"""
        self.read_data()
        return self.buffer[3] & 0x1F

    @property
    def trigger_left(self):
        """Return reading left trigger position"""
        self.read_data()
        return ((self.buffer[2] & 0x60) >> 2) | ((self.buffer[3] & 0xE0) >> 5)

    @property
    def dpad_left(self):
        """Return current pressed state of D-pad left."""
        self.read_data()
        return not bool(self.buffer[5] & 0x2)

    @property
    def dpad_right(self):
        """Return current pressed state of D-pad right"""
        self.read_data()
        return not bool(self.buffer[4] & 0x80)

    @property
    def dpad_up(self):
        """Return current pressed state of D-pad up."""
        self.read_data()
        return not bool(self.buffer[5] & 0x1)

    @property
    def dpad_down(self):
        """Return current pressed state of D-pad down"""
        self.read_data()
        return not bool(self.buffer[4] & 0x40)

    @property
    def button_a(self):
        """Return current pressed state of the A button"""
        self.read_data()
        return not bool(self.buffer[5] & 0x10)

    @property
    def button_b(self):
        """Return current pressed state of the B button"""
        self.read_data()
        return not bool(self.buffer[5] & 0x40)

    @property
    def button_x(self):
        """Return current pressed state of the X button"""
        self.read_data()
        return not bool(self.buffer[5] & 0x8)

    @property
    def button_y(self):
        """Return current pressed state of the Y button"""
        self.read_data()
        return not bool(self.buffer[5] & 0x20)

    @property
    def button_zr(self):
        """Return current pressed state of the Zr button"""
        self.read_data()
        return not bool(self.buffer[5] & 0x4)

    @property
    def button_zl(self):
        """Return current pressed state of the Zl button"""
        self.read_data()
        return not bool(self.buffer[5] & 0x80)

    @property
    def button_home(self):
        """Return current pressed state of the Home button"""
        self.read_data()
        return not bool(self.buffer[4] & 0x8)

    @property
    def button_start(self):
        """Return current pressed state of the Start/Plus button"""
        self.read_data()
        return not bool(self.buffer[4] & 0x4)

    @property
    def button_select(self):
        """Return current pressed state of the Select/Minus button"""
        self.read_data()
        return not bool(self.buffer[4] & 0x10)
