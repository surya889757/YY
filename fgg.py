import Adafruit_DHT
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


 
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN =11

GPIO.setup(DHT_PIN,GPIO.IN)
 
while True: 
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print("Sensor failure. Check wiring.");
    time.sleep(3);
