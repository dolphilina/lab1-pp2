import pygame

pygame.init()


screen = pygame.display.set_mode((1000, 800))    #width, height
pygame.display.set_caption("Paint ୨୧")
FPS = pygame.time.Clock() 
font_1 = pygame.font.SysFont('Verdana', 10)     #font style
font_2 = pygame.font.SysFont('Verdana', 20)   
red, green, blue = 0, 0, 0                      #size of erery color at the finish colour
x, y = 0, 0
draw = False                                    #bool func to check if the button is pressed
erase = False
square = False
circle = True
rect = False
rhomb = False
et = False
rt = False
d = 10                                          #brush size


screen.fill((255, 255, 255))


s1 = font_1.render('Add more red, green or blue to', True, (0, 0, 0))   #text
s2 = font_1.render('the color by pressing R, G, B.', True, (0, 0, 0))
s3 = font_1.render('Reduce them by pressing 1, 2, 3.', True, (0, 0, 0))
s4 = font_1.render('Start/end drawing - left mouse.', True, (0, 0, 0))
s5 = font_1.render('Start/end eracing - right mouse.', True, (0, 0, 0))
s13 = font_1.render('Larger/smaller - 4/5', True, (0, 0, 0))
s6 = font_2.render('Colors', True, (0, 0, 0))
s7 = font_2.render('Shapes', True, (0, 0, 0))
s8 = font_2.render('Size', True, (0, 0, 0))
s9 = font_2.render('5', True, (255, 255, 255))
s10 = font_2.render('10', True, (255, 255, 255))
s11 = font_2.render('20', True, (255, 255, 255))
s12 = font_2.render('50', True, (255, 255, 255))

while True:
    pressed = pygame.key.get_pressed()
    
    x = pygame.mouse.get_pos()[0]       #getting the pos of the mouse to draw on it
    y = pygame.mouse.get_pos()[1]
    
    if x > 815:                         #no drawing if we're to far bellow the border
        draw, erase = False, False
                    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                    exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if x < 800:                         #clicking on the mouse to start/stop drawing
                    if draw: draw = False
                    else:
                        draw = True
                        erase = False
                elif 810 < x < 890 and 300 < y < 380:       #shape buttons
                    square = True
                    circle = False  #square
                    rect = False
                    rhomb = False
                    et = False
                    rt = False
                elif 910 < x < 990 and 300 < y < 380:
                    circle = True
                    square = False  #circle
                    rect = False
                    rhomb = False
                    et = False
                    rt = False
                elif 810 < x < 890 and 420 < y < 480:
                    rect = True
                    circle = False  #rectangle
                    square = False
                    rhomb = False
                    et = False
                    rt = False
                elif 910 < x < 990 and 420 < y < 480:
                    rhomb = True
                    rect = False
                    circle = False  #rhombus
                    square = False
                    et = False
                    rt = False
                elif 810 < x < 890 and 510 < y < 590:
                    et = True
                    rect = False
                    circle = False  #equivalent triangle
                    square = False
                    rhomb = False
                    rt = False
                elif 910 < x < 990 and 510 < y < 590:
                    rt = True
                    rect = False
                    circle = False  #right triangle
                    square = False
                    rhomb = False
                elif 810 < x < 860 and 10 < y < 60:         #color buttons
                        red, green, blue = 255, 0, 0
                elif 875 < x < 925 and 10 < y < 60:
                        red, green, blue = 0, 255, 0
                elif 940 < x < 990 and 10 < y < 60:
                        red, green, blue = 0, 0, 255
                elif 810 < x < 860 and 70 < y < 120:
                        red, green, blue = 255, 255, 0
                elif 875 < x < 925 and 70 < y < 120:
                        red, green, blue = 0, 255, 255
                elif 940 < x < 990 and 70 < y < 120:
                        red, green, blue = 255, 0, 255
                elif 805 < x < 845 and 200 < y < 240: d = 5     #size buttons
                elif 855 < x < 895 and 200 < y < 240: d = 10
                elif 905 < x < 945 and 200 < y < 240: d = 20
                elif 955 < x < 995 and 200 < y < 240: d = 50
            elif event.button == 3:
                if x < 800:                         #clicking on the right mouse to start/stop erasing
                    if erase: erase = False
                    else:
                        erase = True
                        draw = False
    
    if pressed[pygame.K_r] and red < 255:       #keyboard color buttons
        red += 1
    if pressed[pygame.K_g] and green < 255:
        green += 1
    if pressed[pygame.K_b] and blue < 255:
        blue += 1 
    if pressed[pygame.K_1] and red > 0:
        red -= 1
    if pressed[pygame.K_2] and green > 0:
        green -= 1
    if pressed[pygame.K_3] and blue > 0:
        blue -= 1
    color = (red, green, blue)
    
    if pressed[pygame.K_4]:                     #keyboard size buttons
        d += 1
    if pressed[pygame.K_5]:
        d -= 1
        
    if draw and x < 799:                        #drawing
        if circle:
            pygame.draw.circle(screen, color, (x, y), d)
        elif square:
            pygame.draw.rect(screen, color, [x, y, d*1.5, d*1.5])
        elif rect:
            pygame.draw.rect(screen, color, [x, y, d*1.5, d])
        elif rhomb:
            pygame.draw.polygon(screen, color, [[x, y-d], [x+d, y], [x, y+d], [x-d, y]])
        elif et:
            pygame.draw.polygon(screen, color, [[x, y], [x-d, y+d*1.5], [x+d, y+d*1.5]])
        elif rt:
            pygame.draw.polygon(screen, color, [[x, y], [x, y+d], [x+d, y+d]])
    elif erase and x < 799:
        pygame.draw.circle(screen, (255, 255, 255), (x, y), d)
        
        
    #front    
    pygame.draw.rect(screen, (251, 224, 217), [800, 0, 200, 800])   #buttons display

    pygame.draw.rect(screen, (236,183,179), [800, 0, 2, 800])     #color
    pygame.draw.rect(screen, (255, 0, 0), [810, 10, 50, 50])
    pygame.draw.rect(screen, (0, 255, 0), [875, 10, 50, 50])
    pygame.draw.rect(screen, (0, 0, 255), [940, 10, 50, 50])
    pygame.draw.rect(screen, (255, 255, 0), [810, 70, 50, 50])
    pygame.draw.rect(screen, (0, 255, 255), [875, 70, 50, 50])
    pygame.draw.rect(screen, (255, 0, 255), [940, 70, 50, 50])

    pygame.draw.rect(screen, (236,183,179), [810, 300, 80, 80])#square     #shape
    pygame.draw.circle(screen, (236,183,179), (950, 340), 40)#circle
    pygame.draw.rect(screen, (236,183,179), [810, 420, 80, 60])#rect
    pygame.draw.polygon(screen, (236,183,179), [[950, 410], [990, 450], [950, 490], [910, 450]])#rhombus
    pygame.draw.polygon(screen, (236,183,179), [[850, 510], [810, 590], [890, 590]])#equivalent triangle
    pygame.draw.polygon(screen, (236,183,179), [[910, 510], [910, 590], [990, 590]])#right triangle

    pygame.draw.rect(screen, (236,183,179), [805, 200, 40, 40])     #size
    pygame.draw.rect(screen, (236,183,179), [855, 200, 40, 40])
    pygame.draw.rect(screen, (236,183,179), [905, 200, 40, 40])
    pygame.draw.rect(screen, (236,183,179), [955, 200, 40, 40])
    
    screen.blit(s8,(880, 240))                                      #big text
    screen.blit(s7,(863, 590)) 
    screen.blit(s6,(863, 125))

    screen.blit(s1,(805, 150))                                      #little text
    screen.blit(s2,(805, 160))  
    screen.blit(s3,(805, 170)) 
    screen.blit(s4,(805, 750)) 
    screen.blit(s5,(805, 760)) 
    screen.blit(s13,(805, 265)) 

    screen.blit(s9,(815, 205))                                      #button text
    screen.blit(s10,(865, 205))
    screen.blit(s11,(915, 205))
    screen.blit(s12,(965, 205))
    
    pygame.display.flip()
    FPS.tick(120)