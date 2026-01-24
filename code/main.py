import pygame

#initial pygame set up
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 600, 360
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame_icon = pygame.image.load("assets/images/explosion/2.png")
pygame.display.set_icon(pygame_icon)
pygame.display.set_caption("space shooter by amnerysdev ˙⋆✮")

running = True 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             running = False
    
    #drawing the game :)
    display_surface.fill("lightblue")
    pygame.display.update()
    
pygame.quit()