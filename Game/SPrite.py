import pygame
pygame.init()

class Player:
    def __init__(self, image):
        self.sheet = image
        Grabbed = False


        

    #take image
    #create surface
    #crate collision from surface
    def load_sprite(self,image,w,h):
        surface = pygame.Surface((w,h)).convert_alpha()
        
        return surface
    
