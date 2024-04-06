import pygame

pygame.init()
screen = pygame.display.set_mode((550, 550))
x = 25
y = 25
red, green, blue = 51, 0, 0
clock = pygame.time.Clock()

while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 20 if y > 25 else 0
        if pressed[pygame.K_DOWN]: y += 20 if y < 525 else 0
        if pressed[pygame.K_LEFT]: x -= 20 if x > 25 else 0
        if pressed[pygame.K_RIGHT]: x += 20 if x < 525 else 0
        
        screen.fill((255, 255, 255))
        if pressed[pygame.K_r] and red<51:
                red += 1
        if pressed[pygame.K_g] and green<51:
                green += 1
        if pressed[pygame.K_b] and blue<51:
                blue += 1 
        if pressed[pygame.K_1] and red > 0:
                red -= 1
        if pressed[pygame.K_2] and green > 0:
                green -= 1
        if pressed[pygame.K_3] and blue > 0:
                blue -= 1
        color = (red*5, green*5, blue*5)

        
        pygame.draw.circle(screen, color, (x, y), 25)
        
        pygame.display.flip()
        clock.tick(60)