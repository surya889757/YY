import sys
import Adafruit_DHT # import adafruit dht library.
import time
from Adafruit_IO import Client, Feed # import Adafruit IO REST client.

ADAFRUIT_IO_KEY = 'aio_eoWt76N5DRf8zAOSQFDwXPhEXLAQ'
ADAFRUIT_IO_USERNAME = 's8897576332'

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)# Create an instance of the REST client.


# Set up Adafruit IO Feeds.
temperature_feed = aio.feeds('temperature')
humidity_feed = aio.feeds('humidityy')



while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
        # Send humidity and temperature feeds to Adafruit IO
        temperature = '%.2f'%(temperature)
        humidity = '%.2f'%(humidity)
        aio.send(temperature_feed.key, str(temperature))
        aio.send(humidity_feed.key, str(humidity))
        print("dht11 uploaded")
        time.sleep(1)
    else:
        print("not upload")
