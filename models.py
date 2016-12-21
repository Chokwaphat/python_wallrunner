import arcade.key
from random import randint

class Model:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

class Man(Model):
    def __init_(self, world, x, y):
        super().__init__(world, x, y, 0)
        self.vx = 0
        self.vy = 0

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.man = Man(self, 200, 50)
        
