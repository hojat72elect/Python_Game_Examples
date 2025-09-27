import pyray
if __name__ == '__main__':

    # Initialize window
    pyray.init_window(1920, 1080, "Example2 of Raylib")

    # Load the spaceship texture
    spaceship_texture = pyray.load_texture("../../assets/spaceship.png")
    spaceship_image = pyray.load_image("../../assets/spaceship.png")
    pyray.image_color_grayscale(spaceship_image)
    gray_spaceship_texture = pyray.load_texture_from_image(spaceship_image)

    # Load the cowboy texture
    cowboy_image = pyray.load_image("../../assets/animation1/0.png")
    pyray.image_color_invert(cowboy_image)
    inverted_cowboy_texture = pyray.load_texture_from_image(cowboy_image)

    # Load font
    font = pyray.load_font("../../assets/Zero Hour.otf")

    while not pyray.window_should_close():

        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)

        pyray.draw_pixel(100, 200, pyray.RED) # A red pixel
        pyray.draw_pixel_v(pyray.Vector2(200, 200), pyray.WHITE) # A white pixel

        # A green circle in the middle of a yellow circle.
        pyray.draw_circle_v(pyray.Vector2(1000, 600), 200, pyray.YELLOW)
        pyray.draw_circle(1000, 600, 100, pyray.GREEN)

        pyray.draw_line_ex(pyray.Vector2(0, 0), pyray.Vector2(500, 200), 16, (50, 60, 0, 255))

        # Display the loaded images
        pyray.draw_texture(spaceship_texture, 0, 0, pyray.WHITE)
        pyray.draw_texture_v(gray_spaceship_texture, pyray.Vector2(100, 0), pyray.WHITE)
        pyray.draw_texture(inverted_cowboy_texture, 1800, 900, pyray.WHITE)

        # display a text
        pyray.draw_text('Text 1 with default font', 0, 400, 50, pyray.WHITE) # write with the default font of the raylib
        pyray.draw_text_ex(font, 'Text 2 with custom font', pyray.Vector2(0, 600), 20, 0, pyray.BLUE)

        pyray.end_drawing()