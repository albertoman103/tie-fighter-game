import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single tie fighter in the imperial fleet."""

    def __init__(self, ai_game):
        """Initialize the tie fighters and their starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the tie fighter image and set its rect attribute.
        self.image = pygame.image.load('images\\tie1.bmp')
        self.rect =self.image.get_rect()

        # Start each new tie fighter near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the tie fighter's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return true if tie fighter is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the tie fighters to the right."""
        self.x += (self.settings.alien_speed *
                   self.settings.fleet_direction)
        self.rect.x = self.x
