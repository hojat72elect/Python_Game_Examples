from src.examples.raylib.example_7_classes.Sprite import Sprite
from pyray import load_texture, Vector2, is_key_down, draw_texture_v, WHITE
from raylib import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP, Vector2Normalize

class Player(Sprite):
    def __init__(self, pos):
        super().__init__(pos, 400)
        self.texture = load_texture("../../../assets/spaceship.png")
        self.direction = Vector2()

    def update(self, dt):
        self.direction.x = int(is_key_down(KEY_RIGHT)) - int(is_key_down(KEY_LEFT))
        self.direction.y = int(is_key_down(KEY_DOWN)) - int(is_key_down(KEY_UP))
        self.direction = Vector2Normalize(self.direction)

        # update
        self.move(dt)

    def draw(self):
        draw_texture_v(self.texture, self.pos, WHITE)

