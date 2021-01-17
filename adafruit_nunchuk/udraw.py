# SPDX-FileCopyrightText: Copyright (c) 2021 David Glaude
#
# SPDX-License-Identifier: MIT
"""
`udraw`
================================================================================
CircuitPython library for the Nintendo Wii uDraw GameTablet

* Author(s): David Glaude, John Furcean

Implementation Notes
--------------------

**Hardware:**

* Wii uDraw GameTablet http://wiibrew.org/wiki/Wiimote/Extension_Controllers/Drawsome_Tablet

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases
* Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
`adafruit_nunchuk.classic_controller`
"""
from adafruit_nunchuk import NunchukBase


_DEFAULT_ADDRESS = 0x52


class UDraw(NunchukBase):
    """Class which provides interface to the uDraw GameTablet."""

    def __init__(self, i2c, address=_DEFAULT_ADDRESS):
        super().__init__(i2c, address=address)

    @property
    def values(self):
        """Return tuple of values."""

        self.read_data()

        # http://wiibrew.org/wiki/Wiimote/Extension_Controllers/Drawsome_Tablet

        # position
        px = (self.buffer[2] & 0x0F) << 8  # pylint: disable=invalid-name
        px |= self.buffer[0]  # pylint: disable=invalid-name
        py = (self.buffer[2] & 0xF0) << 4  # pylint: disable=invalid-name
        py |= self.buffer[1]  # pylint: disable=invalid-name

        # pressure sensor reading
        pressure = self.buffer[3]

        # buttons
        pen = bool((self.buffer[5] & 0x04) >> 2)
        C = not bool((self.buffer[5] & 0x02) >> 1)  # pylint: disable=invalid-name
        Z = not bool((self.buffer[5] & 0x01))  # pylint: disable=invalid-name

        return px, py, pen, C, Z, pressure

    @property
    def position(self):
        """Return tuple of current position."""
        return self.values[0], self.values[1]

    @property
    def button_pen(self):
        """Return current pressed state of the PEN button"""
        return self.values[2]

    @property
    def button_C(self):  # pylint: disable=invalid-name
        """Return current pressed state of the C button"""
        return self.values[3]

    @property
    def button_Z(self):  # pylint: disable=invalid-name
        """Return current pressed state of the Z button"""
        return self.values[4]

    @property
    def pressure(self):
        """Return current pen pressure."""
        return self.values[5]
