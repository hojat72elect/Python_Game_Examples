from pyray import get_mesh_bounding_box, check_collision_boxes, init_window, load_model_from_mesh, gen_mesh_cube, \
    window_should_close, is_key_down, begin_drawing, clear_background, begin_mode_3d, draw_grid, draw_model, \
    draw_bounding_box, get_frame_time, end_mode_3d, end_drawing, close_window, BoundingBox, Camera3D, Vector3, WHITE, \
    RED, GRAY, GREEN
from raylib import Vector3Add, CAMERA_PERSPECTIVE, KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP

if __name__ == '__main__':

    # Set up window
    init_window(1920, 1080, "Example 12 - 3D collisions - Raylib")

    #Set up camera
    camera = Camera3D()
    camera.position = Vector3(0.0, 5.0, 5.0)
    camera.target = Vector3(0.0, 0.0, 0.0)
    camera.up = Vector3(0.0, 1.0, 0.0)
    camera.fovy = 45.0
    camera.projection = CAMERA_PERSPECTIVE

    # Set up the player properties
    player_model = load_model_from_mesh(gen_mesh_cube(1, 1, 1))
    player_position = Vector3()
    player_direction = Vector3()
    player_speed = 5
    player_bounding_box = get_mesh_bounding_box(player_model.meshes[0])

    # Set up the obstacle properties
    obstacle_model = load_model_from_mesh(gen_mesh_cube(2, 1, 4))
    obstacle_position = Vector3(3, 0, 0)

    while not window_should_close():

        # Read keyboard inputs
        player_direction.x = int(is_key_down(KEY_RIGHT)) - int(is_key_down(KEY_LEFT))
        player_direction.z = int(is_key_down(KEY_DOWN)) - int(is_key_down(KEY_UP))

        delta_time = get_frame_time()
        player_position.x += player_direction.x * (player_speed * delta_time)

        player_bounding_box = get_mesh_bounding_box(player_model.meshes[0])
        min_boundary1_x = Vector3Add(player_position, player_bounding_box.min)
        max_boundary1_x = Vector3Add(player_position, player_bounding_box.max)
        player_bbox_x = BoundingBox(min_boundary1_x, max_boundary1_x)

        # second usage of function
        bounding_box2_x = get_mesh_bounding_box(obstacle_model.meshes[0])
        min_boundary2_x = Vector3Add(obstacle_position, bounding_box2_x.min)
        max_boundary2_x = Vector3Add(obstacle_position, bounding_box2_x.max)
        boundary_bbox_x = BoundingBox(min_boundary2_x, max_boundary2_x)

        if check_collision_boxes(player_bbox_x, boundary_bbox_x):
            if player_direction.x > 0:
                player_position.x = boundary_bbox_x.min.x - 0.5001
            if player_direction.x < 0:
                player_position.x = boundary_bbox_x.max.x + 0.5001

        player_position.z += player_direction.z * player_speed * delta_time
        # first usage of function.
        player_bounding_box = get_mesh_bounding_box(player_model.meshes[0])
        min_boundary1_z = Vector3Add(player_position, player_bounding_box.min)
        max_boundary1_z = Vector3Add(player_position, player_bounding_box.max)
        player_bbox_z = BoundingBox(min_boundary1_z, max_boundary1_z)

        # second usage of function
        bounding_box2_z = get_mesh_bounding_box(obstacle_model.meshes[0])
        min_boundary2_z = Vector3Add(obstacle_position, bounding_box2_z.min)
        max_boundary2_z = Vector3Add(obstacle_position, bounding_box2_z.max)
        boundary_bbox_z = BoundingBox(min_boundary2_z, max_boundary2_z)

        if check_collision_boxes(player_bbox_z, boundary_bbox_z):
            if player_direction.z > 0:
                player_position.z = boundary_bbox_z.min.z - 0.5001
            if player_direction.z < 0:
                player_position.z = boundary_bbox_z.max.z + 0.5001

        # drawing
        begin_drawing()
        clear_background(WHITE)
        begin_mode_3d(camera)
        draw_grid(10, 1)
        draw_model(player_model, player_position, 1.0, RED)
        draw_model(obstacle_model, obstacle_position, 1.0, GRAY)
        player_bounding_box = get_mesh_bounding_box(player_model.meshes[0])
        min_boundary = Vector3Add(player_position, player_bounding_box.min)
        max_boundary = Vector3Add(player_position, player_bounding_box.max)
        resulting_bounding_box = BoundingBox(min_boundary, max_boundary)
        draw_bounding_box(resulting_bounding_box, GREEN)
        end_mode_3d()
        end_drawing()

    close_window()
