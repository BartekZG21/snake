import random
import time


class Snake:
    def __init__(self, length, speed, position_x, position_y):
        self.length = length
        self.speed = speed
        self.position_x = position_x
        self.position_y = position_y
        self.is_alive = True

    def draw_snake(self):
        return '#' * self.length

    def move(self):
        snake_1.position_x = snake_1.position_x + self.speed

    def check_position(self, frame):
        if self.position_x + self.length >= frame.width:
            self.is_alive = False


class Frame:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self, snake):
        if snake.is_alive:
            print('-' * self.width)

            for i in range(self.height):
                if i == snake.position_y:
                    print(('|' + ' ' * snake.position_x + snake.draw_snake() + ' ' * (
                                self.width - 2 - snake.position_x - snake.length) + '|'))
                else:
                    print('|' + ' ' * (self.width - 2) + '|')

            print('-' * self.width)
        else:
            print('-' * self.width)

            for i in range(self.height):
                if i == int(self.width/2):
                    print('|' + ' ' * (self.width/2 - 4) + "GAME OVER" + + ' ' * (self.width/2 - 5) + '|')
                else:
                    print('|' + ' ' * (self.width - 2) + '|')

            print('-' * self.width)

class Obstacle:
    def __init__(self, x, y):  # Metoda wywoływana zawsze gdy jest tworzony obiekt danej klasy
        self.x = x
        self.y = y


frame = Frame(width=200, height=40)
snake_1 = Snake(10, 10, int(frame.width/2), int(frame.height/2))
obstacle_1 = Obstacle(random.randint(1, 10), random.randint(1, 10))
print(snake_1.length)
print(obstacle_1.x)

while snake_1.is_alive:
    frame.draw(snake_1)
    snake_1.move()
    snake_1.check_position(frame)
    time.sleep(1)

frame.draw(snake_1)


