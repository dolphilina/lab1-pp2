import pygame

pygame.init()
screen = pygame.display.set_mode((550, 550))
x = 25
y = 25
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
        color = ("red")

        
        pygame.draw.circle(screen, color, (x, y), 25)
        
        pygame.display.flip()
        clock.tick(60)