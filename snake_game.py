import pygame  # library for game
# import time # libraray for time
from pygame.locals import *


def draw_block():  # preparing Block as a apple
    block_x, block_y = 100, 100
    block = pygame.image.load('Resources/apple.jpg')
    Screen.blit(block, (block_x, block_y))
    pygame.display.flip()  # display your screen


if __name__ == '__main__':
    pygame.init()  # to initialize the pygame library

    # preparing screen
    Screen = pygame.display.set_mode((500, 500))  # create a main window for a game
    Screen.fill((102, 69, 8))  # rgb colour picker
    draw_block()
    pygame.display.flip()

    # time.sleep(5)

    running = True
    while running:
        for event in pygame.event.get():  # event method will contains all the events either by keyboard or mouse
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_UP:
                    pass
                elif event.key == K_DOWN:
                    pass
                elif event.key == K_RIGHT:
                    pass
                # else event.key == K_LEFT:
                # pass
            elif event.type == QUIT:
                running = False
