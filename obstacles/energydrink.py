import pygame

from obstacles.obstacle import Obstacle


class EnergyDrink(Obstacle):
    image_file = 'images/obstacles/energydrink.png'

    def __init__(self, screen, position, speed, player):
        Obstacle.__init__(self,
                          pygame.image.load(self.image_file).convert_alpha(),
                          screen,
                          position,
                          speed,
                          player)