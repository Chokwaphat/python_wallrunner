import arcade.key
from random import randint
import random

MAX_VY = 10
ACCY = 1
LEFT_VX = 10
RIGHT_VX = -10
class Model:
    def __init__(self, world, x, y, angle):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0

class Man(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)
        # print("=================")
        self.vx = 0
        self.vy = 0
        self.is_left = False
        # print("=================")

    def left(self):
        self.is_left = True
        self.vx = LEFT_VX

    def right(self):
        self.is_right = True
        self.vx = RIGHT_VX

    def animate(self, delta):
        if self.vy < MAX_VY:
            self.vy += ACCY
        self.y += self.vy
        if self.is_left:
            self.x -= self.vx
class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.man = Man(self, 200, 50)
        self.rock = Rock(random.randrange(400), 550, 0, 0)

    def animate(self, delta):
        self.man.animate(delta)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.LEFT:
            self.man.left()
        if key == arcade.key.RIGHT:
            self.man.right()
class Rock:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
