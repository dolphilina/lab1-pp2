import pygame
from pygame.locals import * 
import random

pygame.init()

screen = pygame.display.set_mode((300, 800))    #width, height
pygame.display.set_caption("Races ୨୧")
FPS = pygame.time.Clock() 
font_1 = pygame.font.SysFont('Verdana', 20)   #font style
font_2 = pygame.font.SysFont('Verdana', 50)   
color = (0, 0, 0)
x, y = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
    