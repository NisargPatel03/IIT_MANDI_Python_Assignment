from abc import ABC, abstractmethod

class SmartDevices(ABC):
    def __init__(self, name):
        self._name = name
        self.__is_on = False

    @abstractmethod
    def operate(self):
        pass

    def turn_on(self):
        self.__is_on = True
        print(f"{self._name} is now ON")

    def turn_off(self):
        self.__is_off = False
        print(f"{self._name} is now OFF")

    def show_status(self):
        if self.__is_on:
            status = "ON"
            print(f"{self._name} is currently {status}")
        else:
            status = "OFF"
            print(f"{self._name} is currently {status}")
    
    # Getter and Setter of is_on
    def is_on(self):
        return self.__is_on
    

class SmartLight(SmartDevices):
    def __init__(self, name):
        super().__init__(name)
        self.__brightness = 70  # Default Brightness

    def operate(self):
        self.turn_on()
        print(f"{self._name}: Brightness set to {self.__brightness}%")

    # Getter and Setter for Brightness
    def get_brightness(self):
        return self.__brightness
    
    def set_brightness(self, value):
        if 0 <= value <=100:
            self.__brightness = value
        else:
            print("Invalid Brightness Level. Must be Between 0 and 100")


class SmartFan(SmartDevices):
    def __init__(self, name):
        super().__init__(name)
        self.__speed = "Medium"   # Default Speed

    def operate(self):
        self.turn_on()
        print(f"{self._name}: Fan Speed set to {self.__speed}")

    # Getter and Setter for Brightness
    def get_speed(self):
        return self.__speed
    
    def set_speed(self, value):
        if value in ["Low", "Medium", "High"]:
            self.__speed = value
        else:
            print("Invalid Speed. Choose from Low, Medium, and High only")


class SmartAC(SmartDevices):
    def __init__(self, name):
        super().__init__(name)
        self.__temperature = 24   # Default Temperature

    def operate(self):
        self.turn_on()
        print(f"{self._name}: Temperature set to {self.__temperature}")

    # Getter and Setter for Brightness
    def get_temperature(self):
        return self.__temperature
    
    def set_temperature(self, value):
        if 16 <= value <= 30:
            self.__temperature = value
        else:
            print("Invalid Temperature. Must be Between 16 and 30")


print("----- Smart Home System Simulation -----")


light = SmartLight("Bedroom Light")
fan = SmartFan("Bedroom Fan")
ac = SmartAC("Bedroom AC")

devices = [light, fan, ac]

for i in devices:
    i.operate()
    i.show_status()
    print()


# Attempt to modify private attributes directly
print("----- Attempt to Direct Access of Private Attributes -----")
try:
    light.__brightness = 85
except AttributeError as e:
    print("Error:", e)

try:
    fan.__speed = "High"
except AttributeError as e:
    print("Error:", e)

try:
    ac.__temperature = 20
except AttributeError as e:
    print("Error:", e)

print()


# Modify values using setter and getter methods
print("----- Updating Values using Setter Method -----")
light.set_brightness(93)
print(f"Updated Brightness: {light.get_brightness()}%")

fan.set_speed("Low")
print(f"Updated Fan Speed: {fan.get_speed()}")

ac.set_temperature(21)
print(f"Updated AC Temperature: {ac.get_temperature()} Degree Celsius")