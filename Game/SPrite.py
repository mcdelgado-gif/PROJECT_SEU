import pygame
pygame.init()

class SpriteSheet:
    def __init__(self, image):
        self.sheet = image

    #take image
    #create surface
    #crate collision from surface
    def create_sprite(self,image,w,h):
        surface = pygame.Surface((w,h)).convert_alpha()
        collision = surface.get_rect(center=(400,400),width=130,height=100)
        surface = surface.blit(image,(0,0),(0,0,w,h))
        
        return surface
    
