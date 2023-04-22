import unittest
import sys
sys.path.append('./adafruit')
from ada_controller import AdaController


class TestAdafruit(unittest.TestCase):

    def setUp(self):
        self.controller = AdaController()

    def test_sensor_frequency_default(self):
        self.assertEqual(self.controller.sensor_frequency, 0)

    def test_set_frequency(self):
        self.controller.set_frequency('frequency', '10')
        self.assertEqual(self.controller.sensor_frequency, 10)
    
    def test_set_frequency_invalid(self):
        self.controller.set_frequency('frequency', 'invalid')
        self.assertEqual(self.controller.sensor_frequency, 0)
    
    def test_set_frequency_negative(self):
        self.controller.set_frequency('frequency', '-10')
        self.assertEqual(self.controller.sensor_frequency, 0)
    
    def test_set_frequency_zero(self):
        self.controller.set_frequency('frequency', '0')
        self.assertEqual(self.controller.sensor_frequency, 0)
    

