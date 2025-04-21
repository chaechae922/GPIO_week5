from gpiozero import LED, Button
from time import sleep
from signal import pause

led_pins = [20, 16, 7, 8]
leds = [LED(pin) for pin in led_pins]
button = Button(25, pull_up=True)

def led_sequence():
    for led in leds:
        led.on()
        sleep(1)
        led.off()

button.when_pressed = led_sequence

pause()
