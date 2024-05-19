from machine import Pin
from utime import sleep

led = Pin(5, Pin.OUT)
while True:
  led.toggle()
  sleep(2)
