import pygame
import random
from fruit import Fruit
from bomb import Bomb
pygame.init()

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
    speed_x = random.uniform(-1.5, 1.5)
    speed_y = -random.uniform(2,3)
    fruit_image.rect.topleft=(x,y)
    angolo_rotazione=random.uniform(0,360)
    return [x, y, speed_x, speed_y, fruit_image,angolo_rotazione]

def spawn_bomba():
    bomba_image=bomb_images["bomb"]
    x=random.randint(0,WINDOW_WIDTH - bomba_image.rect.width)
    y=WINDOW_HEIGHT
    speed_x=random.uniform(-1.5,1.5)
    speed_y=random.uniform(2,3)
    bomba_rect=pygame.Rect(x,y,bomba_image.rect.width,bomba_image.rect.height)
    angolo_rotazione=random.uniform(0,360)
    return [x, y, speed_x, speed_y, bomba_image,bomba_rect,angolo_rotazione]

def move(x, y, speed_x, speed_y, fruit_image, angolo_rotazione,screen):
    x += speed_x
    y += speed_y
    if y < WINDOW_HEIGHT / 2:
            speed_y += GRAVITY
    if x < -RADIUS:
            x = WINDOW_WIDTH + RADIUS
            speed_x = random.uniform(-1.5, 1.5)
            speed_y = -random.uniform(2,3)
    elif x > WINDOW_WIDTH + RADIUS:
            x = -RADIUS
            speed_x = random.uniform(-1.5, 1.5)
            speed_y = -random.uniform(2,3)
    fruit_image.rect.topleft=(x,y)
    angolo_rotazione+=3
    immagine_ruotata=pygame.transform.rotate(fruit_image.image,angolo_rotazione)
    rect_ruotato=immagine_ruotata.get_rect(center=fruit_image.rect.center)
    screen.blit(immagine_ruotata, rect_ruotato.topleft)
    return x, y, speed_x, speed_y,angolo_rotazione

def move_bomb(x, y, speed_x, speed_y, bomba_image, screen,rect,angolo_rotazione):
    x += speed_x
    y += speed_y
    if y < WINDOW_HEIGHT / 2:
            speed_y += GRAVITY
    if x < -RADIUS:
            x = WINDOW_WIDTH + RADIUS
            speed_x = random.uniform(-1.5, 1.5)
            speed_y = -random.uniform(2,3)
    elif x > WINDOW_WIDTH + RADIUS:
            x = -RADIUS
            speed_x = random.uniform(-1.5, 1.5)
            speed_y = -random.uniform(2,3)
    rect=pygame.Rect(x,y,bomba_image.rect.width,bomba_image.rect.height)
    angolo_rotazione+=3
    immagine_ruotata=pygame.transform.rotate(bomba_image.image,angolo_rotazione)
    rect_ruotato=immagine_ruotata.get_rect(center=rect.center)
    screen.blit(immagine_ruotata, rect_ruotato.topleft)
    return x, y, speed_x, speed_y, rect,angolo_rotazione

#definisco funzione per ottenere frutti tagliati
def frutti():
      with open("progressi.txt","r",encoding="utf-8") as f:
            dati=f.read()
            dati=dati.split("\n")
            tagliati=dati[0]
            record=dati[1]
            return [tagliati,record]

#definisco lista barra di caricamento -demo

barra = []
for percentuale in [25,50,75]:
    frame = pygame.image.load(f"barra-caricamento/{percentuale}.png")
    frame = pygame.transform.scale(frame, (450, 150))
    barra.append(frame)

#definisco costanti barra -demo

POSIZIONE_BARRA = (200, 450)
DELAY = 1200
TOTAL_FRAMES = len(barra)

#definisco pulsante -demo

PLAY_BUTTON = pygame.image.load("play - button.png").convert_alpha()
PLAY_RECT=PLAY_BUTTON.get_rect(center=(WINDOW_WIDTH//2,WINDOW_HEIGHT//2+170))
#definisco schermata gameplay -demo

SCHERMATA_GAMEPLAY = pygame.image.load("schermata-gameplay.jpg")
SCHERMATA_GAMEPLAY = pygame.transform.scale(SCHERMATA_GAMEPLAY, (WINDOW_WIDTH, WINDOW_HEIGHT))

#definisco katana -demo

KATANA = pygame.image.load("katana.png").convert_alpha()
KATANA = pygame.transform.scale(KATANA, (KATANA.get_width() * 0.2, KATANA.get_height() * 0.2))
KATANA_RECT = KATANA.get_rect()

#definisco scia taglio -demo

SCIA = pygame.image.load("scia.png").convert_alpha()
SCIA_RECT = SCIA.get_rect()

#definisco trofeo
#TROFEO_RECT=pygame.Rect(WINDOW_WIDTH-70, 70 , 50, 50)
TROFEO_RECT=pygame.Rect(WINDOW_WIDTH-100, WINDOW_HEIGHT-565 , 65, 65)
TROFEO = pygame.image.load("trofeo.png")
#TROFEO=pygame.transform.scale(TROFEO,(50,50))

STATS_RECT=pygame.Rect(WINDOW_WIDTH-500,WINDOW_HEIGHT-450,500,300)
STATS_SFONDO=pygame.image.load("sfondo stats.png")
X_RECT=pygame.Rect(715,148,40,40)
X_IMMAGINE=pygame.image.load("x.png")

QUIT_IMMAGINE=pygame.image.load("x.png")
QUIT_RECT=pygame.Rect(907,505,50,50)

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

CUORE = pygame.image.load("Scooby Game Graphics/Fruits/cuore rosso.png")
CUORE = pygame.transform.scale(CUORE, (CUORE.get_width()* 0.5, CUORE.get_height()*0.5))
CUORE_RECT = CUORE.get_rect()

#Game over
GAME_OVER = pygame.image.load("game_over.jpg")
GAME_OVER = pygame.transform.scale(GAME_OVER, (WINDOW_WIDTH,WINDOW_HEIGHT))

