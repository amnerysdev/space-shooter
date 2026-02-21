import pygame
import random

#initial pygame set up
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 760, 500
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame_icon = pygame.image.load("assets/images/explosion/2.png").convert_alpha()
pygame.display.set_icon(pygame_icon)
pygame.display.set_caption("space shooter by amnerysdev ˙⋆✮")
clock = pygame.time.Clock()
running = True 

#Surfaces: text, img or plain areas.
star_surf = pygame.image.load("assets/images/star.png").convert_alpha()
coordinates = [(random.randint(0,WINDOW_WIDTH),random.randint(0,WINDOW_HEIGHT)) for _ in range(19)]

player_surf = pygame.image.load("assets/images/player.png").convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
player_direction = pygame.math.Vector2(0,0)
player_speed = 100 

meteor_surf = pygame.image.load("assets/images/meteor.png").convert_alpha()
meteor_rect = meteor_surf.get_frect(center= (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

laser_surf = pygame.image.load("assets/images/laser.png").convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft= (20, WINDOW_HEIGHT-20))



while running:
    dt = clock.tick()/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             running = False
    
    #player movement and input
    keys = pygame.key.get_pressed()
    player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
    player_rect.center +=  player_direction * player_speed * dt
         
    #drawing the game :)
    display_surface.fill("darkgrey")
    for coordinate in coordinates:
        display_surface.blit(star_surf, coordinate)
        
    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)  
    display_surface.blit(player_surf, player_rect)
    
    
    pygame.display.update()
    
pygame.quit()