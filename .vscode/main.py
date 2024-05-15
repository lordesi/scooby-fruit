import pygame, sys
import fruit
import settings

pygame.init()

#definisco la schermata di avvio - demo

screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
pygame.display.set_caption("Scooby Fruit")


#definisco la base per il framerate

clock = pygame.time.Clock()
#sfondo caricamento
immagine_caricamento=pygame.image.load("schermata-iniziale.png")
immagine_caricamento=pygame.transform.scale(immagine_caricamento,(settings.WINDOW_WIDTH,settings.WINDOW_HEIGHT))
#barra di caricament0
barra=[]
frame=pygame.image.load("25.jpeg")
frame=pygame.transform.scale(frame,(500,40))
barra.append(frame)
frame=pygame.image.load("50.jpeg")
frame=pygame.transform.scale(frame,(500,40))
barra.append(frame)
frame=pygame.image.load("75.jpeg")
frame=pygame.transform.scale(frame,(500,40))
barra.append(frame)
frame=pygame.image.load("100.jpeg")
frame=pygame.transform.scale(frame,(500,40))
barra.append(frame)

def schermata_caricamento():
    stato=True
    i=0
    while stato:
        screen.blit(immagine_caricamento,(0,0))
        screen.blit(barra[i],(250,500))
        pygame.display.flip()
        pygame.time.delay(1200)
        i+=1
        if i==4:
            stato=False

schermata_caricamento()

#Loop principale del gioco (eventi) - demo

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    


    pygame.display.flip()
    clock.tick(settings.FPS)

pygame.quit()
sys.exit()
