#!/usr/bin/env python
#coding: utf8

import math
import pygame
from effects.effect import Effect

TRAIL_SIZE = 10
RIGHT_OFFSET = 10
LEFT_OFFSET = 20


class HorizontalTrail(Effect):
    image_file = 'images/nyan_trail_player.png'
    image = None

    def __init__(self, entity, gameboard, duration):
        Effect.__init__(self,
                        entity,
                        self._load_image(),
                        gameboard,
                        duration)
        self.trails = []
        self.trails2 = []
        self.trail_offset = 0

    def blit(self):
        if len(self.trails) == TRAIL_SIZE:
            self.trails.pop(0)

        if self.entity.orientation == 1:
            self.trail_offset = RIGHT_OFFSET
        else:
            self.trail_offset = LEFT_OFFSET

        self.trails.append([self.image, self.entity.x + 10, self.entity.y + 10])

        size = len(self.trails)
        for i in range(size):
            trail = self.trails[i]
            x = self.trail_offset + trail[1]
            y = 15 + trail[2] + 5 * math.cos((trail[1] + 40) / 20)
            self.gameboard.blit(trail[0], self.image.get_rect().move(x, y))

    def kill(self):
        self.trails = []

        super(HorizontalTrail, self).kill()

    def _load_image(self):
        if not HorizontalTrail.image:
            HorizontalTrail.image = pygame.image.load(HorizontalTrail.image_file).convert_alpha()
        return HorizontalTrail.image