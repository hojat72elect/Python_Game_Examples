import pyglet

"""
This example draws a window and writes a label in the middle of it.
"""

if __name__ == '__main__':
    window = pyglet.window.Window()
    label = pyglet.text.Label(
        text="Example 1",
        font_size=36,
        x=window.width // 2,
        y=window.height // 2,
        anchor_x="center",
        anchor_y="center"
    )

    @window.event
    def on_draw():
        window.clear()
        label.draw()

    pyglet.app.run()
