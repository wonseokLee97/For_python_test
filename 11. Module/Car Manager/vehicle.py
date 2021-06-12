# 탈것 : 속도, 색상

class Vehicle:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    def __str__(self):
        return str(self.speed)
