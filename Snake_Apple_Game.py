import pygame
from pygame.locals import *
import time
import random

size = 40


class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.apple_image = pygame.image.load("Resources/apple.jpg").convert()
        self.x = size * 3
        self.y = size * 3

    def draw_apple(self):
        self.parent_screen.blit(self.apple_image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 24) * size
        self.y = random.randint(1, 14) * size


class snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.snake_body = pygame.image.load("Resources/block.jpg").convert()
        self.length = length
        self.x = [size] * length
        self.y = [size] * length
        self.direction = 'Down'

    def move_left(self):
        self.direction = 'Left'

    def move_right(self):
        self.direction = 'Right'

    def move_up(self):
        self.direction = 'Up'

    def move_down(self):
        self.direction = 'Down'

    def snake_walk(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'Down':
            self.y[0] += size
        elif self.direction == 'Up':
            self.y[0] -= size
        elif self.direction == 'Right':
            self.x[0] += size
        elif self.direction == 'Left':
            self.x[0] -= size

        self.draw_snake()

    def draw_snake(self):
        self.parent_screen.fill((52, 235, 195))
        for i in range(self.length):
            self.parent_screen.blit(self.snake_body, (self.x[i], self.y[i]))
        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.play_background_music()
        self.screen = pygame.display.set_mode((1000, 600), pygame.RESIZABLE)
        pygame.display.set_caption("Snake Apple Game 2")
        self.snake = snake(self.screen, 1)
        self.snake.draw_snake()
        self.apple = Apple(self.screen)
        self.apple.draw_apple()

    def play_background_music(self):
        pygame.mixer.music.load('Resources/backgroundSound.mp3')
        pygame.mixer.music.play(-1, 0)

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + size:
            if y1 >= y2 and y1 < y2 + size:
                return True
        return False

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"SCORE : {self.snake.length}", True, (250, 250, 250))
        self.screen.blit(score, (850, 10))

    def show_game_over(self):
        self.screen.fill((52, 235, 195), )
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game is over! Your score is {self.snake.length}", True, (255, 255, 255))
        self.screen.blit(line1, (200, 300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.screen.blit(line2, (200, 350))
        pygame.mixer.music.pause()
        pygame.display.flip()

    def game_reset(self):
        self.snake = snake(self.screen, 1)
        self.apple = Apple(self.screen)

    def play_sound(self, sound):
        if sound == "crash":
            sound = pygame.mixer.Sound("Resources/crash.mp3")
        elif sound == "eat":
            sound = pygame.mixer.Sound("Resources/eat.mp3")
        pygame.mixer.Sound.play(sound)

    def play(self):
        self.snake.snake_walk()
        self.apple.draw_apple()
        self.display_score()
        pygame.display.flip()

        # snake eating apple scenario
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.play_sound("eat")
            self.snake.increase_length()
            self.apple.move()

        # # snake colliding with itself
        for i in range(1, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound("crash")
                raise "Game Over!!"

        # snake colliding with the boundaries of the window
        if not (0 <= self.snake.x[0] <= 1000 and 0 <= self.snake.y[0] <= 600):
            self.play_sound('crash')
            raise "Hit the boundary error"

    def run(self):
        screen_run = True
        game_pause = False

        while screen_run:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        screen_run = False
                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        game_pause = False
                    if not game_pause:
                        if event.key == K_UP:
                            self.snake.move_up()
                        if event.key == K_DOWN:
                            self.snake.move_down()
                        if event.key == K_LEFT:
                            self.snake.move_left()
                        if event.key == K_RIGHT:
                            self.snake.move_right()

                elif event.type == QUIT:
                    screen_run = False
            try:
                if not game_pause:
                    self.play()

            except Exception as e:
                self.show_game_over()
                game_pause = True
                self.game_reset()

            time.sleep(.25)


if __name__ == '__main__':
    game = Game()
    game.run()
