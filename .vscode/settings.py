import pygame
pygame.init()

#definisco parametri base - demo

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
FPS = 60


#definisco display -demo

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

#definisco colori - demo

BIANCO = (255,255,255)
NERO = (0,0,0)
ROSSO = (255,0,0)
BLU = (0,0,255)
VERDE = (0,255,0)

# definisco bg delle schermate -demo


SCHERMATA_CARICAMENTO = pygame.image.load("schermata-iniziale.png")
SCHERMATA_CARICAMENTO = pygame.transform.scale(SCHERMATA_CARICAMENTO,(WINDOW_WIDTH,WINDOW_HEIGHT))

SCHERMATA_MENU = pygame.image.load("schermata-menu.png")
SCHERMATA_MENU=pygame.transform.scale(SCHERMATA_MENU,(WINDOW_WIDTH,WINDOW_HEIGHT))



#definisco lista barra di caricamento -demo

barra = []
for percentuale in [25,50,75]:
    frame = pygame.image.load(f"barra-caricamento/{percentuale}.png")
    frame = pygame.transform.scale(frame, (frame.get_width() * 0.4, frame.get_height() * 0.4))
    barra.append(frame)

#definisco costanti barra -demo

POSIZIONE_BARRA = (250, 500)
DELAY = 1200
TOTAL_FRAMES = len(barra)

#definisco pulsante -demo

PLAY_BUTTON = pygame.image.load("play - button.png").convert_alpha()
PLAY_BUTTON = pygame.transform.scale(PLAY_BUTTON,(110,110))


#definisco rect button -demo

PLAY_RECT = pygame.Rect(WINDOW_WIDTH/2 - 55, WINDOW_HEIGHT/2+100 - 25, 110, 110)
PLAY_RECT_PRESSED = pygame.Rect(WINDOW_WIDTH/2 - 64, WINDOW_HEIGHT/2+91 - 25, 128, 128)

#definisco schermata gameplay -demo

SCHERMATA_GAMEPLAY = pygame.image.load("schermata-gameplay.jpg")
SCHERMATA_GAMEPLAY = pygame.transform.scale(SCHERMATA_GAMEPLAY, (WINDOW_WIDTH, WINDOW_HEIGHT))

#definisco katana -demo

KATANA = pygame.image.load("katana.png").convert_alpha()
KATANA = pygame.transform.scale(KATANA, (KATANA.get_width() * 0.2, KATANA.get_height() * 0.2))
KATANA_RECT = KATANA.get_rect()

#definisco trofeo
#TROFEO_RECT=pygame.Rect(WINDOW_WIDTH-70, 70 , 50, 50)
TROFEO_RECT=pygame.Rect(WINDOW_WIDTH-100, WINDOW_HEIGHT-565 , 65, 65)
TROFEO = pygame.image.load("trofeo.png")
#TROFEO=pygame.transform.scale(TROFEO,(50,50))

STATS_RECT=pygame.Rect(WINDOW_WIDTH-500,WINDOW_HEIGHT-450,500,300)
NERO_STATS=pygame.image.load("nero.png")
X_RECT=pygame.Rect(730,150,20,20)
X_IMMAGINE=pygame.image.load("x.png")


