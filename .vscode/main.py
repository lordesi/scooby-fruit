import pygame, sys
from fruit import Fruit
from bomb import Bomb
from settings import spawn_bomba
from settings import spawn_fruit
from settings import move
from settings import frutti
from settings import scrivi_stats
from settings import scrivi_round
from settings import aggiornare_progressi
from settings import reset_progressi
from settings import scrivi_punteggio
from settings import fruit_images
from settings import bomb_images
import settings
import random
import math
import time

pygame.init()
pygame.font.init()
font=pygame.font.Font("PoetsenOne-Regular.ttf",36)
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
        screen.blit(settings.barra[i],(820,500))
        pygame.display.flip()
        pygame.time.delay(1200)
        i+=1
        if i==settings.TOTAL_FRAMES:
            stato=False

#funzione schermata iniziale XRNTBZP9

def schermata_menu():
    run=True
    angolo=0

    while run:
        screen.blit(settings.SCHERMATA_MENU,(0,0))
        mouse_pressed1 = pygame.mouse.get_pressed()
        

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
                    screen.blit(pygame.transform.scale(settings.STATS_SFONDO, (700, 450)), (150,75))
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
                                if settings.RESET_RECT.collidepoint(pos):
                                    reset_progressi("progressi.txt")
                                    

                        screen.blit(settings.SCHERMATA_MENU, (0, 0))
                        screen.blit(pygame.transform.scale(settings.STATS_SFONDO, (700, 450)), (150, 75))
                        statistiche=frutti()
                        scrivi_stats(statistiche)

                        pos = pygame.mouse.get_pos()
                        if mouse_pressed1[0]:
                            screen.blit(settings.KATANA_PRESSED, (pos[0] - settings.KATANA_PRESSED.get_width() / 2, pos[1] - settings.KATANA_PRESSED.get_height() / 2))
                        else:
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
    frutti_mancati_lista = []
    scia = []
    spawn_timer = 0
    spawn_delay = 60
    spawn_timer_bomba=0
    spawn_delay_bomba=240
    frutti_tagliati=0
    frutti_mancati=0
    max_frutti_mancati = 3
    lista_tempi = [30, 60, 90, 120]
 


    while run:
        screen.blit(settings.SCHERMATA_GAMEPLAY, (0,0))
        pos = pygame.mouse.get_pos()
        mouse_premuto=pygame.mouse.get_pressed()

        scrivi_punteggio(frutti_tagliati)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        current_time_ms = pygame.time.get_ticks()
        current_time_s = current_time_ms // 1000

        if lista_tempi and current_time_s >= lista_tempi[0]:
            lista_tempi.pop(0)
            spawn_delay -= 7
        
        
        
        spawn_timer += 1
        if spawn_timer >= spawn_delay:
            spawn_timer = 0
            fruits.append(spawn_fruit())
        spawn_timer_bomba+=1
        if spawn_timer_bomba>= spawn_delay_bomba:
            spawn_timer_bomba=0
            bombe.append(spawn_bomba())
        
        tempo_corrente=pygame.time.get_ticks()
        frutti_mancati_lista=[x for x in frutti_mancati_lista if tempo_corrente-x[1]<2000]

            
        if fruits:
            for i in range(len(fruits) -1, -1, -1):
                fruit_data = fruits[i]
                x, y, speed_x, speed_y,g,start, fruit_image,angolo = fruit_data
                x, y, speed_x, speed_y,g ,start = move(x, y, speed_x, speed_y,g, start)
                fruit_image.rect.topleft=(x,y)
                angolo+=3
                immagine_ruotata = pygame.transform.rotate(fruit_image.image, angolo)
                rect_ruotato = immagine_ruotata.get_rect(center=fruit_image.rect.center)
                if y > screen.get_height():
                    pos_frutto=fruit_image.rect.topleft
                    fruits.pop(i)
                    frutti_mancati_lista.append((pos_frutto,pygame.time.get_ticks()))
                    screen.blit(settings.X_FRUTTO_MANCATO,(pos_frutto[0]-35,settings.WINDOW_HEIGHT-100))
                    frutti_mancati += 1
                    if frutti_mancati >= max_frutti_mancati:
                        screen.blit(settings.GAME_OVER,(0,0))
                        pygame.display.flip()
                        #aggiornare_progressi("progressi.txt", frutti_tagliati)
                        pygame.time.delay(1400)
                        run=False
                else:
                    screen.blit(immagine_ruotata,rect_ruotato.topleft)
                    fruits[i] = [x, y, speed_x, speed_y, g, start, fruit_image, angolo]
        
        if bombe:
            for i in range(len(bombe)):
                bomba_data = bombe[i]
                x, y, speed_x, speed_y, g, start, bomba_image, rect, angolo = bomba_data
                x, y, speed_x, speed_y, g, start = move(x, y, speed_x, speed_y, g, start)
                rect.topleft=(x,y)
                angolo += 3
                immagine_ruotata = pygame.transform.rotate(bomba_image.image, angolo)
                rect_ruotato = immagine_ruotata.get_rect(center=rect.center)
                screen.blit(immagine_ruotata, rect_ruotato.topleft)
                bombe[i] = [x, y, speed_x, speed_y, g, start, bomba_image, rect, angolo]
        

        for posizione,tempo in frutti_mancati_lista:
            screen.blit(settings.X_FRUTTO_MANCATO,(posizione[0]-35,settings.WINDOW_HEIGHT-60))
        
        for i in range(max_frutti_mancati):
            if i < frutti_mancati:
                screen.blit(settings.CUORE_GRIGIO, settings.POSIZIONI_CUORE[i])
            else:
                screen.blit(settings.CUORE_ROSSO, settings.POSIZIONI_CUORE[i])
        if settings.RETURN_HOME_RECT.collidepoint(pos):
            screen.blit(pygame.transform.scale(settings.RETURN_HOME, (settings.RETURN_HOME.get_width()* 1.1, settings.RETURN_HOME.get_height()*1.1)), (23,23))
        else:
            screen.blit(settings.RETURN_HOME, (30,30))

        if mouse_premuto[0]:
            screen.blit(settings.KATANA_PRESSED, (pos[0] - settings.KATANA_PRESSED.get_width() / 2, pos[1] - settings.KATANA_PRESSED.get_height() / 2))
            if settings.QUIT_PARTITA_RECT.collidepoint(pos):
                run=False
            
            for fruit in fruits[:]:
                if fruit[6].rect.collidepoint(pos):
                    fruits.remove(fruit)
                    frutti_tagliati+=1

            for bomb in bombe[:]:
                 if bomb[7].collidepoint(pos):
                      bombe.remove(bomb)
                      screen.blit(settings.GAME_OVER,(0,0))
                      pygame.display.flip()
                      #aggiornare_progressi("progressi.txt", frutti_tagliati)
                      pygame.time.delay(1400)
                      run=False
        else:
            screen.blit(settings.KATANA, (pos[0] - settings.KATANA.get_width() / 2, pos[1] - settings.KATANA.get_height() / 2))
        
        pygame.display.update() 
        clock.tick(settings.FPS)


schermata_caricamento()
pygame.mouse.set_visible(False)
schermata_menu()



pygame.quit()
sys.exit() 