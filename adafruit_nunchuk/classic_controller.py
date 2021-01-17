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

* Wii Classic Controller https://en.wikipedia.org/wiki/Classic_Controller

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases
"""
from adafruit_nunchuk import NunchukBase


_DEFAULT_ADDRESS = 0x52


class ClassicController(NunchukBase):
    """Class which provides interface to the Nintendo Classic Controller."""

    def __init__(self, i2c, address=_DEFAULT_ADDRESS):
        super().__init__(i2c, address=address)

    @property
    def values(self):  # pylint: disable=too-many-locals
        """returns tuple of values"""

        self.read_data()

        # https://wiibrew.org/wiki/Wiimote/Extension_Controllers/Classic_Controller

        jrx = (self.buffer[0] & 0xC0) >> 3
        jrx |= (self.buffer[1] & 0xC0) >> 5
        jrx |= (self.buffer[2] & 0x80) >> 7
        jry = self.buffer[2] & 0x1F

        # left joystick
        jlx = self.buffer[0] & 0x3F
        jly = self.buffer[1] & 0x3F

        # analog trigger - left
        atl = (self.buffer[2] & 0x60) >> 2  # pylint: disable=invalid-name
        atl |= (self.buffer[3] & 0xE0) >> 5  # pylint: disable=invalid-name

        # analog trigger - right
        atr = self.buffer[3] & 0x1F  # pylint: disable=invalid-name

        # D-Pad
        dl = not bool(self.buffer[5] & 0x2)  # pylint: disable=invalid-name
        dr = not bool(self.buffer[4] & 0x80)  # pylint: disable=invalid-name
        du = not bool(self.buffer[5] & 0x1)  # pylint: disable=invalid-name
        dd = not bool(self.buffer[4] & 0x40)  # pylint: disable=invalid-name

        # Buttons
        A = not bool(self.buffer[5] & 0x10)  # pylint: disable=invalid-name
        B = not bool(self.buffer[5] & 0x40)  # pylint: disable=invalid-name
        X = not bool(self.buffer[5] & 0x8)  # pylint: disable=invalid-name
        btr = not bool(self.buffer[4] & 0x2)  # pylint: disable=invalid-name
        btl = not bool(self.buffer[4] & 0x20)  # pylint: disable=invalid-name
        Y = not bool(self.buffer[5] & 0x20)  # pylint: disable=invalid-name
        ZL = not bool(self.buffer[5] & 0x80)  # pylint: disable=invalid-name
        ZR = not bool(self.buffer[5] & 0x4)  # pylint: disable=invalid-name
        start = not bool(self.buffer[4] & 0x4)
        select = not bool(self.buffer[4] & 0x10)
        home = not bool(self.buffer[4] & 0x8)

        return (
            jrx,
            jry,
            jlx,
            jly,
            dl,
            dr,
            du,
            dd,
            A,
            B,
            X,
            Y,
            atr,
            atl,
            btr,
            btl,
            ZR,
            ZL,
            start,
            select,
            home,
        )

    @property
    def joystick_R(self):  # pylint: disable=invalid-name
        """Return tuple of current right joystick position."""

        return self.values[0], self.values[1]

    @property
    def joystick_L(self):  # pylint: disable=invalid-name
        """Return tuple of current left joystick position."""
        return self.values[2], self.values[3]

    @property
    def dpad_L(self):  # pylint: disable=invalid-name
        """Return current pressed state of D-pad left."""
        return self.values[4]

    @property
    def dpad_R(self):  # pylint: disable=invalid-name
        """Return current pressed state of D-pad right"""
        return self.values[5]

    @property
    def dpad_U(self):  # pylint: disable=invalid-name
        """Return current pressed state of D-pad up."""
        return self.values[6]

    @property
    def dpad_D(self):  # pylint: disable=invalid-name
        """Return current pressed state of D-pad down"""
        return self.values[7]

    @property
    def button_A(self):  # pylint: disable=invalid-name
        """Return current pressed state of the A button"""
        return self.values[8]

    @property
    def button_B(self):  # pylint: disable=invalid-name
        """Return current pressed state of the B button"""
        return self.values[9]

    @property
    def button_X(self):  # pylint: disable=invalid-name
        """Return current pressed state of the X button"""
        return self.values[10]

    @property
    def button_Y(self):  # pylint: disable=invalid-name
        """Return current pressed state of the Y button"""
        return self.values[11]

    @property
    def button_RT(self):  # pylint: disable=invalid-name
        """Return current pressed state of the right trigger button"""
        return self.values[14]

    @property
    def button_LT(self):  # pylint: disable=invalid-name
        """Return current pressed state of the left trigger button"""
        return self.values[15]

    @property
    def button_ZR(self):  # pylint: disable=invalid-name
        """Return current pressed state of the Zr button"""
        return self.values[16]

    @property
    def button_ZL(self):  # pylint: disable=invalid-name
        """Return current pressed state of the Zl button"""
        return self.values[17]

    @property
    def button_start(self):
        """Return current pressed state of the Start button"""
        return self.values[18]

    @property
    def button_select(self):
        """Return current pressed state of the Select button"""
        return self.values[19]

    @property
    def button_home(self):
        """Return current pressed state of the Home button"""
        return self.values[20]

    @property
    def button_plus(self):
        """Return current pressed state of the Plus(Start) button"""
        return self.button_start

    @property
    def button_minus(self):
        """Return current pressed state of the Minus(Select) button"""
        return self.button_select
