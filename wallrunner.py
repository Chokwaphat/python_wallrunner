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
        # self.rock_sprite = ModelSprite('images/rock.png',
        #                               model=self.world.rock)
        self.rock_sprites = []
        for rock in self.world.rocks:
            self.rock_sprites.append(ModelSprite(
                'images/rock.png', model=rock))

    def animate(self, delta):
        self.world.animate(delta)

    def on_draw(self):
        arcade.start_render()

        self.man_sprite.draw()

        for sprite in self.rock_sprites:
            sprite.draw()

        gl.glDisable(gl.GL_TEXTURE_2D)


    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

if __name__ == '__main__':
    window = WallRunnerGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
