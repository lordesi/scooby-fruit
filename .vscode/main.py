import pygame, sys
import fruit
import settings

pygame.init()

#definisco la schermata di avvio - demo

screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
pygame.display.set_caption("Scooby Fruit")


#definisco la base per il framerate

clock = pygame.time.Clock()


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
