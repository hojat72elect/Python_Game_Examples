from pyray import init_window, image_color_grayscale, load_image, load_texture, load_texture_from_image, \
    image_color_invert, load_font, window_should_close, begin_drawing, clear_background, BLACK, draw_pixel, RED, WHITE, \
    Vector2, draw_pixel_v, draw_circle_v, YELLOW, GREEN, draw_circle, draw_line_ex, draw_texture, draw_texture_v, \
    draw_text, draw_text_ex, end_drawing, close_window, BLUE

if __name__ == '__main__':

    # Initialize window
    init_window(1920, 1080, "Example2 of Raylib")

    # Load the spaceship texture
    spaceship_texture = load_texture("../../assets/spaceship.png")
    spaceship_image = load_image("../../assets/spaceship.png")
    image_color_grayscale(spaceship_image)
    gray_spaceship_texture = load_texture_from_image(spaceship_image)

    # Load the cowboy texture
    cowboy_image = load_image("../../assets/animation1/0.png")
    image_color_invert(cowboy_image)
    inverted_cowboy_texture = load_texture_from_image(cowboy_image)

    # Load font
    font = load_font("../../assets/Zero Hour.otf")

    while not window_should_close():
        begin_drawing()
        clear_background(BLACK)

        draw_pixel(100, 200, RED)  # A red pixel
        draw_pixel_v(Vector2(200, 200), WHITE)  # A white pixel

        # A green circle in the middle of a yellow circle.
        draw_circle_v(Vector2(1000, 600), 200, YELLOW)
        draw_circle(1000, 600, 100, GREEN)

        draw_line_ex(Vector2(0, 0), Vector2(500, 200), 16, (50, 60, 0, 255))

        # Display the loaded images
        draw_texture(spaceship_texture, 0, 0, WHITE)
        draw_texture_v(gray_spaceship_texture, Vector2(100, 0), WHITE)
        draw_texture(inverted_cowboy_texture, 1800, 900, WHITE)

        # display a text
        draw_text('Text 1 with default font', 0, 400, 50,
                  WHITE)  # write with the default font of the raylib
        draw_text_ex(font, 'Text 2 with custom font', Vector2(0, 600), 20, 0, BLUE)

        end_drawing()

    close_window()
