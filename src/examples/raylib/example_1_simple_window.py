"""
Example 1 : Just creates a window and then draws a text on it.
"""

import pyray

if __name__ == '__main__':
    pyray.init_window(800, 450, "Hello World")

    while not pyray.window_should_close():
        pyray.begin_drawing()

        pyray.clear_background(pyray.WHITE)
        pyray.draw_text("This is the example 1 of working with raylib", 190, 200, 20, pyray.VIOLET)

        pyray.end_drawing()

    pyray.close_window()
