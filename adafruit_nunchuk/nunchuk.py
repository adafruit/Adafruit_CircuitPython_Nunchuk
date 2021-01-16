# SPDX-FileCopyrightText: 2019 Carter Nelson for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_nunchuk.nunchuck`
================================================================================

CircuitPython library for Nintendo Nunchuk controller

* Author(s): Carter Nelson

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
    def joystick(self):
        """Return tuple of current joystick position."""
        self.read_data()
        return self.buffer[0], self.buffer[1]

    @property
    def button_C(self):  # pylint: disable=invalid-name
        """Return current pressed state of button C."""
        self.read_data()
        return not bool(self.buffer[5] & 0x02)

    @property
    def button_Z(self):  # pylint: disable=invalid-name
        """Return current pressed state of button Z."""
        self.read_data()
        return not bool(self.buffer[5] & 0x01)

    @property
    def acceleration(self):
        """Return 3 tuple of accelerometer reading."""
        self.read_data()
        x = (self.buffer[5] & 0xC0) >> 6
        x |= self.buffer[2] << 2
        y = (self.buffer[5] & 0x30) >> 4
        y |= self.buffer[3] << 2
        z = (self.buffer[5] & 0x0C) >> 2
        z |= self.buffer[4] << 2
        return x, y, z
