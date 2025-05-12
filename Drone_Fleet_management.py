class Device:
    def __init__(self, device_id, model):
        self.device_id = device_id
        self.model = model

    def device_info(self):
        print(f"Device ID: {self.device_id}")
        print(f"Model: {self.model}")

class Flyer:
    def fly(self):
        print("Drone is Flying")
    
class Drone(Device, Flyer):
    def __init__(self, device_id, model, camera_quality):
        Device.__init__(self, device_id, model)
        self.camera_quality = camera_quality

    def capture_image(self):
        print(f"Capturing Image with {self.camera_quality} Camera")

    def drone_status(self):
        self.device_info()
        print(f"Camera Quality: {self.camera_quality}")

D1 = Drone("Drone101", "Dr-15XA", "4K HD")
D1.drone_status()
D1.fly()
D1.capture_image()