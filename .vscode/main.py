import pygame, sys
from fruit import Fruit
import settings



pygame.init()

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

        if settings.PLAY_RECT.collidepoint(pos):
            screen.blit(pygame.transform.scale(settings.PLAY_BUTTON, (128, 128)), settings.PLAY_RECT_PRESSED.topleft)
        else:
            screen.blit(pygame.transform.scale(settings.PLAY_BUTTON, (110, 110)), settings.PLAY_RECT.topleft)

        screen.blit(settings.KATANA, (pos[0] - settings.KATANA.get_width() / 2, pos[1] - settings.KATANA.get_height() / 2))

        pygame.display.update()
        clock.tick(settings.FPS)
def schermata_gameplay():
    run = True
    while run:
        screen.blit(settings.SCHERMATA_GAMEPLAY, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update() 
        clock.tick(settings.FPS)

schermata_caricamento()
pygame.mouse.set_visible(False)
schermata_menu()



pygame.quit()
sys.exit()
