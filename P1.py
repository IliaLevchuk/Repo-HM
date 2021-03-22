from time import sleep

class TrafficLight:
    _colors = None

    def running(self):
        while True:
            print("Red")
            sleep(7)
            print("yellow")
            sleep(2)
            print("green")
            sleep(7)
            print("yellow")


TrafficLight = TrafficLight()
print(TrafficLight.running())
