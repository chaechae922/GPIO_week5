from gpiozero import LED, Button
from signal import pause

leds = [LED(pin) for pin in [20, 16, 7, 8]]
button = Button(25, pull_up=True)

def toggle_all():
    for led in leds:
        led.toggle()

button.when_pressed = toggle_all

pause()
