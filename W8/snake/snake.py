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
        if pressed[pygame.K_UP]: 
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
            
        x += x_change
        y += y_change   
        
        snake_head = [x, y]
        if snake_head[0] == foodx and snake_head[1] == foody:
            if food_type < 7: snake_length += 1
            elif food_type < 10: snake_length += 2
            else: snake_length += 3
            foodx = round(random.randrange(0, 780) / 20.0) * 20.0
            
        for i in range(snake_length-1):
            if snake_parts[i] == snake_head: game_over = True
            
        if x >= 800 or x < 0 or y >= 800 or y < 0:
            game_over = True
            
        screen.fill((236,183,179))  #background
        for i in range(0, 800, 40):
            for j in range(0, 800, 40):
                pygame.draw.rect(screen, (251, 224, 217), [i, j, 20, 20])
        for i in range(20, 800, 40):
            for j in range(20, 800, 40):
                pygame.draw.rect(screen, (251, 224, 217), [i, j, 20, 20])
        
        
        snake_parts.append(snake_head)
        if(len(snake_parts) > snake_length):
            del snake_parts[0]
        for i in snake_parts:
            pygame.draw.rect(screen, (164, 184, 172), [i[0], i[1], 20, 20])
        
        screen.blit(pygame.image.load(food_dict[food_type]), (foodx, foody))
        
        s_count = font_1.render('Points:' + str(snake_length - 1), True, (142, 146, 155)) #number of the points displaces on the screen
        screen.blit(s_count,(700, 20))
    
    if game_over:
        screen.blit(pygame.image.load('W8\\snake\\button.png'), (100, 150))
        screen.blit(pygame.image.load('W8\\snake\\button.png'), (100, 400))
        s2 = font_2.render('Restart', True, (255, 255, 255))
        screen.blit(s2,(220, 180))  
        s2 = font_2.render('Quit', True, (255, 255, 255))
        screen.blit(s2,(280, 430)) 
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if 45 < pygame.mouse.get_pos()[0] < 255 and 305 < pygame.mouse.get_pos()[1] < 365:
                    crash = False
                    coins = 0                                       #coin count
                    collected = False                               #bool to check if the coin is collected
                    x_coin = random.randint(0, 225)                 #coin position
                    y_coin = -150
                    #characteristics of the moving car
                    x_car_1 = round(random.randrange(0, 225))       #position of the car is random
                    x_car_2 = round(random.randint(0,225))
                    y_car_1 = -120
                    y_car_2 = 800
                    car_col_1 = random.randint(1, 5)                #we pick the colour of the cars randomly
                    car_col_2 = random.randint(1, 5) 
                    speed_1 = random.randint(5, 10)                 #speed of the cars are also random
                    speed_2 = random.randint(5, 10)
                if 45 < pygame.mouse.get_pos()[0] < 255 and 405 < pygame.mouse.get_pos()[1] < 465:
                    pygame.quit()
                    exit()
            
    FPS.tick(10)
    pygame.display.update()