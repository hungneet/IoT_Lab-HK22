
import sys
sys.path.append('./uart')
from uart_controller import UartController

AIO_FEED_IDs = ['button1', 'button2', 'button3', 'frequency', 'uart_frequency','pc_connection']

class AdaController:

    sensor_frequency = 0
    pre_humi =0
    pre_light = 0
    pre_temp =0 

    @staticmethod
    def connect(client):
        print("*** Connected")
        client.publish("pc_connection",1)
        for feed in AIO_FEED_IDs:
            client.subscribe(feed)
            client.publish(feed + '/get')

    @staticmethod
    def subscribe(client , userdata , mid , granted_qos):
        print("*** Subscribed to feed successfully")

    @staticmethod
    def disconnected(client):
        sys.exit(1)
        
    @classmethod
    def message(cls, client , feed_id , payload):
        print("*** Recived data from " + feed_id + ": " + payload)

        cls.set_frequency(feed_id, payload)

        UartController.write_serial(feed_id, payload)
        UartController.set_uart_frequency(feed_id, payload)

    @classmethod
    def set_frequency(cls, feed_id, payload):
        if feed_id == 'frequency':
            cls.sensor_frequency = int(payload)

    @classmethod
    def update_sensor(cls, client, count):
        if count == cls.sensor_frequency:
            
            humidity = UartController.get_humidity()
            temperature = UartController.get_temperature()
            light = UartController.get_light()

            if humidity != cls.pre_humi :
                client.publish("sensor1", humidity)
                print("*** Updating humidity: " + str(humidity))
                cls.pre_humi    = humidity
            
            if temperature != cls.pre_temp :
                client.publish("sensor2", temperature)
                print("*** Updating temperature: " + str(temperature))
                cls.pre_temp = temperature              

            if light != cls.pre_light :
                client.publish("sensor3", light)
                print("*** Updating light: " + str(light))
                cls.pre_light = light
                       
    @classmethod
    def update_sensor_count(cls, count):
        return count+1 if count < cls.sensor_frequency else 0
    
    @staticmethod
    def timeout(client):
        print("\nSystem Exit")
        client.publish('button1', '0')
        client.publish('button2', '0')
        client.publish('button3', '0')
        client.publish('sensor1', '0')
        client.publish('sensor2', '0')
        client.publish('sensor3', '0')
                
        client.publish("pc_connection",'0')
        sys.exit(1)
