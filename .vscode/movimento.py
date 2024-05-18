import pygame
import settings
import random
from fruit import Fruit
from bomb import Bomb
from settings import fruit_images


def move(x, y, speed_x, speed_y, fruit_image, screen):
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
    fruit_image.blit_fruit(screen, x, y)