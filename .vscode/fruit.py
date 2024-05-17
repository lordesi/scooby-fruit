import pygame

class Fruit:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
    def blit_fruit(self, screen, x, y):
        screen.blit(self.image, (x,y))

