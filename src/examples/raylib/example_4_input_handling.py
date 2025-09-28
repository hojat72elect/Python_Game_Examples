from pyray import init_window, set_exit_key, load_texture, Vector2, window_should_close, is_key_down, get_frame_time, \
    begin_drawing, clear_background, draw_texture_v, end_drawing, BLACK, WHITE, close_window

from raylib import KEY_ESCAPE, Vector2Normalize, KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP

if __name__ == '__main__':
    init_window(1920, 1080, "Example 4 - Input handling")
    set_exit_key(KEY_ESCAPE)

    # Load spaceship
    ship_texture = load_texture("../../assets/spaceship.png")
    ship_pos = Vector2(0, 0)
    ship_direction = Vector2(0, 0)
    ship_speed = 800

    while not window_should_close():
        # Handle user input regarding spaceship
        ship_direction.x = int(is_key_down(KEY_RIGHT)) - int(is_key_down(KEY_LEFT))
        ship_direction.y = int(is_key_down(KEY_DOWN)) - int(is_key_down(KEY_UP))
        ship_direction = Vector2Normalize(ship_direction) # ?? What does this mean ??
        ship_direction = Vector2Normalize(ship_direction) # ?? What does this mean ??

        # update position
        dt = get_frame_time()
        ship_pos.x += ship_direction.x * (ship_speed * dt)
        ship_pos.y += ship_direction.y * (ship_speed * dt)

        # drawing
        begin_drawing()

        clear_background(BLACK)
        draw_texture_v(ship_texture, ship_pos, WHITE)

        end_drawing()

    close_window()
