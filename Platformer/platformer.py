import pygame

#constant variables
SCREEN_SIZE = (1280, 720)
DARK_GREY = (50,50,50)
WHITE = (255, 255, 255)

#init
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Nino\'s Platformer Game')

font = pygame.font.SysFont('Arial', 36)  # Choose the font and size
text = font.render('Hello, Pygame!', True, WHITE)  # Create the text surface
text_rect = text.get_rect(center=(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2))  # Position the text in the center

#player
player_image = pygame.image.load('Platformer/images/vita_00.png')

#platforms
platform = pygame.Rect(100,300,400,50)

running = True

while running:
#game loop

    #input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #update

    #draw

    #background
    screen.fill(DARK_GREY)
    #platforms
    pygame.draw.rect(screen, WHITE, platform)
    #player
    screen.blit(player_image, (300,100))
    #present screen
    pygame.display.flip()

#quit
pygame.quit()