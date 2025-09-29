from pyray import init_window, Vector2, RED, GREEN, BLUE, YELLOW, ORANGE, Color, Camera2D, window_should_close, \
    is_key_down, vector2_normalize, get_frame_time, begin_drawing, begin_mode_2d, clear_background, WHITE, \
    draw_circle_v, BLACK, end_mode_2d, end_drawing, close_window
from raylib import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP, KEY_S, KEY_A, KEY_W, KEY_Q

from random import randint, choice

if __name__ == '__main__':

    init_window(1920, 1080, "Example 6 - Camera Control")

    # Load player - Currently, our player is just a black circle.
    player_position = Vector2()
    player_radius = 50
    player_direction = Vector2()
    player_speed = 400

    # Draw numerous colorful circles on the screen.
    circles: list[tuple[Vector2, float, Color]] = [
        (
            Vector2(randint(-2_000, 2_000), randint(-1_000, 1_000)),  # position
            randint(50, 200),  # radius
            choice([RED, GREEN, BLUE, YELLOW, ORANGE])  # Randomly choose from these colors
        )
        for i in range(100)
    ]

    # camera
    camera = Camera2D()
    camera.zoom = 1
    camera.target = player_position # Camera's original position is the player
    camera.offset = Vector2(1920 / 2, 1080 / 2)
    camera.rotation = 0

    while not window_should_close():
        # Handle keyboard inputs
        player_direction.x = int(is_key_down(KEY_RIGHT)) - int(is_key_down(KEY_LEFT))
        player_direction.y = int(is_key_down(KEY_DOWN)) - int(is_key_down(KEY_UP))
        player_direction = vector2_normalize(player_direction)

        # movement
        dt = get_frame_time()
        player_position.x += player_direction.x * (player_speed * dt)
        player_position.y += player_direction.y * (player_speed * dt)

        # camera update
        rotate_direction = int(is_key_down(KEY_S)) - int(is_key_down(KEY_A))
        camera.rotation += (rotate_direction * dt) * 50

        zoom_direction = int(is_key_down(KEY_W)) - int(is_key_down(KEY_Q))
        camera.zoom += (zoom_direction * dt) * 2
        camera.zoom = max(0.2, min(2.0, camera.zoom))
        camera.target = player_position

        # drawing
        begin_drawing()
        begin_mode_2d(camera)

        clear_background(WHITE)
        for circle in circles:
            draw_circle_v(*circle)
        draw_circle_v(player_position, player_radius, BLACK)

        end_mode_2d()
        end_drawing()

    close_window()
