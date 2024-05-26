import pygame
import random
from fruit import Fruit
from bomb import Bomb
pygame.init()
font=pygame.font.Font("PoetsenOne-Regular.ttf",36)
#definisco parametri base - demo

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
FPS = 60
TRAIL_LIFETIME = 10000
RADIUS_TRAIL = 10



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

#definisco funzioni spawn frutti e bombe
def spawn_fruit():
    fruit_name = random.choice(list(fruit_images.keys()))
    fruit_image = fruit_images[fruit_name]
    x = random.randint(0, WINDOW_WIDTH - fruit_image.rect.width)
    y = WINDOW_HEIGHT
    speed_x = random.randint(1, 2)
    if x>=500:
         speed_x*=-1
    speed_y = random.randint(-10, -7)
    fruit_image.rect.topleft = (x, y)
    angolo_rotazione = random.randint(0, 360)
    return [x, y, speed_x, speed_y, 8, pygame.time.get_ticks(), fruit_image, angolo_rotazione]  

def spawn_bomba():
    bomba_image = bomb_images["bomb"]
    x = random.randint(0, WINDOW_WIDTH - bomba_image.rect.width)
    y = WINDOW_HEIGHT
    speed_x = random.randint(1, 2)
    if x>=500:
         speed_x*=-1
    speed_y = random.randint(-10, -7)
    bomba_rect = pygame.Rect(x, y, bomba_image.rect.width, bomba_image.rect.height)
    angolo_rotazione = random.randint(0, 360)
    return [x, y, speed_x, speed_y, 8, pygame.time.get_ticks(), bomba_image, bomba_rect, angolo_rotazione] 

def move(x0, y0, vel_x, vel_y, g, start):
    tempo=pygame.time.get_ticks()
    t =(tempo-start)/1000
    x = x0 + vel_x * t
    y = y0 + vel_y * t + 0.5 * g * t * t
    return [x, y, vel_x, vel_y, g, start]

#definisco funzione per ottenere frutti tagliati
def frutti():
      with open("progressi.txt","r",encoding="utf-8") as f:
            dati=f.read()
            dati=dati.split("\n")
            dati=[el.split(":") for el in dati]
            tagliati=dati[0][1]
            record=dati[1][1]
            bombe=dati[2][1]
            return [tagliati,record,bombe]

def scrivi_stats(lista):
        
        record=font.render(lista[1],True,BIANCO)
        record_rect=record.get_rect()
        record_rect.center=(605,175)
        screen.blit(record,record_rect)
        frutti=font.render(lista[0],True,BIANCO)
        frutti_rect=frutti.get_rect()
        frutti_rect.center=(WINDOW_WIDTH//2,330)
        screen.blit(frutti,frutti_rect)
        bombe=font.render(lista[2],True,BIANCO)
        bombe_rect=bombe.get_rect()
        bombe_rect.center=(WINDOW_WIDTH//2+210,330)
        screen.blit(bombe,bombe_rect)

def aggiornare_progressi(file_path, frutti_tagliati):
    with open(file_path, "r", encoding="utf-8") as f:
        dati = f.read().split("\n")
        dati=[el.split(":") for el in dati]
    frutti_tagliati_totali = int(dati[0][1])
    record = int(dati[1][1])
    bomba = int(dati[2][1]) + 1
    if frutti_tagliati > record:
          record = frutti_tagliati
    frutti_tagliati_totali += frutti_tagliati
    with open(file_path, "w", encoding="utf-8") as nuovi_progressi:
          nuovi_progressi.write(f"Frutti tagliati:{frutti_tagliati_totali}\nRecord frutti tagliati in un match:{record}\nBombe esplose:{bomba}")

def reset_progressi(file_path):
      with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"Frutti tagliati:0\nRecord frutti tagliati in un match:0\nBombe esplose:0")


#definisco barra
barra = []
for percentuale in [25,50,75,100]:
    frame = pygame.image.load(f"barra-caricamento/{percentuale}.png")
    frame = pygame.transform.scale(frame, (140 ,80))
    barra.append(frame)

#definisco costanti barra -demo

POSIZIONE_BARRA = (200, 450)
DELAY = 1200
TOTAL_FRAMES = len(barra)

#definisco pulsante -demo

PLAY_BUTTON = pygame.image.load("Scooby Game Graphics/play - button.png").convert_alpha()
PLAY_RECT=PLAY_BUTTON.get_rect(center=(WINDOW_WIDTH//2,WINDOW_HEIGHT//2+170))
#definisco schermata gameplay -demo

SCHERMATA_GAMEPLAY = pygame.image.load("schermata-gameplay.jpg")
SCHERMATA_GAMEPLAY = pygame.transform.scale(SCHERMATA_GAMEPLAY, (WINDOW_WIDTH, WINDOW_HEIGHT))

#definisco katana -demo

KATANA = pygame.image.load("Scooby Game Graphics/katana.png").convert_alpha()
KATANA = pygame.transform.scale(KATANA, (KATANA.get_width() * 0.2, KATANA.get_height() * 0.2))
KATANA_RECT = KATANA.get_rect()

#definisco trofeo
#TROFEO_RECT=pygame.Rect(WINDOW_WIDTH-70, 70 , 50, 50)
TROFEO_RECT=pygame.Rect(WINDOW_WIDTH-100, WINDOW_HEIGHT-565 , 65, 65)
TROFEO = pygame.image.load("Scooby Game Graphics/trofeo.png")
#TROFEO=pygame.transform.scale(TROFEO,(50,50))

STATS_RECT=pygame.Rect(WINDOW_WIDTH-500,WINDOW_HEIGHT-450,500,300)
STATS_SFONDO=pygame.image.load("Scooby Game Graphics/sfondo_nuovo.png")
X_RECT=pygame.Rect(150,75,74,68)
X_IMMAGINE=pygame.image.load("Scooby Game Graphics/x.png")
RESET_RECT=pygame.Rect(507,423,195,45)


QUIT_IMMAGINE=pygame.image.load("Scooby Game Graphics/x.png")
QUIT_RECT=pygame.Rect(907,505,50,50)
QUIT_PARTITA_RECT=pygame.Rect(41,41,50,50)
#definisco return home -demo


RETURN_HOME = pygame.image.load("Scooby Game Graphics/return-home.png").convert_alpha()
RETURN_HOME = pygame.transform.scale(RETURN_HOME, (RETURN_HOME.get_width()* 0.2, RETURN_HOME.get_height()*0.2))
RETURN_HOME_RECT = RETURN_HOME.get_rect()

X_FRUTTO_MANCATO=pygame.image.load("x_frutto_mancato.png")
X_FRUTTO_MANCATO=pygame.transform.scale(X_FRUTTO_MANCATO,(70,70))


#definisco velocità e misure frutta -demo

RADIUS = 20
GRAVITY = 0.05

#definisco fruit e bomba

fruit_images = {

    "kiwi" : Fruit("Scooby Game Graphics/Fruits/Kiwi_Fruit.png"),
    "lemon" : Fruit("Scooby Game Graphics/Fruits/Lemon.png"),
    "lime" : Fruit("Scooby Game Graphics/Fruits/Lime.png"),
    "mango" : Fruit("Scooby Game Graphics/Fruits/Mango.png"),
    "orange" : Fruit("Scooby Game Graphics/Fruits/Orange.png"),
    "passion_fruit" : Fruit("Scooby Game Graphics/Fruits/Passionfruit.png"),
    "peach" : Fruit("Scooby Game Graphics/Fruits/Peach.png"),
    "pear" : Fruit("Scooby Game Graphics/Fruits/Pear.png"),
    "pineapple" : Fruit("Scooby Game Graphics/Fruits/Pineapple.png"),
    "plum" : Fruit("Scooby Game Graphics/Fruits/Plum.png"),
    "red_apple" : Fruit("Scooby Game Graphics/Fruits/Red_Apple.png"),
    "strawberry" : Fruit("Scooby Game Graphics/Fruits/Strawberry.png"),
    "tomato" : Fruit("Scooby Game Graphics/Fruits/Tomato.png"),
    "watermelon" : Fruit("Scooby Game Graphics/Fruits/Watermelon.png")

}

bomb_images = {
    "bomb" : Bomb("Scooby Game Graphics/Fruits/bomb.png")
}

#definisco cuore -demo

CUORE_ROSSO = pygame.image.load("Scooby Game Graphics/Fruits/cuore rosso.png")
CUORE_ROSSO = pygame.transform.scale(CUORE_ROSSO, (CUORE_ROSSO.get_width()* 0.1, CUORE_ROSSO.get_height()*0.1))
CUOREROSSO_RECT = CUORE_ROSSO.get_rect()

CUORE_GRIGIO = pygame.image.load("Scooby Game Graphics/Fruits/cuore grigio.png")
CUORE_GRIGIO = pygame.transform.scale(CUORE_GRIGIO, (CUORE_GRIGIO.get_width()* 0.1, CUORE_GRIGIO.get_height()*0.1))
CUOREGRIGIO_RECT = CUORE_GRIGIO.get_rect()

POSIZIONI_CUORE = [(900, 35), (830, 35), (760, 35)]


#Game over
GAME_OVER = pygame.image.load("Scooby Game Graphics/game_over.jpg")
GAME_OVER = pygame.transform.scale(GAME_OVER, (WINDOW_WIDTH,WINDOW_HEIGHT))

#Prova scia cursore premuto
SCIA=pygame.image.load("scia.png")
SCIA=pygame.transform.scale(SCIA,(50,50))