from pyray import load_texture, draw_texture, WHITE, init_window, window_should_close, get_frame_time, begin_drawing, \
    clear_background, BLACK, end_drawing, close_window
from os.path import join

class AnimatedSprite:
    def __init__(self):
        self.animation_frames = [load_texture(join('../../assets', 'animation1', f'{i}.png')) for i in range(8)]
        self.animation_index, self.animation_speed = 0, 10

    def update(self):
        dt = get_frame_time()
        self.animation_index += self.animation_speed * dt

    def draw(self):
        draw_texture(self.animation_frames[int(self.animation_index) % len(self.animation_frames)], 0, 0, WHITE)

if __name__ == '__main__':

    init_window(1920, 1080, 'Animations')
    animated_sprite = AnimatedSprite()

    while not window_should_close():
        animated_sprite.update()

        begin_drawing()
        clear_background(BLACK)
        animated_sprite.draw()
        end_drawing()

    close_window()
