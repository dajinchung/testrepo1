import pygame

#init pygame
pygame.init

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen  = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# square that player controls
player = pygame.Rect((300,250,50,50))

# game loop
run = True
while run:
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,0,0),player)
    #controls
    key = pygame.key.get_pressed()
        # check for wasd to be pressed, key press moves square
    if key[pygame.K_a] == True:
        player.move_ip(-1,0)
    elif key[pygame.K_d] == True:
        player.move_ip(1,0)
    elif key[pygame.K_w] == True:
        player.move_ip(0,-1)
    elif key[pygame.K_s] == True:
        player.move_ip(0,1)
#event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #update display
    pygame.display.update()
pygame.quit()
