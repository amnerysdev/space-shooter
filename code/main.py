import pygame
import random

class Player(pygame.sprite.Sprite):
    
    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.image.load("assets/images/player.png").convert_alpha()
        self.rect  = self.image.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        self.player_direction = pygame.math.Vector2(0,0)
        self.player_speed = 300   
  
        #cooldown
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 400
        
    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks() 
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True
                 
    def update(self,dt):
        keys = pygame.key.get_pressed()
        self.player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.player_direction = self.player_direction.normalize() if self.player_direction else self.player_direction
        self.rect.center +=  self.player_direction * self.player_speed * dt

        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            Laser(laser_surf, self.rect.midtop, all_sprites)
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()
        
        self.laser_timer()
class Star(pygame.sprite.Sprite):
    def __init__(self, group, surf):
        super().__init__(group)
        self.image = surf
        self.rect = self.image.get_frect(center = (random.randint(0,WINDOW_WIDTH), random.randint(0,WINDOW_HEIGHT)))

class Laser (pygame.sprite.Sprite): 
    def __init__(self, surf, pos, group):
        super().__init__(group)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = pos)
          
    def update(self, dt):
        self.rect.centery -= 400 * dt
        if self.rect.bottom < 0:
            self.kill()

class Meteor(pygame.sprite.Sprite):
    def __init__(self, surf, pos, group):
        super().__init__(group)
        self.image = surf
        self.rect = self.image.get_frect(center = pos)  
        self.created_time = pygame.time.get_ticks()
        self.lifetime = 3000
        self.direction = pygame.math.Vector2(random.uniform(-0.5, 0.5), 1).normalize()
        self.speed = random.randint(100, 200)
        
    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        current_time = pygame.time.get_ticks()
        if current_time - self.created_time >= self.lifetime:
            self.kill()    
        
                         
#initial pygame set up
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 760, 500
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame_icon = pygame.image.load("assets/images/explosion/2.png").convert_alpha()
pygame.display.set_icon(pygame_icon)
pygame.display.set_caption("space shooter by amnerysdev ˙⋆✮")
clock = pygame.time.Clock()
running = True 

#surfaces
star_surf = pygame.image.load("assets/images/star.png").convert_alpha()
meteor_surf = pygame.image.load("assets/images/meteor.png").convert_alpha()
laser_surf = pygame.image.load("assets/images/laser.png").convert_alpha()
all_sprites = pygame.sprite.Group()

for _ in range(20):
    Star(all_sprites, star_surf)
player = Player(all_sprites) 

#Custom Event -> Metor Event
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)


while running:
    dt = clock.tick()/1000 
    
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             running = False
        if event.type == meteor_event:
            x,y = (random.randint(0, WINDOW_WIDTH), random.randint(-200, -100))      
            Meteor(meteor_surf, (x,y), all_sprites)
            
      
    #updating our game 
    all_sprites.update(dt)
     
    #drawing the game :)
    display_surface.fill("darkgrey")
    all_sprites.draw(display_surface)   
    pygame.display.update()
    
pygame.quit()