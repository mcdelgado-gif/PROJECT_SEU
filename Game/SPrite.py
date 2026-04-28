import pygame
pygame.init()

class Player:
    def __init__(self,Image):
        Grabbed = False
        self.Image = Image



    def load_sprite(self):
        sheet = self.Image
        Sprite = pygame.image.load(sheet)
        
        return Sprite
    

