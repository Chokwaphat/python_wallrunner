import arcade
from models import World
import pyglet.gl as gl

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)

        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)

    def draw(self):
        self.sync_with_model()
        super().draw()

class WallRunnerGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.GREEN)
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.man_sprite = ModelSprite('images/man.png',
                                      model=self.world.man)
        self.rock_sprite = ModelSprite('images/rock.png',
                                      model=self.world.rock)

    def animate(self, delta):
        self.world.animate(delta)

    def draw_rocks(self, coins):
        # for c in rocks:
        # if not c.is_collected:
            arcade.draw_texture_rectangle(c.x, c.y, c.width, c.height,
            self.rock_texture)

    def on_draw(self):
        arcade.set_viewport(self.world.man.x - SCREEN_WIDTH // 2,
                            self.world.man.x + SCREEN_WIDTH // 2,
                            self.world.man.y - 100,self.world.man.y + SCREEN_HEIGHT // 2,
                            )
        arcade.start_render()

        self.man_sprite.draw()

        gl.glDisable(gl.GL_TEXTURE_2D)
        self.rock_sprite.draw()

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

if __name__ == '__main__':
    window = WallRunnerGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
