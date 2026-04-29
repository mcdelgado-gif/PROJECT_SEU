import pygame
from SPrite import Player 
pygame.init()

#---Config------
bg = (50,130,200)
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
#----------------------sound effects-----
grab_sfx = pygame.mixer.Sound('Game\Sound\grab.mp3')
walk_sfx = pygame.mixer.Sound('Game\Sound\walk.mp3')
drop_sfx = pygame.mixer.Sound('Game\Sound\Sample_0017.wav')
sfx_1 = pygame.mixer.Sound('Game\Sound\Sample_0014.wav')
sfx_2 = pygame.mixer.Sound('Game\Sound\Sample_0015.wav')
eat_sfx = pygame.mixer.Sound('Game\Sound\Yum_Eat.mp3')
#---------Sprite Rotation-----------------------
idle_rotate = 0
#---------------------game states--------------
walk_state = False
rotate_Right = False
rotate_left =False
Grabed = False
Grab_Player = False
Eaten = False
#------------------------Sprites/Surfaces/Collision
Prince = Player("Game\img\spritesheet.png",1)
Prince_Sprite = Prince.load_sprite()
Prince_location = Prince.collider(100,80,130,80)
Prince_Surface = Prince.create_surface(165,150)

Prince_Grab = Player("Game\img\grab.png",1.4)
Prince_Grab.next_frame = 551.6
Prince_Grab.end_frame = 3861
Grab_Sprite = Prince_Grab.load_sprite()
Grab_Surface = Prince_Grab.create_surface(165,150)

Prince_Walk = Player("Game\img\walk.png",1)
Prince_w_sprite = Prince_Walk.load_sprite()
walk_surface = Prince_Walk.create_surface(165,150)

Cursor_natural = Player("Game\img\Cursor\Press (static).png",1.5)
Cursor_Sprite = Cursor_natural.load_sprite()
Cursor_Surface = Cursor_natural.create_surface(50,50)

Cur_Grab = Player("Game\img\Cursor\Grab (static).png",1.5)
Cur_Grab_Sprite = Cur_Grab.load_sprite()
Cur_Grab_Surface = Cur_Grab.create_surface(50,50)


while True:
    x,y = pygame.mouse.get_pos()
   
    screen.fill((150,100,50))
#--------PLAYER Rotation---------
    if rotate_Right == True:
            idle_rotate += 226
            print(idle_rotate)
    if rotate_left == True:
            if idle_rotate == 0:
                idle_rotate = 3164
            else:
                idle_rotate -= 226
    if idle_rotate == 3616:
            idle_rotate = 0

#------Grab Logic---------------
    if Grabed == True:
       if Grab_Player == True:
        Prince_location.x = x - 86
        Prince_location. y = y
        Grab_Sprite.set_alpha(255)
        Prince_Sprite.set_alpha(0)
        idle_rotate = 0
    else:
       Cursor_Sprite.set_alpha(255)
       Cur_Grab_Sprite.set_alpha(0)
       Grab_Sprite.set_alpha(0)
       grab_sfx.stop()
       
    Animation = Prince.run_animation()
    Prince_Surface.blit(Prince_Sprite,(-125,-30),(Animation,idle_rotate,400,200))
    screen.blit(Prince_Surface,Prince_location)
    Prince_Surface.fill((0,0,0,0))
    
    Grab_Animation = Prince_Grab.run_animation()
    Grab_Surface.blit(Grab_Sprite,(-180,-65),(Grab_Animation,0,430,1000))
    screen.blit(Grab_Surface,Prince_location)
    Grab_Surface.fill((0,0,0,0))
   
    walk_surface.blit(Prince_w_sprite,(-125,-30),(Animation,idle_rotate,400,200))
    screen.blit(walk_surface,Prince_location)
    walk_surface.fill((0,0,0,0))
    Prince_w_sprite.set_alpha(0)

    Cur_Grab_Surface.blit(Cur_Grab_Sprite,(0,0))
    screen.blit(Cur_Grab_Surface,(x-10,y-10))
    cursor_Grab_location = Cursor_natural.collider(x-10 ,y-10,50,50)
    Cur_Grab_Surface.fill((0,0,0,0))
   
    Cursor_Surface.fill((0,0,0,0))
    Cursor_Surface.blit(Cursor_Sprite,(0,0))
    screen.blit(Cursor_Surface,(x-10,y-10))
    cursor_location = Cursor_natural.collider(x-10 ,y-10,50,50)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        Prince_location.y -= 10
        idle_rotate = 1568
        walk_state = True
    if keys[pygame.K_s]:
        Prince_location.y += 10
        idle_rotate = 0
        walk_state = True
    if keys[pygame.K_a]:
        Prince_location.x -= 10
        idle_rotate = 2486
        walk_state = True
    if keys[pygame.K_d]:
        Prince_location.x += 10
        idle_rotate = 678
        walk_state = True

    if walk_state == True:
        Prince_Sprite.set_alpha(0)
        Prince_w_sprite.set_alpha(255)
        walk_state = False
    else:
        Prince_w_sprite.set_alpha(0)
        Prince_Sprite.set_alpha(255)

    #---------------------------------------------------- Exit App
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit( )
        #---------------------------------------------------- Arrow Keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rotate_left = True
                print(rotate_left)
            if event.key == pygame.K_RIGHT:
                rotate_Right = True
                print(rotate_Right)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
             rotate_left = False
             print(rotate_left)
            if event.key == pygame.K_RIGHT:
             rotate_Right = False
             print(rotate_Right)
        #---------------------------------------------------------------- Walk, WASD
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                walk_sfx.play()
            if event.key == pygame.K_a:
                walk_sfx.play()
            if event.key == pygame.K_s:
                walk_sfx.play()
            if event.key == pygame.K_d:
                walk_sfx.play()
        if event.type == pygame.KEYUP:
                walk_sfx.stop()
            
    
        #---------------------------------------------------------------Grab/Mouse Controls
        if event.type == pygame.MOUSEBUTTONDOWN:
            Grabed = True
            Cursor_Sprite.set_alpha(0)
            Cur_Grab_Sprite.set_alpha(255)
            if Prince_location.collidepoint(x,y):
                print("Click")
                sfx_1.play()
                Grab_Player = True
                grab_sfx.play()
        if event.type == pygame.MOUSEBUTTONUP:
            print("Released")
            sfx_2.play()
            drop_sfx.play()
            Grabed = False
            Grab_food = False


    clock.tick(32) 
    pygame.display.update()
    pygame.display.flip()
