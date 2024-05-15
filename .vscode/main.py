import pygame, sys
import fruit
import settings

bianco=(255,255,255)
nero=(0,0,0)
rosso=(255,0,0)
blu=(0,0,255)
verde=(0,255,0)

pygame.init()

#definisco la schermata di avvio - demo

screen = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
pygame.display.set_caption("Scooby Fruit")


#definisco la base per il framerate

clock = pygame.time.Clock()
#sfondo caricamento
immagine_caricamento=pygame.image.load("schermata-iniziale.png")
immagine_caricamento=pygame.transform.scale(immagine_caricamento,(settings.WINDOW_WIDTH,settings.WINDOW_HEIGHT))
#barra di caricamento
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

#Rect e immagine per schermata iniziale
play_rect = pygame.Rect(settings.WINDOW_WIDTH/2 - 55, settings.WINDOW_HEIGHT/2+100 - 25, 110, 110)
play_rect_schiacciato = pygame.Rect(settings.WINDOW_WIDTH/2 - 64, settings.WINDOW_HEIGHT/2+100 - 25, 128, 128)
pulsante_gioca=pygame.image.load("anguria pulsante.jpg")
pulsante_gioca=pygame.transform.scale(pulsante_gioca,(110,110))
pulsante_gioca_cliccato=pygame.transform.scale(pulsante_gioca,(128,128))

#funzione schermata iniziale
def schermata_iniziale():
    inizio=True
    while inizio:
        screen.fill(bianco)
        font=pygame.font.SysFont('arial',40)
        titolo=font.render('Scooby fruit',True,(0,100,0))
        screen.blit(titolo, (settings.WINDOW_WIDTH/2 - titolo.get_width()/2, settings.WINDOW_HEIGHT/4 - titolo.get_height()/2))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inizio = False

            if event.type==pygame.MOUSEMOTION:
                posizione=pygame.mouse.get_pos()
                if play_rect.collidepoint(posizione):
                    screen.blit(pulsante_gioca_cliccato,play_rect_schiacciato)
                    #pulsante_gioca=pygame.transform.scale(pulsante_gioca,(128,128))
                    pygame.display.update()
            
            if event.type==pygame.MOUSEMOTION:
                posizione=pygame.mouse.get_pos()
                if not play_rect.collidepoint(posizione):
                    screen.blit(pulsante_gioca,play_rect)
                    pygame.display.update()
            
            if event.type==pygame.MOUSEBUTTONDOWN:
                posizione=pygame.mouse.get_pos()
                if play_rect.collidepoint(posizione):
                    inizio=False
        

schermata_caricamento()
schermata_iniziale()

#Loop principale del gioco (eventi) - demo

#running = True

#while running:

    #for event in pygame.event.get():
        #if event.type == pygame.QUIT:
            #running = False
            
    


    #pygame.display.flip()
    #clock.tick(settings.FPS)

pygame.quit()
sys.exit()
