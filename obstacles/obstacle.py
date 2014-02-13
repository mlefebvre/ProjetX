from pygame.sprite import Sprite
import pygame

class Obstacle(Sprite):
    images = []

    def __init__(self, image, screen, position, speed):
        Sprite.__init__(self)
        self.x = position[0]
        self.y = position[1]
        self.last_y = self.y
        self.speed = speed
        self.screen = screen
        self.image = image

        w, h = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, w, h)

    def update(self, time_passed):
        displacement = self.speed * time_passed
        self.last_y = self.y
        self.y += displacement

        w, h = self.image.get_size()
        self._change_rect(self.x, self.y, w, h)

    def blit(self):
        draw_pos = self.image.get_rect().move(self.x, self.y)
        self.screen.blit(self.image, draw_pos)
        #pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 1)

    def _change_rect(self, x, y, w, h):
        if y > self.last_y + h:  # Pour eviter que l'obstacle passe d'un bord a un autre du joueur sans entrer en collision avec
            self.rect = pygame.Rect(x,
                                    y - (y - self.last_y) + h,
                                    w,
                                    h + y - (self.last_y + h))
        else:
            self.rect = pygame.Rect(x,
                                    y,
                                    w,
                                    h)



