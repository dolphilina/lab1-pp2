import pygame
from pygame.locals import * 
import random

pygame.init()

screen = pygame.display.set_mode((1000, 800))    #width, height
pygame.display.set_caption("Paint ୨୧")
FPS = pygame.time.Clock() 
font_1 = pygame.font.SysFont('Verdana', 20)     #font style
font_2 = pygame.font.SysFont('Verdana', 50)   
red, green, blue = 0, 0, 0
x, y = 0, 0
draw = True
erase = False
d = 10                                          #размер кисти

screen.fill((255, 255, 255))
pygame.draw.rect(screen, (0, 0, 0), [600, 0, 5, 800])

while True:
    pressed = pygame.key.get_pressed()
    
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]
                    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if draw == True: draw = False
                    else:
                        draw = True
                        erase = False
                if event.button == 3:
                    if erase == True: erase = False
                    else: 
                        erase = True
                        draw = False
    if pressed[pygame.K_r] and red < 51:
                red += 1
    if pressed[pygame.K_g] and green < 51:
                green += 1
    if pressed[pygame.K_b] and blue < 51:
                blue += 1 
    if pressed[pygame.K_1] and red > 0:
                red -= 1
    if pressed[pygame.K_2] and green > 0:
                green -= 1
    if pressed[pygame.K_3] and blue > 0:
                blue -= 1
    color = (red*5, green*5, blue*5)

    if draw == True:
        pygame.draw.circle(screen, color, (x, y), d)
    if erase == True:
        pygame.draw.circle(screen, (255, 255, 255), (x, y), d)
    
    pygame.display.flip()
    FPS.tick(240)