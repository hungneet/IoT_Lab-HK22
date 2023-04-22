import time
from Adafruit_IO import MQTTClient
from adafruit.ada_controller import *

AIO_USERNAME = 'hungneet'
AIO_KEY = '' #key is private 

client = MQTTClient(AIO_USERNAME , AIO_KEY)
print(client)
client.on_connect    = AdaController.connect
client.on_disconnect = AdaController.disconnected
client.on_message    = AdaController.message
client.on_subscribe  = AdaController.subscribe
client.connect()
client.loop_background()

def getClient() :
    time.sleep(3)
    return client
