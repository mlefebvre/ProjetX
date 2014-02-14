import pygame
from pygame.surface import Surface

DEFAULT_BLUR = 10


class GameBoard(Surface):
    background_file = 'images/background.png'
    flip_time = 0
    blur_time = 0

    def __init__(self, size):
        Surface.__init__(self, size)
        self.children = []
        self.background = None
        self.width, self.height = size

    def add_child(self, child):
        self.children.append(child)

    def update(self, time_passed):
        self._draw_background()

        for child in self.children:
            child.update(time_passed)
            child.blit()

    def render(self):
        surface = self
        if pygame.time.get_ticks() < self.flip_time:
            surface = pygame.transform.flip(self, False, True)

        if pygame.time.get_ticks() < self.blur_time:
            surface = self._blur(surface, DEFAULT_BLUR)

        return surface

    def flip(self, duration):
        if duration == 0:
            self.flip_time = 0
        else:
            self.flip_time = pygame.time.get_ticks() + duration * 1000

    def blur(self, duration):
        if duration == 0:
            self.blur_time = 0
        else:
            self.blur_time = pygame.time.get_ticks() + duration * 1000

    def _draw_background(self):
        if not self.background:
            self.background = pygame.image.load(self.background_file)
        self.blit(self.background, (0, 0))

    def _blur(self, surface, amt):
        if amt < 1.0:
            raise ValueError("Arg 'amt' must be greater than 1.0, passed in value is %s"%amt)
        scale = 1.0/float(amt)
        surf_size = surface.get_size()
        scale_size = (int(surf_size[0]*scale), int(surf_size[1]*scale))
        surf = pygame.transform.smoothscale(surface, scale_size)
        surf = pygame.transform.smoothscale(surf, surf_size)
        return surf