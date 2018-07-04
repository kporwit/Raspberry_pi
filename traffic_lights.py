import RPi.GPIO as gpio
from time import *

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(21, gpio.OUT)
gpio.setup(20, gpio.OUT)
gpio.setup(16, gpio.OUT)

while True:
	gpio.output(21, 1)
	sleep(5)
	gpio.output(21, 0)
	gpio.output(20, 1)
	sleep(2)
	gpio.output(20, 0)
	gpio.output(16, 1)
	sleep(5)
	gpio.output(20, 1)
	sleep(2)
	gpio.output(20, 0)
	gpio.output(16, 0)
