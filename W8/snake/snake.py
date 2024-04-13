import pygame
from pygame.locals import *
import time
import random

pygame.init()

screen = pygame.display.set_mode((800, 800))    #the game is 800*800
pygame.display.set_caption("Snake game ୨୧")     #title
FPS = pygame.time.Clock()                       
game_over = False                               #game will stop if it turns True

font_1 = pygame.font.SysFont('Verdana', 20)     #font style
font_2 = pygame.font.SysFont('Verdana', 100) 

snake_length = 1                                
x = 300                                         #coordinates snake starts moving from
y = 300
x_change = 0
y_change = 0

foodx = round(random.randrange(0, 780) / 20.0) * 20.0   #randomizing the food position and value
foody = round(random.randrange(0, 780) / 20.0) * 20.0
food_type = random.randint(1, 10)

food_dict = {1: 'W8\\snake\\1p.png',        #food pics
             2: 'W8\\snake\\1p.png', 
             3: 'W8\\snake\\1p.png', 
             4: 'W8\\snake\\1p.png', 
             5: 'W8\\snake\\1p.png', 
             6: 'W8\\snake\\1p.png', 
             7: 'W8\\snake\\2p.png',
             8: 'W8\\snake\\2p.png',
             9: 'W8\\snake\\2p.png',
             10: 'W8\\snake\\3p.png',
             }

snake_parts = []                                        #coordinates of each part of the snake


while True:
    if not game_over:

        pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                game_over = True
        if pressed[pygame.K_UP]:                #changing direction
            y_change = -20 
            x_change = 0
        if pressed[pygame.K_DOWN]: 
            y_change = 20
            x_change = 0 
        if pressed[pygame.K_LEFT]: 
            x_change = -20 
            y_change = 0
        if pressed[pygame.K_RIGHT]: 
            x_change = 20 
            y_change = 0

        x += x_change                           #changing the pos according to the direction
        y += y_change   

        snake_head = [x, y]                     #pos of the snake head
        if snake_head[0] == foodx and snake_head[1] == foody:   #eating
            if food_type < 7: snake_length += 1
            elif food_type < 10: snake_length += 2
            else: snake_length += 3
            foodx = round(random.randrange(0, 780) / 20.0) * 20.0   #respawning the food
            foody = round(random.randrange(0, 780) / 20.0) * 20.0

        for i in range(snake_length-1):                             #we can't move on ourselfes
            if snake_parts[i] == snake_head: game_over = True

        if x > 800 or x < -10 or y > 800 or y < -10:                  #we can't move belong the screen
            game_over = True

        screen.fill((236,183,179))  #background and net on the bg
        for i in range(0, 800, 40):
            for j in range(0, 800, 40):
                pygame.draw.rect(screen, (251, 224, 217), [i, j, 20, 20])
        for i in range(20, 800, 40):
            for j in range(20, 800, 40):
                pygame.draw.rect(screen, (251, 224, 217), [i, j, 20, 20])


        snake_parts.append(snake_head)                              #add heat to the snake list
        if(len(snake_parts) > snake_length):                        #remove the last element
            del snake_parts[0]
        for i in snake_parts:                                       #draw the snake
            pygame.draw.rect(screen, (164, 184, 172), [i[0], i[1], 20, 20])

        screen.blit(pygame.image.load(food_dict[food_type]), (foodx, foody))                #draw the food

        s_count = font_1.render('Points:' + str(snake_length - 1), True, (142, 146, 155)) #number of the points displaces on the screen
        screen.blit(s_count,(700, 20))

    if game_over:
        screen.blit(pygame.image.load('W8\\snake\\button.png'), (100, 150))
        screen.blit(pygame.image.load('W8\\snake\\button.png'), (100, 400))
        s2 = font_2.render('Restart', True, (255, 255, 255))
        screen.blit(s2,(220, 180))  
        s2 = font_2.render('Quit', True, (255, 255, 255))
        screen.blit(s2,(280, 430)) 

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 100 < pygame.mouse.get_pos()[0] < 500 and 150 < pygame.mouse.get_pos()[1] < 350:     #reset of the game
                        game_over = False
                        snake_length = 1                                
                        x = 300                                        
                        y = 300
                        x_change = 0
                        y_change = 0
                        foodx = round(random.randrange(0, 780) / 20.0) * 20.0   
                        foody = round(random.randrange(0, 780) / 20.0) * 20.0
                        food_type = random.randint(1, 10)
                    if 100 < pygame.mouse.get_pos()[0] < 500 and 400 < pygame.mouse.get_pos()[1] < 600:     #quit
                        pygame.quit()
                        exit()

    FPS.tick(10 + snake_length * 0.2)           #the snake is moving faster as you eat
    pygame.display.update()