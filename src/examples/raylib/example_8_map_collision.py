from raylib import KEY_RIGHT, KEY_DOWN, KEY_LEFT, KEY_UP
from pyray import check_collision_recs, init_window, Rectangle, Vector2, window_should_close, is_key_down, \
    get_frame_time, begin_drawing, clear_background, draw_rectangle_rec, BLACK, GRAY, RED, end_drawing, close_window

def collision_check(axis: str, collision_map: list[Rectangle], player_collider: Rectangle, player_direction: Vector2):
    """
    Checks the collision between the map and the player's collider. Will limit the player inside the map.
    """
    for block in collision_map:
        if check_collision_recs(block, player_collider):
            if axis == 'x':
                if player_direction.x > 0:  # moving right
                    player_collider.x = block.x - player_collider.width
                if player_direction.x < 0:  # moving left
                    player_collider.x = block.x + block.width
            else:
                if player_direction.y < 0:  # moving up
                    player_collider.y = block.y + block.height
                if player_direction.y > 0:  # moving down
                    player_collider.y = block.y - player_collider.height

if __name__ == '__main__':
    init_window(1920, 1080, "Example 8 - Big Map Collision Detection")

    '''
    This list defines the map of the game, it works fine but honestly, I would say it's so 
    much better to use a Tiled app for these situations.
    '''
    level_map: list[str] = [
        '1111111111111111111',
        '1010000000000000001',
        '1010000000001111111',
        '1000000000000000111',
        '1000000200000000011',
        '1000000000000100001',
        '1000000000000100001',
        '1001100000000100001',
        '1001100000000100001',
        '1001100000000100001',
        '1111111111111111111'
    ]

    player = Rectangle(400, 300, 60, 60)
    player_speed = 300
    direction = Vector2()

    # Create the collision map out of the predefined list of data
    blocks: list[Rectangle] = []
    block_size = 100
    for row_index, row in enumerate(level_map):
        for col_index, cell in enumerate(row):
            if cell == '1':
                x = col_index * block_size
                y = row_index * block_size
                current_block = Rectangle(x, y, block_size, block_size)
                blocks.append(current_block)

    while not window_should_close():
        direction.x = int(is_key_down(KEY_RIGHT)) - int(is_key_down(KEY_LEFT))
        direction.y = int(is_key_down(KEY_DOWN)) - int(is_key_down(KEY_UP))

        # movement
        dt = get_frame_time()
        player.x += direction.x * player_speed * dt
        collision_check('x', blocks, player, direction)
        player.y += direction.y * player_speed * dt
        collision_check('y', blocks, player, direction)

        begin_drawing()
        clear_background(BLACK)
        for _block in blocks:
            draw_rectangle_rec(_block, GRAY)
        draw_rectangle_rec(player, RED)
        end_drawing()

    close_window()
