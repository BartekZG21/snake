import random
import time


class Snake:
    def __init__(self, length, speed, position_x, position_y):
        self.length = length
        self.speed = speed
        self.position_x = position_x
        self.position_y = position_y
        self.is_alive = True
        self.previous_action = " "

    def draw_snake(self):
        return '#' * self.length

    def move(self, action):
        if not self.previous_action == 'left' and action == 'right':
            snake_1.position_x = snake_1.position_x + 1
        if action == 'up':
            snake_1.position_y = snake_1.position_y + 1
        if action == 'left':
            snake_1.position_x = snake_1.position_x - 1
        if action == 'down':
            snake_1.position_y = snake_1.position_y - 1

        self.previous_action = action



    def check_position(self, frame):
        if self.position_x >= frame.width - 1:
            self.position_x = self.position_x - 1
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
                    print(('|' + ' ' * (snake.position_x - snake.length) + snake.draw_snake() + ' ' * (
                                self.width - 2 - snake.position_x) + '|'))
                else:
                    print('|' + ' ' * (self.width - 2) + '|')

            print('-' * self.width)
        else:
            print('-' * self.width)

            for i in range(self.height):
                if i == snake.position_y:
                    if i != int(self.height / 2):
                        print(('|' + ' ' * int(snake.position_x - snake.length) + snake.draw_snake() + ' ' * int(
                            self.width - 2 - snake.position_x) + '|'))
                    if i == int(self.height / 2):
                        print('|' + ' ' * int(self.width / 2 - 4) + 'GAME OVER' + ' ' * int(self.width / 2 - snake.length - 7) +
                              snake.draw_snake() + '|')
                elif i == int(self.height / 2):
                    print('|' + ' ' * int(self.width / 2 - 4) + "GAME OVER" + ' ' * int(self.width / 2 - 7) + '|')
                else:
                    print('|' + ' ' * (self.width - 2) + '|')

            print('-' * self.width)

class Obstacle:
    def __init__(self, x, y):  # Metoda wywoływana zawsze gdy jest tworzony obiekt danej klasy
        self.x = x
        self.y = y


frame = Frame(width=200, height=40)
snake_1 = Snake(15, 30, int(frame.width/2 + 10), int(frame.height/4))
obstacle_1 = Obstacle(random.randint(1, 10), random.randint(1, 10))
print(snake_1.length)
print(obstacle_1.x)

while snake_1.is_alive:
    frame.draw(snake_1)
    # wykrywanie jaki przycisk zostal wcisniety
    action = 'right'
    snake_1.move(action)
    snake_1.check_position(frame)
    time.sleep(1/snake_1.speed)
    # time.sleep(-snake_1.speed + 10)
    # x 1 2 3
    # y 6 3 0

frame.draw(snake_1)


