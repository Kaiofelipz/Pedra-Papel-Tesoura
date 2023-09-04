import pygame
from pygame.locals import *
from sys import exit


# class CreateImage():
#     def __init__(self):
#         self.image

class createImage():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

# button class


class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def Click(self):
        # posição do mouse
        position = pygame.mouse.get_pos()

        # verificar se esta clickado
        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        return self.clicked

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
