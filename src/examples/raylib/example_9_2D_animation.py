from pyray import load_texture, draw_texture, WHITE, init_window, window_should_close, get_frame_time, begin_drawing, \
    clear_background, BLACK, end_drawing, close_window, Texture
from os.path import join


class AnimatedSprite:
    def __init__(self):
        self.animation_frames: list[Texture] = [load_texture(join('../../assets', 'animation1', f'{i}.png')) for i in range(8)]
        self.animation_index: int = 0
        self.animation_speed: int = 10

    def update(self, dt):
        self.animation_index += self.animation_speed * dt

    def draw(self):
        draw_texture(self.animation_frames[int(self.animation_index) % len(self.animation_frames)], 0, 0, WHITE)

if __name__ == '__main__':

    init_window(1920, 1080, 'Animations')
    animated_sprite = AnimatedSprite()

    while not window_should_close():
        '''
        delta time should always be defined in your launcher code and then be propagated
         to the underlying source code from there. 
        '''
        delta_time:float = get_frame_time()
        animated_sprite.update(delta_time)

        begin_drawing()
        clear_background(BLACK)
        animated_sprite.draw()
        end_drawing()

    close_window()
