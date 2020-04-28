import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class to represent aliens."""
    def __init__(self, ai_game):
        """Initializes alien and starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # Load alien image
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store exact (float) position
        self.x = float(self.rect.x)

    def update(self):
        """Move alien."""
        self.x += (self.settings.alien_speed *
                    self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Return True if an alien has hit the edge."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
