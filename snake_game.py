import pygame  # library for game
# import time # libraray for time
from pygame.locals import *

block_x, block_y = 100, 100
def draw_block():  # preparing Block as a snake body
    Screen.fill((102, 69, 8))  # rgb colour picker
    block = pygame.image.load('Resources/block.jpg')
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
                if event.key == K_UP:
                    block_y -= 10
                    draw_block()
                if event.key == K_DOWN:
                    block_y += 10
                    draw_block()
                if event.key == K_RIGHT:
                    block_x += 10
                    draw_block()
                if event.key == K_LEFT:
                    block_x -= 10
                    draw_block()
            elif event.type == QUIT:
                running = False
