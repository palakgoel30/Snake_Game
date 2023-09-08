import pygame  # library for game
# import time # library for time
from pygame.locals import *

class Game: # class
    def __init__(self): # Constructor
        pygame.init()  # To initialize the pygame library
        self.parent_screen = pygame.display.set_mode((500, 500))  # create a main window for a game
        self.snake = snake(self.parent_screen)
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

class snake():
    def __init__(self,parent_screen):
        self.parent_screen= parent_screen
        self.block = pygame.image.load('Resources/block.jpg')
        self.block_x, self.block_y = 100, 100

    def draw(self):  # Preparing Block as a snake body

        self.parent_screen.fill((102, 69, 8))  # rgb colour picker
        self.parent_screen.blit(self.block, (self.block_x, self.block_y))
        pygame.display.flip()  # display your screen

    def move_up(self):

        self.block_y -= 10
        self.draw()

    def move_down(self):

        self.block_y += 10
        self.draw()

    def move_right(self):
        self.block_x +=10
        self.draw()


    def move_left(self):
        self.block_x -= 10
        self.draw()

if __name__ == '__main__':
    game = Game() # object of a game class
    game.run()

    # time.sleep(5)


