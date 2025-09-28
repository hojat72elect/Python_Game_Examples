from pyray import init_window, Vector2, Rectangle, window_should_close, get_mouse_position, check_collision_recs, \
    get_collision_rec, begin_drawing, clear_background, BLACK, draw_circle_v, draw_rectangle_rec, \
    BLUE, RED, GREEN, end_drawing, close_window

if __name__ == '__main__':

    init_window(1920, 1080, "Example 5 - 2D Collision detection")
    player_position = Vector2(0, 0)
    obstacle_position = Vector2(500, 400)
    obstacle_radius = 30

    player_rectangle = Rectangle(0, 0, 100, 200)
    obstacle_rectangle = Rectangle(800, 500, 200, 300)

    while not window_should_close():
        # Handle mouse input
        mouse_position = get_mouse_position()
        player_rectangle.x = mouse_position.x
        player_rectangle.y = mouse_position.y

        # Collision detection
        does_collide = check_collision_recs(player_rectangle, obstacle_rectangle)
        overlap_rectangle = get_collision_rec(player_rectangle, obstacle_rectangle)
        print(does_collide)

        # drawing
        begin_drawing()
        clear_background(BLACK)
        draw_circle_v(obstacle_position, obstacle_radius, RED)
        draw_rectangle_rec(player_rectangle, BLUE)
        draw_rectangle_rec(obstacle_rectangle, GREEN)

        if does_collide:
            draw_rectangle_rec(overlap_rectangle, RED)

        end_drawing()

    close_window()
