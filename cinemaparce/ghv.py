import pygame, numpy as np
import time

KONST_TIME = 10

class Vector:
    def __init__(self, length, speed):
        self.speed = speed
        self.length = length
        self.x = length
        self.y = 0
        self.angle = 0

    def update_pos(self, time):
        self.angle = self.speed * np.pi / KONST_TIME * time
        self.angle = self.angle - self.angle // (np.pi * 2) * (np.pi * 2)
        self.x = self.length * np.cos(self.angle)
        self.y = self.length * np.sin(self.angle)

v = Vector(1, 10)
print(np.sin(np.pi))
v.update_pos(5)
print(v.x, v.y, v.angle)

    

    
