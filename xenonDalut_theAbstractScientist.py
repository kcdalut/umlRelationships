from abc import ABC, abstractmethod

class Sensor(ABC):

    @abstractmethod
    def get_reading(self):
        pass

class PHSensor(Sensor):
    def get_reading(self):
        return 7.4

class TempSensor(Sensor):
    def get_reading(self):
        return 36.5

# When I create an object from the Sensor class, it will raise an error because Sensor is an abstract class and cannot be instantiated directly.