from gpiozero import LED, Button
from signal import pause

leds = [LED(pin) for pin in [20, 16, 7, 8]]
button = Button(25, pull_up=True)

def turn_on_all():
    for led in leds:
        led.on()

def turn_off_all():
    for led in leds:
        led.off()

button.when_pressed = turn_on_all
button.when_released = turn_off_all

pause()
