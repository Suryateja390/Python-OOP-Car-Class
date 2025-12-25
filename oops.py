class Car:

    def __init__(self):
        self.name = "BMW X3"
        self.price = 10000000
        self.color = "black"

    def accelerate(self):
        print("I am accelerating")
        print(self.color)

    def color_car(self):
        print("The color of car is", self.color)

    def brake_system(self):
        print("The car is stopped")


c1 = Car()

print(c1.name)
c1.accelerate()
c1.color_car()
c1.brake_system()
