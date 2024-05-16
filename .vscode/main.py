import pygame, sys
import fruit
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
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type==pygame.MOUSEMOTION:
                posizione=pygame.mouse.get_pos()
                if settings.PLAY_RECT.collidepoint(posizione):
                    screen.blit(settings.PLAY_BUTTON,settings.PLAY_RECT_PRESSED)
                    settings.PLAY_BUTTON=pygame.transform.scale(settings.PLAY_BUTTON,(128,128))
                    pygame.display.update()
            
            if event.type==pygame.MOUSEMOTION:
                posizione=pygame.mouse.get_pos()
                if not settings.PLAY_RECT.collidepoint(posizione):
                    screen.blit(settings.PLAY_BUTTON,settings.PLAY_RECT)
                    pygame.display.update()
            
            if event.type==pygame.MOUSEBUTTONDOWN:
                posizione=pygame.mouse.get_pos()
                if settings.PLAY_RECT.collidepoint(posizione):
                    schermata_gameplay()

def schermata_gameplay():
    run = True
    while run:
        screen.blit(settings.SCHERMATA_GAMEPLAY, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pass
    pass


schermata_caricamento()
schermata_menu()



pygame.quit()
sys.exit()
