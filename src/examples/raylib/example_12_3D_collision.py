from pyray import get_mesh_bounding_box, check_collision_boxes, init_window, load_model_from_mesh, gen_mesh_cube, \
    window_should_close, is_key_down, begin_drawing, clear_background, begin_mode_3d, draw_grid, draw_model, \
    draw_bounding_box, get_frame_time, end_mode_3d, end_drawing, close_window, BoundingBox, Camera3D, Vector3, WHITE, RED, GRAY, GREEN

from raylib import Vector3Add, CAMERA_PERSPECTIVE, KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP


def get_bounding_box(model, pos):
    bounding_box = get_mesh_bounding_box(model.meshes[0])
    min_boundary = Vector3Add(pos, bounding_box.min)
    max_boundary = Vector3Add(pos, bounding_box.max)
    return BoundingBox(min_boundary, max_boundary)


def check_collision(axis):
    player_bbox = get_bounding_box(player, pos)
    boundary_bbox = get_bounding_box(obstacle, obstacle_pos)
    if check_collision_boxes(player_bbox, boundary_bbox):
        if axis == 'x':
            if direction.x > 0:
                pos.x = boundary_bbox.min.x - 0.5001
            if direction.x < 0:
                pos.x = boundary_bbox.max.x + 0.5001
        if axis == 'z':
            if direction.z > 0:
                pos.z = boundary_bbox.min.z - 0.5001
            if direction.z < 0:
                pos.z = boundary_bbox.max.z + 0.5001


init_window(1920, 1080, "3D collisions")
camera = Camera3D()
camera.position = Vector3(0.0, 5.0, 5.0)
camera.target = Vector3(0.0, 0.0, 0.0)
camera.up = Vector3(0.0, 1.0, 0.0)
camera.fovy = 45.0
camera.projection = CAMERA_PERSPECTIVE

player = load_model_from_mesh(gen_mesh_cube(1, 1, 1))
pos = Vector3()
direction = Vector3()
speed = 5
bbox = get_mesh_bounding_box(player.meshes[0])

obstacle = load_model_from_mesh(gen_mesh_cube(2, 1, 4))
obstacle_pos = Vector3(3, 0, 0)

while not window_should_close():
    # input
    direction.x = int(is_key_down(KEY_RIGHT)) - int(is_key_down(KEY_LEFT))
    direction.z = int(is_key_down(KEY_DOWN)) - int(is_key_down(KEY_UP))

    # movement & collision
    dt = get_frame_time()
    pos.x += direction.x * speed * dt
    check_collision('x')
    pos.z += direction.z * speed * dt
    check_collision('z')

    # collision check
    # print(check_collision_spheres(pos, 0.5, obstacle_pos, 2))
    # print(check_collision_box_sphere(get_bounding_box(player, pos), obstacle_pos, 2))
    # print(check_collision_boxes(get_bounding_box(player, pos),get_bounding_box(obstacle, obstacle_pos)))

    # drawing
    begin_drawing()
    clear_background(WHITE)
    begin_mode_3d(camera)
    draw_grid(10, 1)
    draw_model(player, pos, 1.0, RED)
    draw_model(obstacle, obstacle_pos, 1.0, GRAY)
    draw_bounding_box(get_bounding_box(player, pos), GREEN)
    end_mode_3d()
    end_drawing()
close_window()
