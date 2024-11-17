import pygame
from pygame.locals import *
import random

pygame.init()

clock = pygame.time.Clock()
Fps = 60

screen_WIDTH = 864
screen_HEIGHT = 936

screen = pygame.display.set_mode((screen_WIDTH, screen_HEIGHT))
pygame.display.set_caption('Flappy Bird')

font = pygame.font.SysFont('Bauhaus 93', 60)

white = (255,255,255)

ground_scroll = 0
scroll_speed = 4
flying = False
game_Over = False
pipe_gap = 150
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
pass_pipe = False

bg = pygame.image.load('img/bg.png')
ground_img = pygame.image.load('img/ground.png')
button_img = pygame.image.load('img/restart.png')

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

def reset_game():
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(screen_HEIGHT / 2)
    score = 0
    return score