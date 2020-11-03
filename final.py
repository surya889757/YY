import time
#import digitalio
#import board
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
DHT_PIN = 26

DHT_SENSOR = Adafruit_DHT.DHT11
ADAFRUIT_IO_KEY = 'aio_vIGH46ksRHtjeW9g5OCZNa3AHgrI' # Set your APIO Key
 # Set to your Adafruit IO username.
ADAFRUIT_IO_USERNAME = 'Mahi_7013'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
##print ("Calibrating.....")
##time.sleep(2)
##
##print ("Place the object......")
print("working")

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))

