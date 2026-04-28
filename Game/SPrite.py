import pygame
pygame.init()

class Player:
    def __init__(self,Image,scale):
        Grabbed = False
        self.Image = Image
        self.scale = scale
        self.loaded_sprite = self.load_sprite()



    def load_sprite(self):
        sheet = self.Image
        Sprite = pygame.image.load(sheet)
        Sprite = pygame.transform.scale_by(Sprite,self.scale)

        return Sprite
    def create_surface(self):
        Surface = pygame.Surface((165,150))
        Surface.fill((255,255,255))
        x = Surface

        return x

    

