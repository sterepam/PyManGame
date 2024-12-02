import pygame, sys
import random
clock = pygame.time.Clock()

from pygame.locals import *
pygame.init() 

pygame.display.set_caption('Py-Man')
window_size = (600,600)
display = pygame.display.set_mode(window_size,0,32)
black = (0,0,0)
white= (255,255 , 255)
global level1
global level2
level1=False
level2=False
StartGame=pygame.image.load("StartGame1.png")
StartGame2=pygame.image.load("StartGame2.png")
blackimg=pygame.image.load("black.png")
fallsound= pygame.mixer.Sound("Jump.wav")






def score(progress):
        font=pygame.font.Font("alien5.ttf",35)
        text=font.render("Score: :"+str(int(progress)) , True , (white))
        display.blit(text,(0,0))
def message_display(text, size ,x, y, color):
        largeText=pygame.font.Font("alien5.ttf",size)
        TextSurf , TextRect = text_objects(text , largeText , color)
        TextRect.center = (x ,y)
        display.blit(TextSurf ,TextRect)
def message_display1(text, size ,x, y, color):
        largeText=pygame.font.Font("neon.ttf",size)
        TextSurf , TextRect = text_objects(text , largeText , color)
        TextRect.center = (x ,y)
        display.blit(TextSurf ,TextRect)
        
    
def text_objects(text , font , color ):
        textSurface = font.render(text , True , color)
        return textSurface , textSurface.get_rect()

def game_intro():
        global intro
        global level1
        global level2
        pygame.mixer.init()
        pygame.mixer.music.load("deodato.mp3")                        
        pygame.mixer.music.play()
        display=pygame.display.set_mode((600,600),0,32)
##        def message_display(text, size ,x, y, color):
##        largeText=pygame.font.Font("alien5.ttf",size)
##        TextSurf , TextRect = text_objects(text , largeText , color)
##        TextRect.center = (x ,y)
##        display.blit(TextSurf ,TextRect)
        message_display("Py-Man" , 115 , 300 , 200, white)
        q=True
        s=True
        while intro==True:
            
            click=pygame.mouse.get_pressed()
            mouse=pygame.mouse.get_pos()
            
            
            if q==True:
                    display.blit(StartGame ,(170,380))
                    if 170<mouse[0]<420 and 380<mouse[1]<410:
                        display.blit(StartGame2 ,(170,380))
           
            
            
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN and 436<mouse[1]<458 and  221<mouse[0]<378 and q==True:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN and 170<mouse[0]<420 and 350<mouse[1]<410:
                    q=False
                    
                    
                if event.type == MOUSEBUTTONDOWN and 539<mouse[1]<560 and  221<mouse[0]<378 and q==False:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN and 437<mouse[1]<457 and  250<mouse[0]<347 and q==False:
                    level1=True
                    level2=False
                    intro=False
                if event.type == MOUSEBUTTONDOWN and 489<mouse[1]<511 and  250<mouse[0]<347 and q==False:
                    level1=False
                    level2=True
                    intro=False
                    
            if q==True:
                
                if 436<mouse[1]<458 and  221<mouse[0]<378:
                    message_display("Quit Game" ,35, 300 , 450, (240,40,200))
                else:
                        message_display("Quit Game" ,35, 300 , 450, (255,255,255))
                
                    
            else:
                display.fill((0,0,0))
                message_display("Py-Man" , 115 , 300 , 200, white)
                message_display("Quit Game" , 35 ,300 , 550 ,(255,255,255))
                if 539<mouse[1]<560 and  221<mouse[0]<378:
                    message_display("Quit Game" ,35, 300 , 550, (240,40,200))
                
                display.blit(StartGame2 ,(170,380))
                
                
                
                
                message_display("Level 1" , 30 ,300 , 450 ,(255,255,255))
                if 437<mouse[1]<457 and  250<mouse[0]<347:
                    message_display("Level 1" , 30 ,300 , 450 ,(255,40,230))
                
                message_display("Level 2" , 30 ,300 , 500 ,(255,255,255))
                if 489<mouse[1]<511 and  250<mouse[0]<347:
                    message_display("Level 2" , 30 ,300 , 500 ,(255,40,230))
                
                
                
                pygame.display.update()
        pygame.display.update()
            
            
intro=True

############################################################################################
#################################################################
##############################################
##############################################
while True:
    game_intro()
    if level1==True:
        pygame.mixer.init()
        pygame.mixer.music.load("simpleminds.mp3")                        
        pygame.mixer.music.play(-1)
        
        game=True
        while True:
            if game==False:
                break
            else:
                right = False
                left = False
                vertical_momentum = 0
                walkCount =0 
                air_timer = 0
                scroll=0
                camera_scroll=0
                goinRight = [pygame.image.load("right1.png").convert() ,pygame.image.load("right2.png").convert() ,pygame.image.load("right3.png").convert(),pygame.image.load("right4.png").convert()]
                goinLeft = [pygame.transform.flip(pygame.image.load("right1.png").convert(),1,0),pygame.transform.flip(pygame.image.load("right2.png").convert(),1,0),pygame.transform.flip(pygame.image.load("right3.png").convert(),1,0),pygame.transform.flip(pygame.image.load("right4.png").convert(),1,0)]
                player_img = pygame.image.load('standing.png').convert()

                def load_map(path):
                    f = open(path + '.txt','r')
                    data = f.read()
                    f.close()
                    data = data.split('\n')
                    game_map = []
                    for row in data:
                        game_map.append(list(row))
                    return game_map

                game_map = load_map('map')

                dirt_img = pygame.image.load('dirt.png')
                bg=pygame.image.load("lala.png")
                bglose=pygame.image.load("bglose.png")


                player_img.set_colorkey((0,0,0))
                player_rect = pygame.Rect(100,100,40,58)
                
                def redrawchar():
                    global walkCount
                    if walkCount +1 >32:
                        walkCount=0
                    if left:
                        goinLeft[walkCount//8].set_colorkey((0,0,0))
                        display.blit(goinLeft[walkCount//8] , (player_rect.x-scroll , player_rect.y))
                        walkCount+=1
                    elif right:
                        goinRight[walkCount//8].set_colorkey((0,0,0))
                        display.blit(goinRight[walkCount//8] , (player_rect.x-scroll , player_rect.y))
                        walkCount+=1
                    else:
                        display.blit(player_img , (player_rect.x-scroll , player_rect.y))
                    pygame.display.update()

                def collision_test(rect,tiles):
                    hit_list = []
                    for tile in tiles:
                        if rect.colliderect(tile):
                            hit_list.append(tile)
                    return hit_list

                def move(rect,movement,tiles):
                    collision_types = {'top':False,'bottom':False,'right':False,'left':False}
                    rect.x += movement[0]
                    hit_list = collision_test(rect,tiles)
                    for tile in hit_list:
                        if movement[0] > 0:
                            rect.right = tile.left
                            collision_types['right'] = True
                        elif movement[0] < 0:
                            rect.left = tile.right
                            collision_types['left'] = True
                    rect.y += movement[1]
                    hit_list = collision_test(rect,tiles)
                    for tile in hit_list:
                        if movement[1] > 0:
                            rect.bottom = tile.top
                            collision_types['bottom'] = True
                        elif movement[1] < 0:
                            rect.top = tile.bottom
                            collision_types['top'] = True
                    return rect, collision_types
                scrolla=1
                racc=0
                lacc=0
                bgPosX=0
                scroll2=0
                game=True
                a=True
                if intro==True:
                    game_intro()
                
                while True:
                    if game == False:
                        break
                    else:
                        if a==True:
                            display = pygame.display.set_mode((1200,400),0,32)
                        a=False
                        scroll += scrolla
                        scrolla+=0.002
                        if scrolla>4.8:
                            scrolla=4.6
                        
                        display.blit(bg , (-scroll , 0))
                        bgPosX -= scroll
                        
                        
                        tile_rects = []
                        y = 0
                        for layer in game_map:
                            x = 0
                            for o in range(2):
                                    for tile in layer:
                                        if tile == '1':
                                            display.blit(dirt_img,(x*24-scroll,y*24))
                                        if tile == '2':
                                            display.blit(grass_img,(x*24-scroll,y*24))
                                        if tile != '0':
                                            tile_rects.append(pygame.Rect(x*24,y*24,24,24))
                                        x += 1
                            y += 1

                        player_movement = [0,0]
                       
                        if right == True:
                            lacc=0
                            player_movement[0] += racc
                            racc+=0.1
                            if racc>=6:
                                racc=5.8
                            
                            
                        if left == True:
                            racc=0
                            player_movement[0] -= lacc
                            lacc+=0.1
                            if lacc>=6:
                                lacc=5.8
                        player_movement[1] += vertical_momentum
                        vertical_momentum += 0.2
                        if vertical_momentum > 3:
                            vertical_momentum = 3

                        player_rect,collisions = move(player_rect,player_movement,tile_rects)

                        if collisions['bottom'] == True:
                            air_timer = 0
                            vertical_momentum = 0
                        else:
                            air_timer += 1

                        
                        if scroll>=player_rect.x+50:
                            game=False
                            pygame.mixer.Sound.play(fallsound)
                            pygame.mixer.music.stop()
                        if player_rect.y>=400:
                            pygame.mixer.Sound.play(fallsound)
                            pygame.mixer.music.stop()
                            game=False
                        

                        for event in pygame.event.get():
                            if event.type == QUIT:
                                pygame.quit()
                                sys.exit()
                            if event.type == KEYDOWN:
                                if event.key == K_RIGHT:
                                    right = True
                                    left=False
                                    
                                if event.key == K_LEFT:
                                    left = True
                                    right=False
                                    
                                if event.key == K_UP:
                                    if air_timer < 6:
                                        vertical_momentum = -5
                            if event.type == KEYUP:
                                if event.key == K_RIGHT:
                                    right = False
                                    racc=0
                                    
                                if event.key == K_LEFT:
                                    left = False
                                    lacc=0
                        score(scroll)
                        
                        redrawchar()
                        clock.tick(60)
                        gamescore=scroll
                pygame.display.update()
               
    ###################################################################################################################
    ############################################################################################
    #####################################################################
    #####################################################################                
        pygame.time.delay(700)
        while True:
            if game==True:
                break
            else:
                scroll+=0.1
                if scroll>12000:
                        scroll=0
                
                display.blit(bglose , (-scroll,0))
                message_display("Your Score: {}".format(int(gamescore)) , 60, 600 , 250 , white)
                
                message_display("Press 'r' to retry" , 30 , 600 , 300, white)
                message_display("Press 'm' to go to menu" , 30 , 600 , 350, white)
                message_display1("Game Over" , 100 , 600 , 150 ,(white))
                pygame.display.update()
                
                message_display1("Game Over" , 100 , 600 , 150 ,(240,135,195))
                pygame.display.update()
                message_display1("Game Over" , 100 , 600 , 150 ,(240,135,195))
                pygame.display.update()
                message_display1("Game Over" , 100 , 600 , 150 ,(240,135,195))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_r:
                            game=True
                            intro=False
                        if event.key==K_m:
                            intro=True
                            game=True
                            game_intro()
##################################################################
##################################################################
##################################################################
    elif level2==True:
        game2=True
        pygame.mixer.init()
        pygame.mixer.music.load("heretostay.mp3")                        
        pygame.mixer.music.play()
        
        while True:
            
            if game2==False:
                break
            else:
                window_size = (1200,395)
                display= pygame.display.set_mode(window_size,0,32)
                bglose2=pygame.image.load("bglose2.png")



                up = False
                down = False
                right=False
                left=False
                vertical_momentum = 0
                scroll=0

                player_img = pygame.image.load('flying.png').convert()
                player_img.set_colorkey((0,0,0))
                bg=pygame.image.load("lala2.png")
                planeImg = pygame.image.load("plane.png").convert()
                planeImg.set_colorkey((0,0,0))
                pygame.display.update()
                bird=[pygame.image.load('bird1.png').convert(),pygame.image.load('bird2.png').convert(),pygame.image.load('bird3.png').convert(),pygame.image.load('bird4.png').convert(),pygame.image.load('bird5.png').convert(),pygame.image.load('bird6.png').convert(),pygame.image.load('bird7.png').convert(),pygame.image.load('bird8.png').convert()]
                bird2=[pygame.image.load('bird10.png').convert(),pygame.image.load('bird11.png').convert(),pygame.image.load('bird12.png').convert(),pygame.image.load('bird13.png').convert(),pygame.image.load('bird14.png').convert(),pygame.image.load('bird15.png').convert(),pygame.image.load('bird16.png').convert(),pygame.image.load('bird17.png').convert()]
                bird3=[pygame.image.load('bird30.png').convert(),pygame.image.load('bird31.png').convert(),pygame.image.load('bird32.png').convert(),pygame.image.load('bird33.png').convert(),pygame.image.load('bird34.png').convert(),pygame.image.load('bird35.png').convert()]
                flyCount=0
                

                player_rect = pygame.Rect(100,160,60,25)
                

                def birds(birdx,birdy,frames):
                    bird[frames].set_colorkey((255,255,255))
                    display.blit(bird[frames], (birdx,birdy))
                    
                def birds2(bird2x,bird2y,frames):
                   display.blit(bird2[frames], (bird2x,bird2y))
                   bird2[frames].set_colorkey((0,0,0))
                def plane(planex, planey):
                    display.blit(planeImg , (planex, planey))
                       
                def birds3(bird3x,bird3y,frames):
                   display.blit(bird3[frames], (bird3x,bird3y))
                   bird3[frames].set_colorkey((0,0,0))
                    
                    
                bird_starty = random.randrange(100 , 300)
                bird2_starty=random.randrange(0, 300)
                bird3_starty=random.randrange(0,350)
                plane_starty= -200

                bird_startx = 1280
                bird2_startx= 15000
                plane_startx=2500
                bird3_startx=6000

                bird_speed = 10
                bird2_speed=15
                plane_speed=5
                bird3_speed=7

                player_width=65
                bird_width=55
                bird2_width=70
                plane_width=400
                bird3_width=30

                player_height=31
                bird2_height=30
                bird_height=37
                bird3_height=30
                plane_height=120
                acc=0
                scroll=0
                scrolla=0
                game2=True


                while True:
                    if game2 == False:
                        break
                    flyCount+=1
                    
                    if flyCount==48:
                        flyCount=0
                    
                    scroll += 5 +scrolla
                    scrolla+=0.001
                    if scrolla>5:
                        scorlla=5
                    
                    
                    display.blit(bg , (-scroll,-5))
                    
                    if scroll>=12000:
                            display.blit(bg, (15000-scroll,-5))
                    if scroll>=24000:
                            display.blit(bg, (27000-scroll,-5))
                    if scroll>=36000:
                            display.blit(bg, (39000-scroll,-5))
                
                   

                    acc+=scroll//100000
                    if up == True:
                        player_rect.y-=3+acc
                    if down == True:
                        player_rect.y+=3+acc
                    if right==True:
                        player_rect.x+=3
                    if left==True:
                        player_rect.x-=3+acc
                    

                    birds(bird_startx, bird_starty,flyCount//6)
                    bird_startx-=bird_speed + scroll//3000
                    if bird_startx < -bird_width:
                        bird_startx =2080
                        bird_starty = random.randrange(0, 350)
                    bird_rect= pygame.Rect(bird_startx+10,bird_starty , bird_width,bird_height)
                    if player_rect.colliderect(bird_rect):
                            game2=False

                    birds2(bird2_startx, bird2_starty,flyCount//6)
                    bird2_startx-=bird2_speed + scroll//3000
                    if bird2_startx < -bird2_width:
                        bird2_startx =4000
                        bird2_starty = random.randrange(0, 350)
                    bird2_rect= pygame.Rect(bird2_startx+10,bird2_starty , bird2_width,bird2_height)
                    if player_rect.colliderect(bird2_rect):
                            game2=False

                    birds3(bird3_startx, bird3_starty,flyCount//8)
                    bird3_startx-=bird3_speed + scroll//3000
                    if bird3_startx < -bird3_width:
                        bird3_startx =3000
                        bird3_starty = random.randrange(0, 350)
                    bird3_rect= pygame.Rect(bird3_startx+10,bird3_starty , bird3_width,bird3_height)
                    if player_rect.colliderect(bird3_rect):
                            game2=False
                   
                    
                    plane(plane_startx , plane_starty)
                    plane_startx-=plane_speed+scroll//3000
                    if plane_startx < -plane_width:
                        plane_startx =2500
                        plane_starty = random.randrange(0, 300)
                    plane1_rect=pygame.Rect(plane_startx,plane_starty+100,360,70)
                    plane2_rect=pygame.Rect(plane_startx+360,plane_starty,40,130)
                    if player_rect.colliderect(plane1_rect):
                        game2=False
                        
                    if player_rect.colliderect(plane2_rect):
                        game2=False
                    
                    display.blit(player_img,(player_rect.x,player_rect.y))
                    if player_rect.y+player_rect.height>=390:
                        down=False
                        player_rect.y=390-player_rect.height
                    if player_rect.y<=0:
                        up=False
                        player_rect.y=0
                    if player_rect.x<=0:
                        left=False
                        player_rect.x=0
                    if player_rect.x+player_rect.width>1200:
                        right=False
                        player_rect.x=1200-player_rect.width
                    

                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == KEYDOWN:
                            if event.key == K_UP:
                                up = True
                            if event.key == K_DOWN:
                                down = True
                            if event.key == K_RIGHT:
                                right = True
                            if event.key == K_LEFT:
                                left = True
                            
                        if event.type == KEYUP:
                            if event.key == K_UP:
                                up = False
                            if event.key == K_DOWN:
                                down = False
                            if event.key == K_RIGHT:
                                right = False
                            if event.key == K_LEFT:
                                left = False    
                    score(scroll)
                    pygame.display.update()
                    clock.tick(60)
                    gamescore=scroll
        pygame.time.delay(300)
        
        while True:
            if game2==True:
                break
            else:
                scroll+=0.1
                if scroll>12000:
                        scroll=0
                
                display.blit(bglose2 , (-scroll,0))
                message_display("Your Score: {}".format(int(gamescore)) , 60, 600 , 250 , white)
                
                message_display("Press 'r' to retry" , 30 , 600 , 300, white)
                message_display("Press 'm' to go to menu" , 30 , 600 , 350, white)
                message_display1("Game Over" , 100 , 600 , 150 ,(white))
                pygame.display.update()
                
                message_display1("Game Over" , 100 , 600 , 150 ,(240,135,195))
                pygame.display.update()
                message_display1("Game Over" , 100 , 600 , 150 ,(240,135,195))
                pygame.display.update()
                message_display1("Game Over" , 100 , 600 , 150 ,(240,135,195))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_r:
                            game2=True
                            intro=False
                        if event.key==K_m:
                            intro=True
                            game2=True
                            game_intro()
                    
              
    



