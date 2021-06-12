from car import *


class Sport(Car):
    def __init__(self, speed, wheels, seats, turbo, conv, color='white'):
        super().__init__(speed, color, wheels, seats)
        self.turbo = turbo
        self.conv = conv


