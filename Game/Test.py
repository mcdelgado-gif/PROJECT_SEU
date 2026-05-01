import pygame
from SPrite import Player 
pygame.init()

#---Config------
bg = (50,130,200)
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

Prince = Player("Game\img\spritesheet.png",1)
Prince_Sprite = Prince.load_sprite()
Prince_location = Prince.collider(400,80,130,80)
Prince_Surface = Prince.create_surface(165,150)
Animation = Prince.run_animation()
idle_rotate = 0


Prince_Grab = Player("Game\img\grab.png",1.4)
Prince_Grab.next_frame = 551.6
Prince_Grab.end_frame = 3861
Grab_Sprite = Prince_Grab.load_sprite()
Grab_Surface = Prince_Grab.create_surface(1650,1500)

exmaple = Player("Game\img\grab.png",0.5)
exmaple_s = exmaple.load_sprite()

while True:
    screen.fill((0,0,0))

    Prince_Surface.blit(Prince_Sprite,(-125,-30),(Animation,idle_rotate,400,200))
    screen.blit(Prince_Surface,Prince_location)
    Prince_Surface.fill((255,255,255))

    Grab_Animation = Prince_Grab.run_animation()
    Grab_Surface.blit(Grab_Sprite,(-180,-65),(Grab_Animation,0,4300,1000))
    screen.blit(Grab_Surface,(0,400))
    Grab_Surface.fill((0,0,0,0))
    
    screen.blit(Prince_Surface,(100,100))
    screen.blit(exmaple_s,(0,0))

    







    #---------------------------------------------------- Exit App
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit( )
        #---------------------------------------------------- Arrow Keys

    clock.tick(60) 
    pygame.display.update()
    
