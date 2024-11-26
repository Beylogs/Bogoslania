import pygame

#constant variables
SCREEN_SIZE = (700,500)
DARK_GREY = (50,50,50)
WHITE = (255, 255, 255)

#init
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Platformer Game")

font = pygame.font.SysFont('Arial', 36)  # Choose the font and size
text = font.render('Hello, Pygame!', True, WHITE)  # Create the text surface
text_rect = text.get_rect(center=(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2))  # Position the text in the center

while True:
#game loop

    #input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #update

    #draw
    screen.fill(DARK_GREY)
    pygame.display.flip()

#quit
pygame.quit()