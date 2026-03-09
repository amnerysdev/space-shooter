import pygame
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.image.load("assets/images/player.png").convert_alpha()
        self.rect  = self.image.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        self.player_direction = pygame.math.Vector2(0,0)
        self.player_speed = 300   
  
    def update(self,dt):
        keys = pygame.key.get_pressed()
        self.player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.player_direction = self.player_direction.normalize() if self.player_direction else self.player_direction
        self.rect.center +=  self.player_direction * self.player_speed * dt

class Star(pygame.sprite.Sprite):
    def __init__(self, group, surf):
        super().__init__(group)
        self.image = surf
        self.rect = self.image.get_frect(center = (random.randint(0,WINDOW_WIDTH), random.randint(0,WINDOW_HEIGHT)))
    
  
    
#initial pygame set up
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 760, 500
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame_icon = pygame.image.load("assets/images/explosion/2.png").convert_alpha()
pygame.display.set_icon(pygame_icon)
pygame.display.set_caption("space shooter by amnerysdev ˙⋆✮")
clock = pygame.time.Clock()
running = True 


star_surf = pygame.image.load("assets/images/star.png").convert_alpha()
all_sprites = pygame.sprite.Group()
for _ in range(20):
    Star(all_sprites, star_surf)
player = Player(all_sprites) 



meteor_surf = pygame.image.load("assets/images/meteor.png").convert_alpha()
meteor_rect = meteor_surf.get_frect(center= (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

laser_surf = pygame.image.load("assets/images/laser.png").convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft= (20, WINDOW_HEIGHT-20))

#state variable to check the status of a variable.
key_status = False

while running:
    dt = clock.tick()/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             running = False
    
         
    #drawing the game :)
    display_surface.fill("darkgrey")
      
    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)  
    
    all_sprites.update(dt)
    all_sprites.draw(display_surface)
    
    
    pygame.display.update()
    
pygame.quit()