from pyray import Vector2, draw_rectangle_v, RED

from src.examples.raylib.example_7_classes.Sprite import Sprite

class Block(Sprite):
    def __init__(self, pos, speed):
        super().__init__(pos, speed)
        self.direction = Vector2(1,0)
        self.size = Vector2(100,200)

    def update(self, dt):
        self.move(dt)

    def draw(self):
        draw_rectangle_v(self.pos,self.size, RED)

