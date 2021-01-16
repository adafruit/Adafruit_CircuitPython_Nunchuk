"""
`adafruit_nunchuk`
================================================================================
Base Library for the Nunchuck Style libraries.
* Author(s): John Furcean 

Implementation Notes
--------------------

**Hardware:**

* `Wii Remote Nunchuk <https://en.wikipedia.org/wiki/Wii_Remote#Nunchuk>`_
* `Wiichuck <https://www.adafruit.com/product/342>`_

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases
* Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
"""
import time
from adafruit_bus_device.i2c_device import I2CDevice

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_PortalBase.git"

_DEFAULT_ADDRESS = 0x52
_I2C_INIT_DELAY = 0.1
_I2C_READ_DELAY = 0.01
_I2C_BUFFER_UPDATE_DELAY = .05


class NunchukBase:
    """Base Class which provides interface to Nintendo Nunchuk style controllers.
    :param i2c: An i2c device.
    :address: an i2c address.
                    Defaults to _DEFAULT_ADDRESS (0x52).
    """

    def __init__(self, i2c, address=_DEFAULT_ADDRESS):
        self.buffer = bytearray(6)
        self.i2c_device = I2CDevice(i2c, address)
        time.sleep(_I2C_INIT_DELAY)
        with self.i2c_device as i2c_dev:
            # turn off encrypted data
            # http://wiibrew.org/wiki/Wiimote/Extension_Controllers
            i2c_dev.write(b"\xF0\x55")
            time.sleep(_I2C_INIT_DELAY)
            i2c_dev.write(b"\xFB\x00")
        self.last_updated = time.monotonic()

    
    def _read_data(self):
        if (time.monotonic() - self.last_updated) > _I2C_BUFFER_UPDATE_DELAY:
            self.last_updated = time.monotonic()
            self._read_register(b"\x00")

    def _read_register(self, address):
        with self.i2c_device as i2c:
            time.sleep(_I2C_READ_DELAY)
            i2c.write(address)
            time.sleep(_I2C_READ_DELAY)
            i2c.readinto(self.buffer)
        time.sleep(_I2C_READ_DELAY)
        return self.buffer