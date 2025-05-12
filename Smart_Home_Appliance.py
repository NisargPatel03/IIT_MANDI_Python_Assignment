class Appliance:
    def status(self):
        print("Appliance is Working")

class Fan(Appliance):
    def status(self):
        print("Fan is Working")

class Light(Appliance):
    def status(self):
        print("Light is Glowing")

class AC(Appliance):
    def status(self):
        print("AC is ON")

F1 = Fan()
F1.status()

L1 = Light()
L1.status()

AC1 = AC()
AC1.status()