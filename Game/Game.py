import pygame
from SPrite import Player 
pygame.init()


bg = (50,130,200)
screen = pygame.display.set_mode((800, 800))
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
eat_sfx = pygame.mixer.Sound('Game\Sound\Yum_Eat.mp3')


# -------------------sprite incriments
idle_rotate = 0
#---------------------game states
walk_state = False
rotate_Right = False
rotate_left =False
Grabed = False
Grab_Player = False
Eaten = False

Prince = Player("Game\img\spritesheet.png",1)
Prince_Sprite = Prince.load_sprite()
Prince_location = Prince.collider(100,80,130,80)
Prince_Surface = Prince.create_surface()

Prince_Grab = Player("Game\img\grab.png",1.4)
Prince_Grab.next_frame = 551.6
Prince_Grab.end_frame = 3861
Grab_Sprite = Prince_Grab.load_sprite()
Grab_Surface = Prince_Grab.create_surface()
Grab_location = Prince_Grab.collider(200,0,130,80)





t =0
while True:
   
    screen.fill((150,100,50))


    if rotate_Right == True:
            idle_rotate += 226
    if rotate_left == True:
            if idle_rotate == 0:
                idle_rotate = 3164
            else:
                idle_rotate -= 226
    if idle_rotate == 3616:
            idle_rotate = 0


    if Grabed == True:
       if Grab_Player == True:
        Prince_location.x = x - 86
        Prince_location. y = y
        Grab_Sprite.set_alpha(255)
        Prince_Sprite.set_alpha(0)
        idle_rotate = 0

        
    else:
       Grab_Sprite.set_alpha(0)
       Prince_Sprite.set_alpha(255)
       grab_sfx.stop()
       
       Curorgrab.set_alpha(0)
       Curor_nutural.set_alpha(255)
    
          



    Animation = Prince.run_animation()
    Prince_Surface.blit(Prince_Sprite,(-125,-30),(Animation,idle_rotate,400,200))
    screen.blit(Prince_Surface,Prince_location)
    Prince_Surface.fill((0,0,0,0))
    
    Grab_Animation = Prince_Grab.run_animation()
    Grab_Surface.blit(Grab_Sprite,(-180,-65),(Grab_Animation,0,430,1000))
    screen.blit(Grab_Surface,Prince_location)
    Grab_Surface.fill((0,0,0,0))
   
    

    
   
  
    
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

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
             up = False
             walk_state = False
             walk_sfx.stop()
            if event.key == pygame.K_s:
             down = False
             walk_state = False
             walk_sfx.stop()
            if event.key == pygame.K_a:
             Right = False
             walk_state = False
             walk_sfx.stop()
            if event.key == pygame.K_d:
             walk_state = False
             left = False
             walk_sfx.stop()
             
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_w:
                walk_state = True
                up = True
                walk_sfx.play()
           if event.key == pygame.K_s:
              walk_state = True
              down =True
              walk_sfx.play()
           if event.key == pygame.K_a:
              Right = True
              walk_state = True
              idle_rotate = 2486
              walk_sfx.play()
           if event.key == pygame.K_d:
              walk_state = True
              left =True
              walk_sfx.play()
        
        
        


        #---------------------------------------------------------------Grab/Mouse Controls
        if event.type == pygame.MOUSEBUTTONDOWN:
            Grabed = True
            Curorgrab.set_alpha(255)
            Curor_nutural.set_alpha(0)

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
            Grab_Player = False
    


    x,y = pygame.mouse.get_pos()
    
#---------------------------------------------- cursor
    screen.blit(Curor_nutural,(x -15,y-10))
    screen.blit(Curorgrab,(x -15,y-10))


    clock.tick(32) 
    pygame.display.update()
    pygame.display.flip()
