import pyb 
import random

leds = [pyb.LED(i) for i in range(1, 5)]

def slick():
    while True: 
        for led in leds: 
            led.toggle() 
            pyb.delay(100)                                                                                         

def das_blinken(delay):
    while True:
        led = leds[random.randint(0, len(leds)-1)]
        led.toggle()
        pyb.delay(delay)                                                                                         

das_blinken(10)
