import arcade.key
from random import randint
import random
import math

UP_VY = 2
DOWN_VY = -2
LEFT_VX = -2
RIGHT_VX = 2
NUM_ROCK = 7
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600

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
        self.is_right = False
        self.is_up = False
        self.is_down = False
        # print("=================")

    def up(self):
        self.is_up = True
        self.vy = UP_VY

    def down(self):
        self.is_down = True
        self.vy = DOWN_VY

    def left(self):
        self.is_left = True
        self.vx = LEFT_VX

    def right(self):
        self.is_right = True
        self.vx = RIGHT_VX

    def wrap(self):
        if self.x > SCREEN_WIDTH:
            self.x = 0

        elif self.x < 0:
            self.x = SCREEN_WIDTH

        elif self.y > SCREEN_HEIGHT:
            self.y = 0

        elif self.y < 0:
            self.y = SCREEN_HEIGHT

    def animate(self, delta):
        if self.is_up:
            self.y += self.vy

        if self.is_down:
            self.y += self.vy

        if self.is_left:
            self.x += self.vx

        if self.is_right:
            self.x += self.vx

        self.wrap()

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.man = Man(self, 200, 50)
        self.rocks = []
        for i in range(NUM_ROCK):

            x = random.randrange(500)
            y = 400 + random.randrange(200)
            self.rock = Rock(x,y)
            self.rocks.append(self.rock)

    def animate(self, delta):
        self.man.animate(delta)
        for rock in self.rocks:
            rock.animate(delta)
        self.man.wrap()
        self.rock.wrap()


    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.UP:
            self.man.up()
        if key == arcade.key.DOWN:
            self.man.down()
        if key == arcade.key.LEFT:
            self.man.left()
        if key == arcade.key.RIGHT:
            self.man.right()

class Rock:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = random.randrange(360)

    def animate(self, delta_time):
        self.random_direction()
        self.move_forward()
        self.wrap()

    def move_forward(self):
        self.x += math.sin(-math.radians(self.angle))
        self.y += math.cos(-math.radians(self.angle))

    def wrap(self):
        if self.x > SCREEN_WIDTH:
            self.x = 0

        elif self.x < 0:
            self.x = SCREEN_WIDTH

        elif self.y > SCREEN_HEIGHT:
            self.y = 0

        elif self.y < 0:
            self.y = SCREEN_HEIGHT

    def random_direction(self):
        direction = bool(random.getrandbits(1))
        if direction:
            self.angle += 5
        else:
            self.angle -= 5
