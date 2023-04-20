import paho.mqtt.client as mqtt
import time

from periphery import GPIO

led = GPIO("/dev/gpiochip2", 13, "out") #pin 37


#import paho.mqtt.server as mqtt

# Define callback functions
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, message):
    print(message.topic+" "+str(message.payload))

# Create an MQTT broker instance
broker = mqtt.Mosquitto("myBroker")

# Set the callback functions
broker.on_connect = on_connect
broker.on_message = on_message

# Start the MQTT broker
broker.connect("localhost", 1883)
broker.subscribe("test/topic")

try:
    broker.loop_forever()
except KeyboardInterrupt:
    broker.disconnect()



# def on_connect(client, userdata, flags, rc):
#    global flag_connected
#    flag_connected = 1
#    client_subscriptions(client)
#    print("Connected to MQTT server")

# def on_disconnect(client, userdata, rc):
#    global flag_connected
#    flag_connected = 0
#    print("Disconnected from MQTT server")
   
# # a callback functions 
# def callback_esp32_sensor1(client, userdata, msg):
#     print('ESP sensor1 requesting for : ', msg.payload.decode('utf-8'),' the led')
#     operation = msg.payload.decode('utf-8')
    
#     if operation is "ON":
#         led.write(True)
#         time.sleep(2)
#     elif operation is "OFF" :
#         led.write(False)
#         time.sleep(2)

# def client_subscriptions(client):
#     client.subscribe("esp32/#")

# client = mqtt.Client("rpi_client1") #this should be a unique name
# flag_connected = 0

# client.on_connect = on_connect
# client.on_disconnect = on_disconnect
# client.message_callback_add('esp32/sensor1', callback_esp32_sensor1)


# # start a new thread
# client.loop_start()
# client_subscriptions(client)
# print("......client setup complete............")


# while True:
#     time.sleep(4)
#     if (flag_connected != 1):
#         print("trying to connect MQTT server..")
        
