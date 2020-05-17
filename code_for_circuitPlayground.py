from adafruit_circuitplayground.express import cpx
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from time import sleep
import usb_hid
from adafruit_circuitplayground import cp

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
pix = cpx.pixels
pix.brightness = 0.4
while True:
    x, y, z = cpx.acceleration
    for i in range(10):
        print(int(x),int(y),int(z))
        pix[i] = (abs(int(x))*10 %255,abs(int(y))*10 %255,abs(int(z))*10 %255)

    if cp.button_a:
        txt = ""
        txt2=""
        # with open('tweet.csv', encoding="utf8") as csv_file:
        #     csv_reader = csv.reader(csv_file, delimiter=',')
        #     for i,row in enumerate(csv_reader):
        #       if i ==0:
        #           continue
        #       if i>6:
        #           break
        #       txt += row[0]
        valid = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm .0987654321"
        with open('tweet.csv', 'r', encoding="utf8") as f:
            results = []
            for i,line in enumerate(f):
                if i ==0:
                    continue
                if i>6:
                    break
                words = line.split(',')
                txt += words[0][:-1]

            for i in txt:
                if i in valid:
                    txt2+=i
            # print(results)
            try:
                layout.write(txt2)
                kbd.press(Keycode.RETURN)
                kbd.release(Keycode.RETURN)
            except:
                    kbd.press(Keycode.RETURN)
                    kbd.release(Keycode.RETURN)

    if cp.button_b:
        kbd.press(Keycode.GRAVE_ACCENT)
        kbd.release(Keycode.GRAVE_ACCENT)