import pygame  # library for game
import time # library for time
from pygame.locals import *
import random

SIZE = 40

class Apple:
    def __init__(self,parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("Resources/apple.jpg")
        self.x = SIZE*3
        self.y = SIZE*3

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()  # display your screen

    def move(self):
        self.x = random.randint(1,12)*SIZE
        self.y = random.randint(1,12)*SIZE



class Game: # class
    def __init__(self): # Constructor
        pygame.init()  # To initialize the pygame library
        self.parent_screen = pygame.display.set_mode((500, 500))  # create a main window for a game
        self.snake = snake(self.parent_screen,2)
        self.snake.draw()
        self.apple = Apple(self.parent_screen)
        self.apple.draw()

    def display_score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"score:{self.snake.length}",True,(200, 200, 200))
        self.parent_screen.blit(score,(350,10))

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2  and x1 <= x2 + SIZE:
            if y1 >= y2 and y1 <= y2 + SIZE:
                return True
        return False

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        if(self.is_collision(self.snake.block_x[0],self.snake.block_y[0],self.apple.x,self.apple.y)):
            self.snake.increase_length()
            self.apple.move()


    def run(self):

        running = True
        while running:
            for event in pygame.event.get():  # event method will contains all the events either by keyboard or mouse
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                elif event.type == QUIT:
                    running = False

            self.play()
            time.sleep(.2)

class snake():
    def __init__(self,parent_screen,length):
        self.parent_screen= parent_screen
        self.block = pygame.image.load('Resources/block.jpg')
        self.length = length
        self.block_x, self.block_y = [SIZE]*length, [SIZE]*length
        self.direction = 'down'

    def increase_length(self):
        self.length += 1
        self.block_x.append(-1)
        self.block_y.append(-1)

    def draw(self):  # Preparing Block as a snake body

        self.parent_screen.fill((102, 69, 8))  # rgb colour picker
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.block_x[i], self.block_y[i]))
            pygame.display.flip()  # display your screen

    def walk(self):
        for i in range(self.length-1,0,-1):
            self.block_x[i] = self.block_x[i-1]
            self.block_y[i] = self.block_y[i-1]

        if self.direction == 'left':
            self.block_x[0] -= SIZE
        elif self.direction == 'right':
            self.block_x[0] += SIZE
        elif self.direction == 'up':
            self.block_y[0] -= SIZE
        elif self.direction == 'down':
            self.block_y[0] += SIZE

        self.draw()

    def move_up(self):

        self.direction = 'up'

    def move_down(self):

        self.direction = 'down'

    def move_right(self):
        self.direction = 'right'


    def move_left(self):
        self.direction = 'left'

if __name__ == '__main__':
    game = Game() # object of a game class
    game.run()

    # time.sleep(5)


