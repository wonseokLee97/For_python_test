from vehicle import *

# 자동차 : 속도, 생상, 바퀴, 좌석

class Car(Vehicle):
    def __init__(self, speed, color, wheels, seats):
        super().__init__(speed, color)
        self.wheels = wheels
        self.seats = seats


myCar = Car(10, 'white', 4, 4)