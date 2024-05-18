import pygame

class Bomb:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 0.55, self.image.get_height() * 0.55))
        self.rect = self.image.get_rect()
    def blit_bomb(self, screen, x, y):
        screen.blit(self.image, (x,y))