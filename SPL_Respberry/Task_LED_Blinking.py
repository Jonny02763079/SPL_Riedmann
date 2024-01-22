import RPi.GPIO as GPIO
import time

on = str(input("Starten Sie mit e das Program\n"))
of = str(input("Beenden Sie mit a das Program\n"))

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

if on == "e" or on == "E":
    while True:
            GPIO.output(18,True)
            time.sleep(3)
            GPIO.output(18,False)
            time.sleep(1)
            GPIO.output(18,True)
            time.sleep(3)
            GPIO.output(18,False)
            time.sleep(1)
            GPIO.output(18,True)
            time.sleep(3)
            GPIO.output(18,False)
            time.sleep(1)