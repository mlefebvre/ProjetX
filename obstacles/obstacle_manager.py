#!/usr/bin/env python
#coding: utf8

import random
from beer import Beer
from nyan import Nyan
from healthpack import HealthPack
from energydrink import EnergyDrink
from vodka import Vodka
from pygame.sprite import Group, spritecollide
import pygame

class ObstacleManager:

    obstacle_types = {Beer: 89,
                      Nyan: 2,
                      EnergyDrink: 3,
                      HealthPack: 4,
                      Vodka: 10
                      }
    obstacles = []
    counter = 0
    default_speed = 0

    def __init__(self, gameboard, speed, max_obstacles, collision_strategy_factory, player):
        self.max_obstacles = max_obstacles
        self.gameboard = gameboard
        self.width = gameboard.width
        self.height = gameboard.height
        self.speed = speed
        self.default_speed = speed
        self.obstacle_group = Group()
        self.collision_strategy_factory = collision_strategy_factory
        self.player = player

    def update(self, time_passed):
        delete_list = []

        for obstacle in self.obstacles:
            if obstacle.y > self.height:
                delete_list.append(obstacle)
            else:
                obstacle.update(time_passed)

        for obstacle in delete_list:
            self.obstacles.remove(obstacle)
            obstacle.kill()

    def blit(self):
        for obstacle in self.obstacles:
            obstacle.blit()

    def create_obstacle(self):
        if len(self.obstacles) <= self.max_obstacles:
            self.counter += 1
            if self.counter % 10 == 0:
                obstacle = self.__select_obstacle_type()(self.gameboard,
                                                         (random.randint(0, self.width), -40),
                                                         self.speed * (1 + (random.random()-0.5) * 0.2))

                self.obstacles.append(obstacle)
                self.obstacle_group.add(obstacle)

    def __select_obstacle_type(self):
        total = sum(w for c, w in self.obstacle_types.items())
        r = random.uniform(0, total)
        upto = 0
        for c, w in self.obstacle_types.items():
            if upto + w > r:
                return c
            upto += w

    def detect_collision(self):
        collisions = spritecollide(self.player, self.obstacle_group, True)

        for c in collisions:
            self.collision_strategy_factory.get_strategy(c).on_collision()
            self.obstacles.remove(c)
            c.kill()

    def accelerate_obstacles(self, speed):
        self.speed += speed
        if self.speed > 1.5:
            self.speed = 1.5

    def reset(self):
        self.speed = self.default_speed
        for obstacle in self.obstacles:
            obstacle.kill()
            self.obstacle_group.remove(obstacle)
        self.obstacles = []

