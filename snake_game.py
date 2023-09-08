import pygame  # library for game
import time # library for time
from pygame.locals import *

class Game: # class
    def __init__(self): # Constructor
        pygame.init()  # To initialize the pygame library
        self.parent_screen = pygame.display.set_mode((500, 500))  # create a main window for a game
        self.snake = snake(self.parent_screen,7)
        self.snake.draw()

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

            self.snake.walk()
            time.sleep(.2)

class snake():
    def __init__(self,parent_screen,length):
        self.parent_screen= parent_screen
        self.block = pygame.image.load('Resources/block.jpg')
        self.length = length
        self.block_x, self.block_y = [40]*length, [40]*length
        self.direction = 'up'

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
            self.block_x[0] -= 40
        elif self.direction == 'right':
            self.block_x[0] += 40
        elif self.direction == 'up':
            self.block_y[0] -= 40
        elif self.direction == 'down':
            self.block_y[0] += 40

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


