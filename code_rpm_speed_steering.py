import time
import digitalio
import microcontroller
from busio import I2C
import busio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode


# Import the SSD1306 module.
import adafruit_ssd1306

count = 0 

btn1_pin = board.GP12
btn2_pin = board.GP15
btn3_pin = board.GP13



keyboard = Keyboard(usb_hid.devices)

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN


btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN


i2c = I2C(sda=microcontroller.pin.GPIO4wwwww, scl=microcontroller.pin.GPIO5)

display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
# Alternatively you can change the I2C address of the device with an addr parameter:
#display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x31)

# Clear the display.  Always call show after changing pixels to make the display
# update visible!
display.fill(0)
display.show()

while True:
    if btn1.value:
        print("button 1 pressed")
        keyboard.press(Keycode.W)
        time.sleep(0.1)
        keyboard.release(Keycode.W)
        if count < 3:
            if count == 0:
                start = time.time()
                count = count +  1
            else:
                count = count + 1
        else:
            display.fill(0)
            display.show()
            end = time.time()
            time_sec = end - start
            time_min = time_sec / 60
            rpm = 3 / time_min
            print(rpm, "rpm")
            speed = rpm * 0.44
            print(speed, "km/h")
            count = 0
            display.text(str(speed), 5, 0, 1, size=5)
            display.text("KM/U", 40, 50, 1, size=2)
            display.show()
    if btn2.value:
        print("button 2 pressed")
        keyboard.press(Keycode.A)
        time.sleep(0.1)
        keyboard.release(Keycode.A)
    if btn3.value:
        print("button 2 pressed")
        keyboard.press(Keycode.D)
        time.sleep(0.1)
        keyboard.release(Keycode.D)
