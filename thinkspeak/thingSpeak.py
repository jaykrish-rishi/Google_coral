import thingspeak
import time
from ~/Adafruit_Python_DHT import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 3 

channel_id = 2114719 # put here the ID of the channel you created before

write_key = '2ULTO3VB2LK41EPL' #update the "WRITE KEY"

read_key = 'VHXVLT0203SGI8ZS'

def measure (channel):

    try:
        
        humidity , temperature = Adafruit_DHT.read_retry(sensor, pin)
        
        if humidity is not None and temperature is not None :
            print("Temperature = {0:0.1f}^C Humidity = {0:0.1f} %".format(temperature,humidity))

        else:
            print("'Did not receive any reading form sensor. Please check!")
        
        response = channel.update({'field1':temperature,'field2':humidity})

    except :

        print("connecyion failure")

if _name_ == "_main_":

    channel = thingspeak.Channel(id=channel_id, write_key=write_key)

    while True:

        measure(channel)

        time.sleep(16)