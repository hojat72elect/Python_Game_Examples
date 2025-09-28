from pyray import init_window, set_target_fps, load_texture, Vector2, get_frame_time, begin_drawing, clear_background, \
    BLACK, draw_texture_v, WHITE, draw_fps, window_should_close, end_drawing, close_window, Texture

if __name__ == '__main__':

    # Create the window
    init_window(1920, 1080, "Move")
    set_target_fps(100)

    # Load ship's texture
    ship: Texture = load_texture("../../assets/spaceship.png")

    ship_pos: Vector2 = Vector2(0, 0)  # initial position of the ship : (0 , 0)
    ship_direction: Vector2 = Vector2(1, 1)  # Initial direction of the ship
    ship_speed = 800

    while not window_should_close():

        # change the direction when ship reaches the end of the screen (the direction should be updated before updating the position).
        if ship_pos.y >= 1080 - 40:
            ship_direction.y = -1
        if ship_pos.x >= 1920 - 100:
            ship_direction.x = -1
        if ship_pos.y <= 0:
            ship_direction.y = 1
        if ship_pos.x <= 0:
            ship_direction.x = 1

        dt = get_frame_time()
        # Change the position of the ship according to its current position and direction
        ship_pos.x += ship_direction.x * (ship_speed * dt)
        ship_pos.y += ship_direction.y * (ship_speed * dt)

        begin_drawing()

        clear_background(BLACK)
        draw_texture_v(ship, ship_pos, WHITE)
        draw_fps(0, 0)

        end_drawing()

    close_window()
