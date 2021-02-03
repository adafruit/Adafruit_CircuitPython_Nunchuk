# SPDX-FileCopyrightText: 2019 Carter Nelson for Adafruit Industries

# SPDX-License-Identifier: MIT

"""
`adafruit_nunchuk.classic_controller`
================================================================================

CircuitPython library for Wii Nintendo Classic Controller & Classic Controller Plus


* Author(s): Carter Nelson, John Furcean

Implementation Notes
--------------------

**Hardware:**

* `Wii Remote Nunchuk <https://en.wikipedia.org/wiki/Wii_Remote#Nunchuk>`_
* `Wiichuck <https://www.adafruit.com/product/342>`_
* `Adafruit Wii Nunchuck Breakout Adapter <https://www.adafruit.com/product/4836>`_

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases
* Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
"""
from collections import namedtuple
from adafruit_nunchuk import NunchukBase

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_Nunchuk.git"


class ClassicController(NunchukBase):
    """
    Class which provides interface to Nintendo Wii Classic Controller.

    :param i2c: The `busio.I2C` object to use.
    :param address: The I2C address of the device. Default is 0x52.
    :type address: int, optional
    :param i2c_read_delay: The time in seconds to pause between the
        I2C write and read. This needs to be at least 200us. A
        conservative default of 2000us is used since some hosts may
        not be able to achieve such timing.
    :type i2c_read_delay: float, optional
    """

    _Values = namedtuple("Values", ("joysticks", "buttons", "dpad", "triggers"))
    _Joysticks = namedtuple("Joysticks", ("rx", "ry", "lx", "ly"))
    _Buttons = namedtuple(
        "Buttons",
        (
            "A",
            "B",
            "X",
            "Y",
            "R",
            "L",
            "ZR",
            "ZL",
            "start",
            "select",
            "home",
            "plus",
            "minus",
        ),
    )
    _Dpad = namedtuple("Dpad", ("up", "down", "right", "left"))
    _Triggers = namedtuple("Trigers", ("right", "left"))

    def __init__(self, i2c, address=0x52, i2c_read_delay=0.002):
        super().__init__(i2c, address=address, i2c_read_delay=i2c_read_delay)

    @property
    def values(self):
        """The current state of all values."""
        self._read_data()
        return self._Values(
            self._joysticks(do_read=False),
            self._buttons(do_read=False),
            self._dpad(do_read=False),
            self._triggers(do_read=False),
        )

    @property
    def joysticks(self):
        """The current joysticks positions."""
        return self._joysticks()

    @property
    def buttons(self):
        """The current pressed state of all buttons."""
        return self._buttons()

    @property
    def dpad(self):
        """The current pressed state of the dpad."""
        return self._dpad()

    @property
    def triggers(self):
        """The current accelerometer reading."""
        return self._triggers()

    def _joysticks(self, do_read=True):
        if do_read:
            self._read_data()
        return self._Joysticks(
            (
                (self.buffer[0] & 0xC0) >> 3
                | (self.buffer[1] & 0xC0) >> 5
                | (self.buffer[2] & 0x80) >> 7
            ),  # rx
            self.buffer[2] & 0x1F,  # ry
            self.buffer[0] & 0x3F,  # lx
            self.buffer[1] & 0x3F,  # ly
        )

    def _buttons(self, do_read=True):
        if do_read:
            self._read_data()
        return self._Buttons(
            not bool(self._read_data()[5] & 0x10),  # A
            not bool(self._read_data()[5] & 0x40),  # B
            not bool(self._read_data()[5] & 0x8),  # X
            not bool(self._read_data()[5] & 0x20),  # Y
            not bool(self._read_data()[4] & 0x2),  # R
            not bool(self._read_data()[4] & 0x20),  # L
            not bool(self._read_data()[5] & 0x4),  # ZR
            not bool(self._read_data()[5] & 0x80),  # ZL
            not bool(self._read_data()[4] & 0x4),  # start
            not bool(self._read_data()[4] & 0x10),  # select
            not bool(self._read_data()[4] & 0x8),  # home
            not bool(self._read_data()[4] & 0x4),  # plus
            not bool(self._read_data()[4] & 0x10),  # minus
        )

    def _dpad(self, do_read=True):
        if do_read:
            self._read_data()
        return self._Dpad(
            not bool(self._read_data()[5] & 0x1),  # UP
            not bool(self._read_data()[4] & 0x40),  # DOWN
            not bool(self._read_data()[4] & 0x80),  # RIGHT
            not bool(self._read_data()[5] & 0x2),  # LEFT
        )

    def _triggers(self, do_read=True):
        if do_read:
            self._read_data()
        return self._Triggers(
            self._read_data()[3] & 0x1F,  # right
            (self.buffer[2] & 0x60) >> 2 | (self.buffer[3] & 0xE0) >> 5,  # left
        )
