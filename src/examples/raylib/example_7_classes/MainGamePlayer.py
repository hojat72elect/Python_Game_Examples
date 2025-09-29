from pyray import init_window, Vector2, window_should_close, get_frame_time, begin_drawing, clear_background, BLACK, \
    end_drawing, close_window

from src.examples.raylib.example_7_classes.Block import Block
from src.examples.raylib.example_7_classes.Player import Player

if __name__ == '__main__':

    init_window(1920, 1080, 'OOP')
    sprites = [Player(Vector2(500, 200)), Block(Vector2(700, 0), 200)]

    while not window_should_close():

        dt = get_frame_time()
        for sprite in sprites:
            sprite.update(dt)

        begin_drawing()
        clear_background(BLACK)
        for sprite in sprites:
            sprite.draw()
        end_drawing()

    close_window()
