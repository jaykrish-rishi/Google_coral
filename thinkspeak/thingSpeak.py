from urllib3 import HTTPConnectionPool as hp
import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 3 

channel_id = 2114719 # put here the ID of the channel you created before

wk = "2ULTO3VB2LK41EPL" #update the "WRITE KEY"

read_key = 'VHXVLT0203SGI8ZS'


def measure ():
	humidity , temperature =(0,0) #Adafruit_DHT.read_retry(sensor, pin)
	f= hp.urlopen(method="PUSH",url="https://api.thingspeak.com/update?api_key=2ULT03VB2LK41EPL&field1=0"
 )
	f.read()
	f.close()
	temperature = temperature + 1

while True :

	measure()
	time.sleep(16)


