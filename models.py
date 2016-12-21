import arcade.key
from random import randint

MAX_VY = 10
ACCY = 1

class Model:
    def __init__(self, world, x, y, angle):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0

class Man(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)
        print("=================")
        self.vx = 0
        self.vy = 0
        print("=================")
    def animate(self, delta):
        if self.vy < MAX_VY:
            self.vy += ACCY
        self.y += self.vy

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        print("sddssddsdsd11111")
        self.man = Man(self, 200, 50)
        # self.init_platforms()
        print("sddssddsdsd")
        self.rock = Rock(150, 550, 0, 0)
    # def init_platforms(self):
    #     self.rocks = []
    #     for p in self.platforms:
    #         self.rocks += p.spawn_rocks()

    def animate(self, delta):
        self.man.animate(delta)


class Rock:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
