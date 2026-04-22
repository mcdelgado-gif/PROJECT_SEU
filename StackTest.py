import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800,200))
pygame.display.set_caption("HEL MEEEE")
clock = pygame.time.Clock() #pygame tick

katamari =  pygame.image.load("img\SpriteStack_Cars\BlueCar.png")
kat = pygame.Surface((100,200))
kat_scale = 6

katamari = pygame.transform.scale_by(katamari,kat_scale)

kat.fill((255,255,0))



surface = pygame.image.load("img/torus.png")
surface = pygame.transform.scale_by(surface,2.0)

    #rect_1 = surface.get_rect(topleft=(0,0), width=100, height=50)
    #surface = surface.subsurface(rect_1)
#print(rect_1)


character_surface = pygame.Surface((125,200))
character_surface.fill((255,255,0))

square_x = 20
square_y = 48

deer_y_counter = 100
h = 3

x= -80
y = 55
counter = 100
y_counter = 0.5
while True:
    #draw all elements
    #update
    # check for types of player input with an event loo6

    #events only activte on the frame its activatied on
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
    
    screen.blit(kat,(20,40))
    kat.blit(katamari,(square_x,square_y),(0,0,4000,80))

    square_x -= deer_y_counter
    square_y -= h
    
    print(square_x)



    screen.blit(character_surface,(325,50))
    x -= counter
    y -= y_counter
    


    character_surface.blit(surface,(x,y, 100,100))
   

    
    


   
    
       
       
  

 
    pygame.display.update() #updates the pygamescreen
    clock.tick(15) #framerate cap