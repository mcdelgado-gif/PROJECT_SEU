import pygame
pygame.init()

class Player:
    def __init__(self,Image,scale):
        Grabbed = False
        self.Image = Image
        self.scale = scale
        self.loaded_sprite = self.load_sprite()
        self.starting_frame = 0
        self.next_frame = 394
        self.end_frame = 6304



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
    def run_animation(self):
        self.starting_frame += self.next_frame
        if self.starting_frame == self.end_frame:
            self.starting_frame = 0
        return self.starting_frame
        
        
    

