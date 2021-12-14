import board
import usb_hid
from microcontroller import pin

import lib.display as display
from lib.adafruit_hid.keyboard import Keyboard
from lib.adafruit_hid.keycode import Keycode
from lib.button import button
from lib.halleffectsensor import HallEffectSensor

keyboard = Keyboard(usb_hid.devices)
btn1 = button(board.GP15, board.GP14, keyboard, Keycode.A)
btn2 = button(board.GP13, board.GP12, keyboard, Keycode.D)
hallSensor = HallEffectSensor(board.GP16, keyboard, Keycode.W)
screen = display.Display(sda=pin.GPIO4, scl=pin.GPIO5)

old_speed = 0
speed = 0

while True:
    btn1.BUTTON()
    btn2.BUTTON()
    if hallSensor.HALLEFFECTSENSOR() > 2:
        speed = hallSensor.compute_average()
    if not old_speed == speed:
        print(speed)
        screen.speed(speed)
        old_speed = speed
