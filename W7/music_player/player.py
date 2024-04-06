import pygame

pygame.init()

index = 1
stop = True

screen = pygame.display.set_mode((895, 825))
pygame.display.set_caption("Coquette Player ୨୧")

clock = pygame.time.Clock()

font = pygame.font.SysFont('Maiandra GD', 30)
s_1 = font.render("You can pause/play music by pressing SPACE", True, pygame.Color(255, 105, 180), pygame.Color(255, 228, 225))
s_2 = font.render("You can change music by pressing LEFT/RIGHT arrow", True, pygame.Color(255, 105, 180), pygame.Color(255, 228, 225))
s_3 = font.render("Song list:", True, pygame.Color(255, 105, 180), pygame.Color(255, 228, 225))
s_4 = font.render("Smarty", True, pygame.Color(255, 105, 180), pygame.Color(255, 228, 225))
s_5 = font.render("Behind Closed Doors", True, pygame.Color(255, 105, 180), pygame.Color(255, 228, 225))
s_6 = font.render("Ultraviolence", True, pygame.Color(255, 105, 180), pygame.Color(255, 228, 225))
s_7 = font.render("Yes To Heaven", True, pygame.Color(255, 105, 180), pygame.Color(255, 228, 225))
s_8 = font.render("Carmen", True, pygame.Color(255, 105, 180), pygame.Color(255, 228, 225))
s_9 = font.render("Million Dollar Man", True, pygame.Color(255, 105, 180), pygame.Color(255, 228, 225))
s_10 = font.render("Pretty When You Cry", True, pygame.Color(255, 105, 180), pygame.Color(255, 228, 225))
s_11 = font.render("Art Deco", True, pygame.Color(255, 105, 180), pygame.Color(255, 228, 225))

music_dict = {
    1 : 'W7\\music_player\\Smarty.mp3',
    2 : 'W7\\music_player\\Behind Closed Doors.mp3',
    3 : 'W7\\music_player\\Ultraviolence.mp3',
    4 : 'W7\\music_player\\Yes To Heaven.mp3',
    5 : 'W7\\music_player\\Carmen.mp3',
    6 : 'W7\\music_player\\Million Dollar Man.mp3',
    7 : 'W7\\music_player\\Pretty When You Cry.mp3',
    8 : 'W7\\music_player\\Art Deco.mp3',
}

pygame.mixer.music.load(music_dict[index])
pygame.mixer.music.play()

def play_music(bool_play):
    if not bool_play:
        pygame.mixer.music.unpause()
    else: 
        pygame.mixer.music.pause()
def next_music(index):
    pygame.mixer.music.load(music_dict[index])
    pygame.mixer.music.play()
    

while True:
    
    pressed = pygame.key.get_pressed()
    
    screen.fill((255, 255, 255))
    screen.blit(pygame.image.load('W7\\music_player\\bg.jpg'), (0, 0))
    screen.blit(s_1,(10, 10))
    screen.blit(s_2,(10, 50))
    screen.blit(s_3,(10, 120))
    screen.blit(s_4,(10, 160))
    screen.blit(s_5,(10, 200))
    screen.blit(s_6,(10, 240))
    screen.blit(s_7,(10, 280))
    screen.blit(s_8,(10, 320))
    screen.blit(s_9,(10, 360))
    screen.blit(s_10,(10, 400))
    screen.blit(s_11,(10, 440))
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if pressed[pygame.K_SPACE]:
            if stop == True: stop = False
            else: stop = True
            play_music(stop)
        if pressed[pygame.K_RIGHT]:
            if index == 8: index = 1
            else: index += 1
            next_music(index)
        if pressed[pygame.K_LEFT]:
            if index == 1: index = 8
            else: index -= 1
            next_music(index)
            
    
    pygame.display.flip()
    clock.tick(60)