# SPDX-FileCopyrightText: 2019 Carter Nelson for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_nunchuk.nunchuck`
================================================================================

CircuitPython library for Nintendo Nunchuk controller

* Author(s): Carter Nelson, John Furcean

Implementation Notes
--------------------

**Hardware:**

* `Wii Remote Nunchuk <https://en.wikipedia.org/wiki/Wii_Remote#Nunchuk>`_
* `Wiichuck <https://www.adafruit.com/product/342>`_

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases
"""
from adafruit_nunchuk import NunchukBase

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_Nunchuk.git"

_DEFAULT_ADDRESS = 0x52


class Nunchuk(NunchukBase):
    """Class which provides interface to Nintendo Nunchuk controller."""

    def __init__(self, i2c, address=_DEFAULT_ADDRESS):
        super().__init__(i2c, address=address)

    @property
    def values(self):
        """Return tuple of values."""
        self.read_data()

        # https://wiibrew.org/wiki/Wiimote/Extension_Controllers/Nunchuck

        # joystick
        jx = self.buffer[0]  # pylint: disable=invalid-name
        jy = self.buffer[1]  # pylint: disable=invalid-name

        # buttons
        C = not bool(self.buffer[5] & 0x02)  # pylint: disable=invalid-name
        Z = not bool(self.buffer[5] & 0x01)  # pylint: disable=invalid-name

        # acceleration
        ax = (self.buffer[5] & 0xC0) >> 6  # pylint: disable=invalid-name
        ax |= self.buffer[2] << 2  # pylint: disable=invalid-name
        ay = (self.buffer[5] & 0x30) >> 4  # pylint: disable=invalid-name
        ay |= self.buffer[3] << 2  # pylint: disable=invalid-name
        az = (self.buffer[5] & 0x0C) >> 2  # pylint: disable=invalid-name
        az |= self.buffer[4] << 2  # pylint: disable=invalid-name

        return jx, jy, C, Z, ax, ay, az

    @property
    def joystick(self):
        """Return tuple of current joystick position."""
        return self.values[0], self.values[1]

    @property
    def button_C(self):  # pylint: disable=invalid-name
        """Return current pressed state of button C."""
        return self.values[2]

    @property
    def button_Z(self):  # pylint: disable=invalid-name
        """Return current pressed state of button Z."""
        return self.values[3]

    @property
    def acceleration(self):
        """Return 3 tuple of accelerometer reading."""
        return self.values[4], self.values[5], self.values[6]
