import pygame
from SPrite import SpriteSheet
import math
pygame.init()


bg = (50,130,200)
clock = pygame.time.Clock()
#-------------------------------------------------------------------------------cursor
pygame.mouse.set_visible(False)
Curor_nutural = pygame.image.load("Game\img\Cursor\Press (static).png")
Curorgrab = pygame.image.load("Game\img\Cursor\Grab (static).png")

Curorgrab = pygame.transform.scale_by(Curorgrab,1.5)
Curor_nutural = pygame.transform.scale_by(Curor_nutural,1.5)

#--------------------------------------------------------------------------------music
grab_sfx = pygame.mixer.Sound('Game\Sound\grab.mp3')
walk_sfx = pygame.mixer.Sound('Game\Sound\walk.mp3')
drop_sfx = pygame.mixer.Sound('Game\Sound\Sample_0017.wav')
sfx_1 = pygame.mixer.Sound('Game\Sound\Sample_0014.wav')
sfx_2 = pygame.mixer.Sound('Game\Sound\Sample_0015.wav')


screen = pygame.display.set_mode((500, 500))
player = pygame.Rect((300,100,50,100))

Spritesheet_imgae = pygame.image.load("Game\img\sprite_sheet.png").convert_alpha()
katmari = pygame.image.load("Game\img\grab.png").convert_alpha()
collision_mask = pygame.mask.from_surface(katmari)
katmari = pygame.transform.scale_by(katmari,1.4)

Player_location = (100,30)
#---------------------------------------------------------------------------pickup surfaces
pick_rec = pygame.Surface((165,150)).convert_alpha()
test_rect= pick_rec.get_rect(midtop=(Player_location))

idle = pygame.image.load("Game\img\spritesheet.png").convert_alpha()
idle_rec =pygame.Surface((130,200)).convert_alpha()
collision = idle_rec.get_rect(midtop=(100,30),width=130,height=100)
# -------------------------------------------------------------------------walk surfaces
walk = pygame.Surface((165,150)).convert_alpha()
walk = pygame.image.load("Game\img\walk.png").convert_alpha()
walk_rec =pygame.Surface((130,200)).convert_alpha()
collision_walk = walk_rec.get_rect(midtop=(100,20),width=130,height=100)


katmari.set_alpha(0)
idle.set_alpha(255)
walk.set_alpha(0)
#-----------------------------playermovment cordinateswwwwwwww
collision.x,collision.y =(0,0)
collision_walk.x,collision_walk.y =(0,0)
Player_location = (100,30)
# -------------------sprite incriments
idle_rotate = 0
idle_ani = 394
w = 551.6
#---------------------game states
walk_state = False
rotate_Right = False
rotate_left =False
Grabed = False


while True:
    
    screen.fill(bg)
    pick_rec.fill((0,0,0,0))
    idle_rec.fill((0,0,0,0))
    walk_rec.fill((0,0,0,0))
    #---------------------------------------------------- Exit App
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit( )
        #---------------------------------------------------- Arrow Keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
             rotate_left = True
             print("Released")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
             rotate_left = False
             

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rotate_Right =True
                

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
             rotate_Right = False
             
        #---------------------------------------------------------------- Walk, WASD
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_w:
              walk_state = True
              walk_sfx.play()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
             walk_state = False
             walk_sfx.stop()
             
        #---------------------------------------------------------------Grab/Mouse Controls
        if event.type == pygame.MOUSEBUTTONDOWN:
            Curorgrab.set_alpha(255)
            if collision.collidepoint(x,y):
                print("Click")
                sfx_1.play()
                Grabed = True
                grab_sfx.play()
        if event.type == pygame.MOUSEMOTION:
           if Grabed == True:
            collision.move_ip(event.rel)
            collision_walk.move_ip(event.rel)
        
        if event.type == pygame.MOUSEBUTTONUP:
            print("Released")
            sfx_2.play()
            drop_sfx.play()
            Grabed = False
    

    

    x,y = pygame.mouse.get_pos()
    
    


    #------------------------------------------------------------------idle
    idle_rec.blit(idle,(-130,0),(idle_ani,idle_rotate,250, 3616))
    screen.blit(idle_rec,collision)
    #------------------------------------------------------------------walk
    walk_rec.blit(walk,(-130,0),(idle_ani,idle_rotate,250, 3616))
    screen.blit(walk_rec,collision_walk)
    
    #-----------------------------------------------------------------Rotation animation logic
    if rotate_Right == True:
        idle_rotate += 226
    if rotate_left == True:
        if idle_rotate == 0:
         idle_rotate = 3164
        else:
         idle_rotate -= 226
    if idle_rotate == 3616:
        idle_rotate = 0

    print(idle_rotate)
    #--------------------------------------------------------------------idle_sprite animations
    idle_ani += 394
    if idle_ani == 6304:
        idle_ani = 394

   #---------------------------------------------------------------------pickup animation
    w += 551.6
    if w >= 3861:
        w = 551.6
    
    pick_rec.blit(katmari,(-180,-65),(w,0,430,1000))
    screen.blit(pick_rec,test_rect)
    #--------------------------------------------------------------------------------------walk_logic
    print(idle_rotate)


    #----------------------------------------------------------walk logic
    if walk_state == True:
       if Grabed ==  False:
        collision_walk.y += 10
        collision.y +=10
        walk.set_alpha(255)
        idle.set_alpha(0)
    else:
       walk.set_alpha(0)
       idle.set_alpha(255)
       




    #-------------------------------------------------------------------------Grab Logic
    if Grabed == True:
       test_rect.x = x -86
       test_rect.y = y
       katmari.set_alpha(255)
       idle.set_alpha(0)
       Curor_nutural.set_alpha(0)
       idle_rotate = 0
    
    else:
       grab_sfx.stop()
       katmari.set_alpha(0)
       
       Curorgrab.set_alpha(0)
       Curor_nutural.set_alpha(255)
       
       

    
    screen.blit(Curor_nutural,(x -15,y-10))
    screen.blit(Curorgrab,(x -15,y-10))
    
    
    dt= clock.tick(30) 
    pygame.display.update()
    pygame.display.flip()
