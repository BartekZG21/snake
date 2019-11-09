import random

class Snake:
    def __init__(self, length, speed):
        self.length = length
        self.speed = speed


class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y


snake_1 = Snake(10, 5)
obstacle_1 = Obstacle(random.randint(1, 10), random.randint(1, 10))
print(snake_1.length)
print(obstacle_1.x)
