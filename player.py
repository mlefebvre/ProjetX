import os
import pygame
from pygame.sprite import Sprite


class Player(Sprite):
    image_directory = 'images/player/'
    images = {-1: [], 1: []}
    imageOrientation = 1
    counter = 0
    still_counter = 0
    image_id = 0


    def __init__(self, screen, position, speed):
        Sprite.__init__(self)
        self.x = position[0]
        self.y = position[1]
        self.speed = speed
        self.screen = screen
        self._load_images()
        w, h = self.images[self.imageOrientation][self.image_id].get_size()
        self.rect = pygame.Rect(self.x, self.y, w, h)

    def update(self, time_passed, direction):

        if direction != 0:
            self.still_counter = 0
            self.counter += 1
            if self.counter % 5 == 0:
                self.image_id = (self.image_id + 1) % len(self.images[self.imageOrientation])
        else:
            self.still_counter += 1
            if self.still_counter > 5:
                self.image_id = 0

        if self.imageOrientation != direction and direction != 0:
            self.imageOrientation = -self.imageOrientation

        displacement = direction * self.speed * time_passed

        bounds = self.screen.get_rect()
        new_x = self.x + displacement
        w, h = self.images[self.imageOrientation][self.image_id].get_size()

        if new_x > bounds.left and new_x + w < bounds.right:
            self.x = new_x
            self.rect = pygame.Rect(self.x, self.y, w, h)

    def blit(self):
        draw_pos = self.images[self.imageOrientation][self.image_id].get_rect().move(self.x, self.y)
        self.screen.blit(self.images[self.imageOrientation][self.image_id], draw_pos)

    def _load_images(self):
        for f in os.listdir(self.image_directory):
            if f.endswith(".png"):
                self.images[1].append(pygame.image.load(self.image_directory + f).convert_alpha())
                self.images[-1].append(pygame.transform.flip(self.images[1][-1], True, False))

