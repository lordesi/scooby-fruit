import pygame, sys
from fruit import Fruit
from bomb import Bomb
from settings import fruit_images
from settings import bomb_images
import settings
import random
import math




pygame.init()

#definisco la schermata di avvio - demo

screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
pygame.display.set_caption("Scooby Fruit")

#definisco la base per il framerate

clock = pygame.time.Clock()

fruit_images = {

    "kiwi" : Fruit("Scooby Game Graphics\Fruits\Kiwi_Fruit.png"),
    "lemon" : Fruit("Scooby Game Graphics\Fruits\Lemon.png"),
    "lime" : Fruit("Scooby Game Graphics\Fruits\Lime.png"),
    "mango" : Fruit("Scooby Game Graphics\Fruits\Mango.png"),
    "orange" : Fruit("Scooby Game Graphics\Fruits\Orange.png"),
    "passion_fruit" : Fruit("Scooby Game Graphics\Fruits\Passionfruit.png"),
    "peach" : Fruit("Scooby Game Graphics\Fruits\Peach.png"),
    "pear" : Fruit("Scooby Game Graphics\Fruits\Pear.png"),
    "pineapple" : Fruit("Scooby Game Graphics\Fruits\Pineapple.png"),
    "plum" : Fruit("Scooby Game Graphics\Fruits\Plum.png"),
    "red_apple" : Fruit("Scooby Game Graphics\Fruits\Red_Apple.png"),
    "strawberry" : Fruit("Scooby Game Graphics\Fruits\Strawberry.png"),
    "tomato" : Fruit("Scooby Game Graphics\Fruits\Tomato.png"),
    "watermelon" : Fruit("Scooby Game Graphics\Fruits\Watermelon.png")

}


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
    x = random.randint(0, settings.WINDOW_WIDTH - fruit_images["kiwi"].rect.width)
    y = settings.WINDOW_HEIGHT - fruit_images["kiwi"].rect.height
    speed_x = random.uniform(-1.5, 1.5)
    speed_y = -random.uniform(2,3)
    while run:
        screen.blit(settings.SCHERMATA_GAMEPLAY, (0,0))
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        x += speed_x
        y += speed_y
        if y < settings.WINDOW_HEIGHT / 2:
            speed_y += settings.GRAVITY
        if x < -settings.RADIUS:
            x = settings.WINDOW_WIDTH + settings.RADIUS
            speed_x = random.uniform(-1.5, 1.5)
            speed_y = -random.uniform(2,3)
        elif x > settings.WINDOW_WIDTH + settings.RADIUS:
            x = -settings.RADIUS
            speed_x = random.uniform(-1.5, 1.5)
            speed_y = -random.uniform(2,3)
        
        fruit_images["kiwi"].blit_fruit(screen, x, y)
        bomb_images["bomb"].blit_bomb(screen, x, y)
        screen.blit(settings.KATANA, (pos[0] - settings.KATANA.get_width() / 2, pos[1] - settings.KATANA.get_height() / 2))
        if y > settings.WINDOW_HEIGHT:
            run = False
        
        pygame.display.update() 
        clock.tick(settings.FPS)

schermata_caricamento()
pygame.mouse.set_visible(False)
schermata_menu()



pygame.quit()
sys.exit()
