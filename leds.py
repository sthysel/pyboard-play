import pyb 
import random

leds = [pyb.LED(i) for i in range(1, 5)]

blue_led = pyb.LED(4)

def fanfare(delay=200):
    def switch_all(on=True):
        for led in leds:
            if on:
                led.on()
            else:
                led.off()

    for i in range(4):
        switch_all(on=True)
        pyb.delay(delay)
        switch_all(on=False)

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

def das_dico():
    try:
        fanfare()
        das_blinken(100)
    finally:
        fanfare()

def ramp_glow():
    intensity = 0
    while True:
        intensity = (intensity + 1) % 255
        blue_led.intensity(intensity)
        pyb.delay(20)

def glow():
    intensity = 0
    direction = 1

    while True:
        if intensity == 255:
            direction = -1
        if intensity == 0:
            direction = 1
        intensity = intensity + direction
        blue_led.intensity(intensity)
        pyb.delay(20)


glow()

