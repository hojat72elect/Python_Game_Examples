from pyray import get_mesh_bounding_box, check_collision_boxes, init_window, load_model_from_mesh, gen_mesh_cube, \
    window_should_close, is_key_down, begin_drawing, clear_background, begin_mode_3d, draw_grid, draw_model, \
    draw_bounding_box, get_frame_time, end_mode_3d, end_drawing, close_window, BoundingBox, Camera3D, Vector3, WHITE, \
    RED, GRAY, GREEN
from raylib import Vector3Add, CAMERA_PERSPECTIVE, KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP

if __name__ == '__main__':

    init_window(1920, 1080, "Example 12 - 3D collisions - Raylib")
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
        # first usage of function.
        bounding_box1_x = get_mesh_bounding_box(player.meshes[0])
        min_boundary1_x = Vector3Add(pos, bounding_box1_x.min)
        max_boundary1_x = Vector3Add(pos, bounding_box1_x.max)
        player_bbox_x = BoundingBox(min_boundary1_x, max_boundary1_x)

        # second usage of function
        bounding_box2_x = get_mesh_bounding_box(obstacle.meshes[0])
        min_boundary2_x = Vector3Add(obstacle_pos, bounding_box2_x.min)
        max_boundary2_x = Vector3Add(obstacle_pos, bounding_box2_x.max)
        boundary_bbox_x = BoundingBox(min_boundary2_x, max_boundary2_x)

        if check_collision_boxes(player_bbox_x, boundary_bbox_x):
            if direction.x > 0:
                pos.x = boundary_bbox_x.min.x - 0.5001
            if direction.x < 0:
                pos.x = boundary_bbox_x.max.x + 0.5001

        pos.z += direction.z * speed * dt
        # first usage of function.
        bounding_box1_z = get_mesh_bounding_box(player.meshes[0])
        min_boundary1_z = Vector3Add(pos, bounding_box1_z.min)
        max_boundary1_z = Vector3Add(pos, bounding_box1_z.max)
        player_bbox_z = BoundingBox(min_boundary1_z, max_boundary1_z)

        # second usage of function
        bounding_box2_z = get_mesh_bounding_box(obstacle.meshes[0])
        min_boundary2_z = Vector3Add(obstacle_pos, bounding_box2_z.min)
        max_boundary2_z = Vector3Add(obstacle_pos, bounding_box2_z.max)
        boundary_bbox_z = BoundingBox(min_boundary2_z, max_boundary2_z)

        if check_collision_boxes(player_bbox_z, boundary_bbox_z):
            if direction.z > 0:
                pos.z = boundary_bbox_z.min.z - 0.5001
            if direction.z < 0:
                pos.z = boundary_bbox_z.max.z + 0.5001

        # drawing
        begin_drawing()
        clear_background(WHITE)
        begin_mode_3d(camera)
        draw_grid(10, 1)
        draw_model(player, pos, 1.0, RED)
        draw_model(obstacle, obstacle_pos, 1.0, GRAY)
        bounding_box = get_mesh_bounding_box(player.meshes[0])
        min_boundary = Vector3Add(pos, bounding_box.min)
        max_boundary = Vector3Add(pos, bounding_box.max)
        resulting_bounding_box = BoundingBox(min_boundary, max_boundary)
        draw_bounding_box(resulting_bounding_box, GREEN)
        end_mode_3d()
        end_drawing()

    close_window()
