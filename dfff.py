import time

import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import spidev
import os

import cv2
import smtplib
import os.path
from email.mime.text import MIMEText#email.mime.text.MIMEText(_text[, _subtype[, _charset]])
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase#email.mime.base.MIMEBase(_maintype(e.g. text or image), _subtype(e.g. plain or gif), **_params(e.g.key/value dictionary))
from email import encoders
from Adafruit_IO import Client, Feed, RequestError


ADAFRUIT_IO_KEY = 'aio_eoWt76N5DRf8zAOSQFDwXPhEXLAQ'
ADAFRUIT_IO_USERNAME = 's8897576332'

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)# Create an instance of the REST client.


# Set up Adafruit IO Feeds.
temperature_feed = aio.feeds('temperature')
humidity_feed = aio.feeds('humidityy')


email = 's8897576332@gmail.com'
password = 'surya8897'
send_to_email = 's8897576332@gmail.com'
subject = 'This is the subject'
message = 'This is my message from home'
file_location = '/home/pi/firstside0.png'
msg = MIMEMultipart()#Create the container (outer) email message.
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject
'''as.string() 
|
+------------MIMEMultipart 
              |                                                |---content-type 
              |                                   +---header---+---content disposition 
              +----.attach()-----+----MIMEBase----| 
                                 |                +---payload (to be encoded in Base64)
                                 +----MIMEText'''
msg.attach(MIMEText(message, 'plain'))#attach new  message by using the Message.attach





while True:
    print("with in cemara")
##    camera = cv2.VideoCapture(0)
##    for i in range(10):
##        return_value, image = camera.read()
##        cv2.imwrite('firstside'+str(i)+'.png', image)
##        print('firstside captured')
##        time.sleep(2)
##        break
##    del(camera)
    
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
    # Send humidity and temperature feeds to Adafruit IO
    temperature = '%.2f'%(temperature)
    humidity = '%.2f'%(humidity)
    aio.send(temperature_feed.key, str(temperature))
    aio.send(humidity_feed.key, str(humidity))
    print("dht11 uploaded")
    time.sleep(1)
    
    filename = os.path.basename(file_location)#function returns the tail of the path
    attachment = open(file_location, "rb") #“rb” (read binary)
    part = MIMEBase('application', 'octet-stream')#Content-Type: application/octet-stream , image/png, application/pdf
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)#Content-Disposition: attachment; filename="takeoff.png"
    msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com', 587)# Send the message via local SMTP server.
    print("with in msg")
    server.starttls()# sendmail function takes 3 arguments: sender's address, recipient's address and message to send
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    print("mail sended")
    server.quit()
                

GPIO.cleanup() 
