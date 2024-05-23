import pygame, sys
from fruit import Fruit
from bomb import Bomb
from settings import spawn_bomba
from settings import spawn_fruit
from settings import move
from settings import move_bomb
from settings import frutti
from settings import fruit_images
from settings import bomb_images
import settings
import random
import math

pygame.init()
pygame.font.init()
font=pygame.font.Font(None,36)

#definisco la schermata di avvio - demo

screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
pygame.display.set_caption("Scooby Fruit")

#definisco la base per il framerate

clock = pygame.time.Clock()

def schermata_caricamento():
    stato=True
    i=0
    while stato:
        screen.blit(settings.SCHERMATA_CARICAMENTO,(0,0))
        screen.blit(settings.barra[i],(175,350))
        pygame.display.flip()
        pygame.time.delay(1200)
        i+=1
        if i==settings.TOTAL_FRAMES:
            stato=False

#funzione schermata iniziale

def schermata_menu():
    run=True
    angolo=0

    while run:
        screen.blit(settings.SCHERMATA_MENU,(0,0))
        

        pos = pygame.mouse.get_pos()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if settings.PLAY_RECT.collidepoint(pos):
                    schermata_gameplay()
                if settings.QUIT_RECT.collidepoint(pos):
                    run=False
                if settings.TROFEO_RECT.collidepoint(pos):
                    screen.blit(pygame.transform.scale(settings.STATS_SFONDO, (500, 300)), (250,150))
                    screen.blit(pygame.transform.scale(settings.X_IMMAGINE, (40, 40)), (715,148))
                    screen.blit(settings.KATANA, (pos[0] - settings.KATANA.get_width() / 2, pos[1] - settings.KATANA.get_height() / 2))
                    pygame.display.update()
                    stats=True
                    while stats:
                        for event in pygame.event.get():
                            if event.type==pygame.QUIT:
                                run = False
                                stats=False
                            elif event.type==pygame.MOUSEBUTTONDOWN:
                                pos = pygame.mouse.get_pos()
                                if settings.X_RECT.collidepoint(pos):
                                    stats=False
                        screen.blit(settings.SCHERMATA_MENU, (0, 0))
                        screen.blit(pygame.transform.scale(settings.STATS_SFONDO, (500, 300)), (250, 150))

                        statistiche=frutti()
                        testo=font.render(statistiche[0],True,settings.BLU)
                        testo_rect=testo.get_rect()
                        testo_rect.center=(settings.WINDOW_WIDTH//2,settings.WINDOW_HEIGHT//2+20)
                        screen.blit(testo,testo_rect)
                        testo2=font.render(statistiche[1],True,settings.BLU)
                        testo_rect2=testo2.get_rect()
                        testo_rect2.center=(settings.WINDOW_WIDTH//2,settings.WINDOW_HEIGHT//2-20)
                        screen.blit(testo2,testo_rect2)

                        screen.blit(pygame.transform.scale(settings.X_IMMAGINE, (40, 40)), (715, 148))
                        pos = pygame.mouse.get_pos()
                        screen.blit(settings.KATANA, (pos[0] - settings.KATANA.get_width() / 2, pos[1] - settings.KATANA.get_height() / 2))
                        pygame.display.update()          
        angolo+=1

        play_ruotato=pygame.transform.rotate(settings.PLAY_BUTTON,angolo)
        play_ruotato=pygame.transform.scale(play_ruotato,(128,128))
        rect_ruotato=play_ruotato.get_rect(center=settings.PLAY_RECT.center)
        screen.blit(play_ruotato,rect_ruotato.topleft)
        
            

        
        
        if settings.TROFEO_RECT.collidepoint(pos):
            screen.blit(pygame.transform.scale(settings.TROFEO, (65, 65)), (900,35))
        else:
            screen.blit(pygame.transform.scale(settings.TROFEO, (50, 50)), (907,45))
        
        if settings.QUIT_RECT.collidepoint(pos):
            screen.blit(pygame.transform.scale(settings.QUIT_IMMAGINE, (65, 65)), (900,495))
        else:
            screen.blit(pygame.transform.scale(settings.QUIT_IMMAGINE, (50, 50)), (907,505))
        
        screen.blit(settings.KATANA, (pos[0] - settings.KATANA.get_width() / 2, pos[1] - settings.KATANA.get_height() / 2))
        
        pygame.display.update()
        clock.tick(settings.FPS)

def schermata_gameplay():
    run = True
    fruits = []
    bombe = []
    spawn_timer = 0
    spawn_delay = 60
    spawn_timer_bomba=0
    spawn_delay_bomba=240
    frutti_tagliati=0


    while run:
        screen.blit(settings.SCHERMATA_GAMEPLAY, (0,0))
        pos = pygame.mouse.get_pos()
        mouse_premuto=pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        spawn_timer += 1
        if spawn_timer >= spawn_delay:
            spawn_timer = 0
            fruits.append(spawn_fruit())
        spawn_timer_bomba+=1
        if spawn_timer_bomba>= spawn_delay_bomba:
            spawn_timer_bomba=0
            bombe.append(spawn_bomba())

        if mouse_premuto[0]:
            for fruit in fruits[:]:
                if fruit[4].rect.collidepoint(pos):
                    fruits.remove(fruit)
                    frutti_tagliati+=1

            for bomb in bombe[:]:
                 if bomb[5].collidepoint(pos):
                      bombe.remove(bomb)
                      screen.blit(settings.GAME_OVER,(0,0))
                      pygame.display.flip()
                      with open ("progressi.txt","r",encoding="utf-8") as f:
                          dati=f.read()
                          dati=dati.split("\n")
                          dati=[el.split(":") for el in dati]
                          record=int(dati[1][1])
                          if frutti_tagliati>record:
                              record=frutti_tagliati
                          dati[0][1]=int(dati[0][1])
                          da_scrivere=frutti_tagliati+dati[0][1]
                          with open("progressi.txt","w",encoding="utf-8") as nuovi_progressi:
                              nuovi_progressi.write(f"Frutti tagliati:{da_scrivere}\nRecord frutti tagliati in un match:{record}")
                      pygame.time.delay(1400)
                      run=False

            
        
        for i in range(len(fruits)):
            fruit_data = fruits[i]
            x, y, speed_x, speed_y, fruit_image,angolo = fruit_data
            x, y, speed_x, speed_y,angolo = move(x, y, speed_x, speed_y, fruit_image, angolo,screen)
            fruits[i] = [x, y, speed_x, speed_y, fruit_image,angolo]
        
        
        for i in range (len(bombe)):
            bomba_data=bombe[i]
            x, y, speed_x, speed_y, bomba_image,rect,angolo = bomba_data
            x, y, speed_x, speed_y,rect,angolo = move_bomb(x, y, speed_x, speed_y, bomba_image, screen,rect,angolo)
            bombe[i] = [x, y, speed_x, speed_y, bomba_image,rect,angolo]


        screen.blit(settings.KATANA, (pos[0] - settings.KATANA.get_width() / 2, pos[1] - settings.KATANA.get_height() / 2))
        
        pygame.display.update() 
        clock.tick(settings.FPS)

schermata_caricamento()
pygame.mouse.set_visible(False)
schermata_menu()



pygame.quit()
sys.exit() 