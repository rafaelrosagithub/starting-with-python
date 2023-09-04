# Object orientation in python

class Car:
    def __init__(self, brand, model, color, fuel):
        self.brand = brand
        self.model = model
        self.color = color
        self.fuel = fuel
        self.switched_on = False
        self.speed = 0

    def turn_on(self):
        if self.switched_on:
            print("Car is already on")
        else:
            print("Car on")
            self.switched_on = True

    def turn_off(self):
        if self.switched_on:
            print("Car off")
            self.switched_on = False
        else:
            print("Car is already off")

    def speed_up(self):
        if self.switched_on:
            self.speed += 1
            print(f"{self.speed}Km/h")
        else:
            print("Car off, unable accelerate")

    def brake(self):
        if self.switched_on:
            self.speed -= 1
            print(f"{self.speed}Km/h")
        else:
            print("Car off, it is not possible to brake")