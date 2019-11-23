import random

class Snake:
    def __init__(self, length, speed, position_x, position_y):
        self.length = length
        self.speed = speed
        self.position_x = position_x
        self.position_y = position_y
		
		
    def draw_snake(self):
        return '#' * self.length


class Obstacle:
    def __init__(self, x, y):  # Metoda wywoływana zawsze gdy jest tworzony obiekt danej klasy
        self.x = x
        self.y = y

		
def draw_frame(snake, height, width):
	print('-'*width)

	for i in range(height):
		if i == snake.position_y:
			print(('|'+ ' '*snake.position_x + snake.draw_snake()+ ' '*(width-2 - snake.position_x - snake.length) + '|'))	
		else:
			print('|' + ' '*(width - 2) + '|')

	print('-'*width)


width = 200
height = 40
	
snake_1 = Snake(10, 5, int(width/2), int(height/2))
obstacle_1 = Obstacle(random.randint(1, 10), random.randint(1, 10))
print(snake_1.length)
print(obstacle_1.x)

draw_frame(snake_1, height, width)



