from pyray import init_window, load_model, window_should_close, get_frame_time, begin_drawing, clear_background, \
    begin_mode_3d, draw_grid, draw_model_ex, end_mode_3d, end_drawing, close_window, Camera3D, Vector3, WHITE, \
    matrix_scale
from raylib import CAMERA_PERSPECTIVE

if __name__ == '__main__':

    init_window(1920, 1080, "Example 11 - importing 3D models")
    camera = Camera3D()
    camera.position = Vector3(0.0, 3.0, 5.0)
    camera.target = Vector3(0.0, 0.0, 0.0)
    camera.up = Vector3(0.0, 1.0, 0.0)
    camera.fovy = 45.0
    camera.projection = CAMERA_PERSPECTIVE

    # Import 3D models
    ship = load_model("../../assets/ship.glb")
    rupee = load_model("../../assets/rupee.gltf")  # texture and bin file must be in the same directory

    rotation = 0

    while not window_should_close():
        rupee.transform = matrix_scale(0.5,0.5,0.5)
        dt = get_frame_time()
        rotation += 20 * dt
        begin_drawing()
        clear_background(WHITE)
        begin_mode_3d(camera)
        draw_grid(10, 1.0)
        draw_model_ex(ship, Vector3(2, 0, 0), Vector3(0, 1, 0), rotation, Vector3(1.4, 1.4, 1.4), WHITE)
        draw_model_ex(rupee, Vector3(-2, 0, 0), Vector3(0, 1, 0), rotation, Vector3(1.4, 1.4, 1.4), WHITE)
        end_mode_3d()
        end_drawing()

    close_window()
