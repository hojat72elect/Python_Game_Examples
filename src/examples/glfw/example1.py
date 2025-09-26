"""
Example 1 : Just creates an empty window which can be closed by user.

"""

import glfw

def main():

    # Initialize the library, and if it wasn't successful, finish up the code.
    if not glfw.init():
        return

    # Create a window
    window = glfw.create_window(640, 480, "Hello World", None, None)

    # If creating window wasn't successful, terminate the app.
    if not window:
        glfw.terminate()
        return

    # Make the context of the previously built window current for the calling thread.
    glfw.make_context_current(window)

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Render here

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    # User wants to close the window
    glfw.terminate()

if __name__ == "__main__":
    main()