import pygame

class SpriteSheet():
    def __int__(self,image):
        self.sheet = image

    #take image
    #create surface
    #crate collision from surface
    def create_sprite(self,w,h):
        sprite = pygame.image.load(self.sheet)
        surface = pygame.Surface((w,h)).convert_alpha()
        collision = surface.get_rect(center=(400,400),width=130,height=100)
        draw_sprite = surface.blit(sprite,(0,0),(0,0,250,3616))
        draw_surface = screen.blit(surface,collision)
        return draw_sprite,draw_surface