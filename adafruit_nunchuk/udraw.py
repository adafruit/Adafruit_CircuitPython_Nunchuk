# SPDX-FileCopyrightText: Copyright (c) 2021 David Glaude
#
# SPDX-License-Identifier: MIT
"""
`udraw`
================================================================================
CircuitPython library for the Nintendo Wii uDraw GameTablet

* Author(s): David Glaude

Implementation Notes
--------------------

**Hardware:**

* Wii uDraw GameTablet http://wiibrew.org/wiki/Wiimote/Extension_Controllers/Classic_Controller

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases
* Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
`adafruit_nunchuk.classic_controller`
"""
from adafruit_nunchuk import NunchukBase


_DEFAULT_ADDRESS = 0x52
_I2C_INIT_DELAY = 0.1
_I2C_READ_DELAY = 0.01


class uDraw(NunchukBase):
    """Class which provides interface to the uDraw GameTablet."""

    def __init__(self, i2c, address=_DEFAULT_ADDRESS):
        super().__init__(i2c, address=address)

    @property
    def pressure(self):
        """Return current pen pressure."""
        self.read_data()
        return self.buffer[3]

    @property
    def button_pen(self):
        """Return current pressed state of the PEN button"""
        self.read_data()
        return bool((self.buffer[5] & 0x04) >> 2)

    @property
    def button_c(self):
        """Return current pressed state of the C button"""
        self.read_data()
        return not bool((self.buffer[5] & 0x02) >> 1)

    @property
    def button_z(self):
        """Return current pressed state of the Z button"""
        self.read_data()
        return not bool((self.buffer[5] & 0x01))

    @property
    def position(self):
        """Return tuple of current position."""
        self.read_data()
        return ((self.buffer[2] & 0x0F) << 8 | self.buffer[0]), (
            (self.buffer[2] & 0xF0) << 4 | self.buffer[1]
        )
