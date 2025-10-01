from pyray import init_window, gen_mesh_cube, load_model_from_mesh, gen_mesh_cylinder, gen_image_gradient_linear, \
    load_texture_from_image, set_material_texture, window_should_close, close_window, get_frame_time, matrix_rotate_x, \
    clear_background, begin_drawing, begin_mode_3d, draw_grid, draw_model, draw_line_3d, end_mode_3d, end_drawing, \
    Camera3D, Vector3, RED, YELLOW, WHITE, BLACK

from raylib import CAMERA_PERSPECTIVE, MATERIAL_MAP_ALBEDO

if __name__ == '__main__':

    init_window(1920, 1080, "3D base")

    # 3D enabled camera
    camera = Camera3D()
    camera.position = Vector3(0, 5.0, 5.0)
    camera.target = Vector3()
    camera.up = Vector3(0, 1, 0)
    camera.fovy = 45.0
    camera.projection = CAMERA_PERSPECTIVE

    # Create a cube mesh and make a 3D model out of it.
    cube_mesh = gen_mesh_cube(1, 1, 1)
    cube_model = load_model_from_mesh(cube_mesh)

    # Create a cylinder mesh and make a 3D model out of it.
    cylinder_mesh = gen_mesh_cylinder(1, 2, 20)
    cylinder_model = load_model_from_mesh(cylinder_mesh)

    # Create an Image, extract a texture out of it, and apply that texture as the surface material of the model
    image = gen_image_gradient_linear(20, 20, 1, RED, YELLOW)
    texture = load_texture_from_image(image)
    set_material_texture(cylinder_model.materials[0], MATERIAL_MAP_ALBEDO, texture)

    # position and angle of the model in our world.
    model_position = Vector3()
    model_rotation = 0

    while not window_should_close():

        dt = get_frame_time()
        model_rotation += 4 * dt
        cylinder_model.transform = matrix_rotate_x(model_rotation)

        clear_background(WHITE)
        begin_drawing()

        begin_mode_3d(camera)
        draw_grid(10, 0.5)
        draw_model(cylinder_model, model_position, 1, WHITE)
        draw_line_3d(Vector3(-4, 0, -2), Vector3(5, 2, 3), BLACK)
        end_mode_3d()

        end_drawing()

    close_window()
