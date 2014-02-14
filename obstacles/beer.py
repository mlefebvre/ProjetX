#!/usr/bin/env python
#coding: utf8

import pygame

from obstacles.obstacle import Obstacle


class Beer(Obstacle):
    image_file = 'images/obstacles/beer.png'

    def __init__(self, gameboard, position, speed, player):
        Obstacle.__init__(self,
                          pygame.image.load(self.image_file).convert_alpha(),
                          gameboard,
                          position,
                          speed,
                          player)