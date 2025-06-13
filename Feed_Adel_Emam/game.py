import pygame
from random import randint
#variable initialization
WIDTH=800
HEIGHT=400
Running=True
dt=0
lives=5
score=0
spead=5
playing=True

#init pygame
pygame.init()
pygame.mixer.init()
screan=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("FEED_ADEL_EMAM")
clock=pygame.time.Clock()
screan.fill("silver")


#text initialization 

title_text=pygame.font.SysFont("arial",30)
title_text=title_text.render("Feed Adel Emam",True,"Black")
title_text_rect=title_text.get_rect()
title_text_rect.center=(WIDTH/2,30)



score_font=pygame.font.SysFont("arial",25)
score_text=score_font.render(f"score : {score}",True,"Black")
score_text_rect=score_text.get_rect()
score_text_rect.topleft=(10,10)

lives_font=pygame.font.SysFont("arial",25)
lives_text=lives_font.render(f"lives : {lives}",True,"Black")
lives_text_rect=lives_text.get_rect()
lives_text_rect.topright=(WIDTH-10,10)


game_over_font=pygame.font.SysFont("comicSansMS",50)
game_over_text=game_over_font.render("Game Overrrrrr!",True,"red")
game_over_text_rect=game_over_text.get_rect()
game_over_text_rect.center=(WIDTH/2,HEIGHT/2)


restart_font=pygame.font.SysFont("impact",30)
restart_text=restart_font.render("press p to feed adel emam again ",True,"red")
restart_text_rect=restart_text.get_rect()
restart_text_rect.center=(WIDTH/2,HEIGHT/2+100)
# line 
pygame.draw.line(screan,"black",(0,score_text.get_height()+20),(WIDTH,score_text.get_height()+20))

#bg photo
BG_photo=pygame.image.load("adel_emam.jpeg")
BG_photo = pygame.transform.scale(BG_photo, (WIDTH, HEIGHT-(score_text.get_height()+30)))
BG_photo_rect=BG_photo.get_rect()
BG_photo_rect.center=(WIDTH/2,HEIGHT/2+29)


#adel emam image
adel_emam=pygame.image.load("g3an.jpeg")
adel_emam = pygame.transform.scale(adel_emam, (50,50))
adel_emam_rect=adel_emam.get_rect()
adel_emam_rect.center=(40,HEIGHT/2)

#food image
food_image=pygame.image.load("meat.jpg")
food_image = pygame.transform.scale(food_image, (50,50))
food_image_rect=food_image.get_rect()
food_image_rect.center=(WIDTH-40,HEIGHT/2)

# voices
pygame.mixer.music.load("main.mp3")
music_playing=False
quit_sound=pygame.mixer.Sound("quit.mp3")
quit_sound_on=True

catch_sound=pygame.mixer.Sound("el72.mp3")
hit_sound=pygame.mixer.Sound("hit.mp3")

while Running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            Running=False
    
    keys=pygame.key.get_pressed()
    screan.fill("silver")


    # blit image
    screan.blit(BG_photo,BG_photo_rect)
    screan.blit(adel_emam,adel_emam_rect)
    screan.blit(food_image,food_image_rect)

    # blit texts
    screan.blit(lives_text,lives_text_rect)
    screan.blit(score_text,score_text_rect)
    screan.blit(title_text,title_text_rect)
    

    # adel_emam movement
    if keys[pygame.K_w] and adel_emam_rect.y> score_text.get_height()+30:
        adel_emam_rect.y-=500*dt
    if keys[pygame.K_s] and adel_emam_rect.y< HEIGHT-adel_emam.get_height()-10:
        adel_emam_rect.y+=500 *dt
    
    # meat movement
    if food_image_rect.x-25<0:
        lives-=1
        food_image_rect.center=(WIDTH,randint(score_text.get_height()+40,HEIGHT-adel_emam.get_height()-10))
        lives_text=lives_font.render(f"lives : {lives}",True,"Black")
        if lives:
           catch_sound.play()
           pygame.time.delay(350)
        
        

    else:
        food_image_rect.x-=spead
    
    if adel_emam_rect.colliderect(food_image_rect):
        score+=1
        spead+=.5
        food_image_rect.center=(WIDTH,randint(score_text.get_height()+40,HEIGHT-adel_emam.get_height()-10))
        score_text=score_font.render(f"score : {score}",True,"Black")
        hit_sound.play()
    
    if lives==0:
        screan.blit(game_over_text,game_over_text_rect)
        screan.blit(restart_text,restart_text_rect)
        food_image_rect.center=(WIDTH,10000)
        playing=False
        if quit_sound_on:
            quit_sound.play()
            quit_sound_on=False
    if keys[pygame.K_p]:
        lives=5
        spead=5
        score=0
        score_text=score_font.render(f"score : {score}",True,"Black")
        food_image_rect.center=(WIDTH,randint(score_text.get_height()+40,HEIGHT-adel_emam.get_height()-10))
        lives_text=lives_font.render(f"lives : {lives}",True,"Black")
        playing=True
    if playing and not music_playing:
        pygame.time.delay(500)
        pygame.mixer.music.play(-1)
        music_playing = True

    if not playing and music_playing:
        pygame.mixer.music.stop()
        music_playing = False



    
          
    dt=clock.tick(60)/1000
    pygame.display.flip()


pygame.quit()