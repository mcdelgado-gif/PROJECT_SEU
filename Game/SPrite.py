import pygame
pygame.init()

class Player:
    def __init__(self,Image,scale):
        w = 0
        h = 0
        self.Grabbed = False
        self.Walking = False
        self.Image = Image
        self.scale = scale
        self.loaded_sprite = self.load_sprite()
        self.sprite_surface = self.create_surface(w,h)
        self.starting_frame = 0
        self.next_frame = 394
        self.end_frame = 6304



    def load_sprite(self):
        sheet = self.Image
        Sprite = pygame.image.load(sheet)
        Sprite = pygame.transform.scale_by(Sprite,self.scale)
       
        return Sprite
    def create_surface(self,w,h):
        Surface = pygame.Surface((w,h)).convert_alpha()
        x = Surface

        return x
    
    def collider(self,x,y,w,h):
         Sprite_Collision = self.sprite_surface.get_rect(midtop=(x,y),width=w,height=h)

         return Sprite_Collision

    def run_animation(self):
        self.starting_frame += self.next_frame
        if self.starting_frame >= self.end_frame:
            self.starting_frame = 0
        return self.starting_frame
        
        
0
226
452
678
904
1130
1356
1582
1808
2034
2260
2486
2712
2938
3164
3390
3616