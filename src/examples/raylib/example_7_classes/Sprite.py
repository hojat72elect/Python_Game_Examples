class Sprite:
    def __init__(self, pos, speed):
        self.pos = pos
        self.speed = speed

    def move(self, dt):
        self.pos.x += self.direction.x * self.speed * dt
        self.pos.y += self.direction.y * self.speed * dt
