from typing import Optional, Tuple

import arcade
from arcade.types import RGBOrA255, RGBANormalized
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pong_Game"

class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('ball.png', 1.0)
        self.change_x = 50
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('bar.png', 0.5)


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.Bar = Bar()
        self.Ball = Ball()
        self.setup()

    def setup(self):
        self.Bar.center_x = SCREEN_WIDTH / 2
        self.Bar.center_y = SCREEN_HEIGHT / 5
        self.Ball.center_x = SCREEN_WIDTH / 2
        self.Ball.center_y = SCREEN_HEIGHT / 2

    def on_draw(self):
        self.clear((255, 255, 255))
        self.Bar.draw()
        self.Ball.draw()

    def update(self, delta):
        self.ball.update()



if __name__ == '__main__':
    Window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()