import pygame, sys
from fruit import Fruit
from bomb import Bomb
from settings import spawn_bomba
from settings import spawn_fruit
from settings import move
from settings import move_bomb
from settings import numfrutti
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
        screen.blit(settings.barra[i],(250,400))
        pygame.display.flip()
        pygame.time.delay(1200)
        i+=1
        if i==settings.TOTAL_FRAMES:
            stato=False

#funzione schermata iniziale

def schermata_menu():
    run=True
    while run:
        screen.blit(settings.SCHERMATA_MENU,(0,0))
        

        pos = pygame.mouse.get_pos()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if settings.PLAY_RECT.collidepoint(pos):
                    schermata_gameplay()
                if settings.TROFEO_RECT.collidepoint(pos):
                    screen.blit(pygame.transform.scale(settings.NERO_STATS, (500, 300)), (250,150))
                    screen.blit(pygame.transform.scale(settings.X_IMMAGINE, (20, 20)), (730,150))
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
                        screen.blit(pygame.transform.scale(settings.NERO_STATS, (500, 300)), (250, 150))
                        tagliati=numfrutti()
                        testo=font.render(tagliati,True,settings.BLU)
                        testo_rect=testo.get_rect()
                        testo_rect.center=(settings.WINDOW_WIDTH//2,settings.WINDOW_HEIGHT//2)
                        screen.blit(testo,testo_rect)
                        screen.blit(pygame.transform.scale(settings.X_IMMAGINE, (20, 20)), (730, 150))
                        pos = pygame.mouse.get_pos()
                        screen.blit(settings.KATANA, (pos[0] - settings.KATANA.get_width() / 2, pos[1] - settings.KATANA.get_height() / 2))
                        pygame.display.update()          
                        
        if settings.PLAY_RECT.collidepoint(pos):
            screen.blit(pygame.transform.scale(settings.PLAY_BUTTON, (128, 128)), settings.PLAY_RECT_PRESSED.topleft)
        else:
            screen.blit(pygame.transform.scale(settings.PLAY_BUTTON, (110, 110)), settings.PLAY_RECT.topleft)
        if settings.TROFEO_RECT.collidepoint(pos):
            screen.blit(pygame.transform.scale(settings.TROFEO, (65, 65)), (900,35))
        else:
            screen.blit(pygame.transform.scale(settings.TROFEO, (50, 50)), (907,45))
        
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
                          dati=dati.split(":")
                          dati[1]=int(dati[1])
                          da_scrivere=frutti_tagliati+dati[1]
                          with open("progressi.txt","w",encoding="utf-8") as nuovi_progressi:
                              nuovi_progressi.write(f"Frutti tagliati:{da_scrivere}")
                      pygame.time.delay(1400)
                      run=False

            
        
        for i in range(len(fruits)):
            fruit_data = fruits[i]
            x, y, speed_x, speed_y, fruit_image = fruit_data
            x, y, speed_x, speed_y = move(x, y, speed_x, speed_y, fruit_image, screen)
            fruits[i] = [x, y, speed_x, speed_y, fruit_image]
        
        
        for i in range (len(bombe)):
            bomba_data=bombe[i]
            x, y, speed_x, speed_y, bomba_image,rect = bomba_data
            x, y, speed_x, speed_y,rect = move_bomb(x, y, speed_x, speed_y, bomba_image, screen,rect)
            bombe[i] = [x, y, speed_x, speed_y, bomba_image,rect]


        screen.blit(settings.KATANA, (pos[0] - settings.KATANA.get_width() / 2, pos[1] - settings.KATANA.get_height() / 2))
        
        pygame.display.update() 
        clock.tick(settings.FPS)

schermata_caricamento()
pygame.mouse.set_visible(False)
schermata_menu()



pygame.quit()
sys.exit() 