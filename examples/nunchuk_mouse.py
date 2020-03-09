import board
import adafruit_nunchuk
from adafruit_hid.mouse import Mouse

THRESHOLD = 10

m = Mouse()
nc = adafruit_nunchuk.Nunchuk(board.I2C())

while True:
    x, y = nc.joystick
    x = (x - 128) // 2
    y = (128 - y) // 2
    if abs(x) > THRESHOLD:
        m.move(x, 0, 0)
    if abs(y) > THRESHOLD:
        m.move(0, y, 0)
    if nc.button_Z:
        m.click(Mouse.LEFT_BUTTON)
    if nc.button_C:
        m.click(Mouse.RIGHT_BUTTON)
