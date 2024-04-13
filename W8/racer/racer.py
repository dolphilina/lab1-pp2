import pygame
from pygame.locals import * 
import random

pygame.init()

screen = pygame.display.set_mode((300, 800))    #width, height
pygame.display.set_caption("Races ୨୧")
FPS = pygame.time.Clock() 
font_1 = pygame.font.SysFont('Verdana', 20)   #font style
font_2 = pygame.font.SysFont('Verdana', 50)   

#the place of the player, starts at the middle of the frame
x = 112
y = 680
crash = False                                   #check if car is crashed
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

#different car images
cars = {
    1 : 'W8\\racer\\files\\car1.png',
    2 : 'W8\\racer\\files\\car2.png',
    3 : 'W8\\racer\\files\\car3.png',
    4 : 'W8\\racer\\files\\car4.png',
    5 : 'W8\\racer\\files\\car5.png',
}


while True: 
    pressed = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        #leaving the game
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    #placing the background
    screen.blit(pygame.image.load('W8\\racer\\files\\bg.png'), (0, 0))
    
    if not crash:               #this part works if game is not over
        #place of the coin
        screen.blit(pygame.image.load('W8\\racer\\files\\coin.png'), (x_coin, y_coin))
        #place of the driving car
        screen.blit(pygame.image.load(cars[car_col_1]), (x_car_1, y_car_1))
        screen.blit(pygame.image.load(cars[car_col_2]), (x_car_2, y_car_2))
        #place of the player
        screen.blit(pygame.image.load('W8\\racer\\files\\player.png'), (x, y))
        #number of the coins 
        s1 = font_1.render('Coins: ' + str(coins), True, (255, 255, 255))
        screen.blit(s1,(200, 10))
        screen.blit(pygame.image.load('W8\\racer\\files\\coin_count.png'), (175, 12))
        
        #moving the player   
        if pressed[pygame.K_LEFT]: x -= 5 if x > 0 else 0
        if pressed[pygame.K_RIGHT]: x += 5 if x < 225 else 0  
            
        #the position of the cars & coins and its affection
        if y_car_1 == 600 or y_car_1 == 601:        #if the car reaches the position, another car will start moving
            y_car_2 = -120
            x_car_2 = random.randint(0,225)
            car_col_2 = random.randint(1, 5)
            speed_2 = random.randint(5, 10)
        if y_car_2 == 600 or y_car_2 == 601: 
            y_car_1 = -120
            x_car_1 = random.randint(0,225)
            car_col_1 = random.randint(1, 5)
            speed_1 = random.randint(5, 10)
            
        if y_car_1 <=810: y_car_1 += speed_1        #car won't move belong the screen
        if y_car_2 <=810: y_car_2 += speed_2
        
        if y_coin <= 800: y_coin += 5               #pos of the coin
        if y_coin > 800 or collected: 
            y_coin = -150
            x_coin = random.randint(0,225)
            collected = False
        
        if 750 > y_coin >= y-70:                          #counting the coins
            if x-75 <= x_coin <= x+75:
                coins += 1
                collected = True
                
        if 750 >= y_car_1 >= y-116:                  #crashes
            if x-75 <= x_car_1 <= x+75:
                crash = True
        if 750 >= y_car_2 >= y-116:                  
            if x-75 <= x_car_2 <= x+75:
                crash = True
    
    if crash:
        screen.blit(pygame.image.load('W8\\racer\\files\\button.png'), (45, 305))
        screen.blit(pygame.image.load('W8\\racer\\files\\button.png'), (45, 405))
        s2 = font_2.render('Restart', True, (255, 255, 255))
        screen.blit(s2,(60, 300))  
        s3 = font_2.render('Quit', True, (255, 255, 255))
        screen.blit(s3,(98, 400))   
        
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
                    
            
    FPS.tick(60)
    pygame.display.update()