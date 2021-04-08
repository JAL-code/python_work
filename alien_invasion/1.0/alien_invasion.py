# Import modules
import pygame
import sys

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to merge game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        # Init an instance of the Settings
        self.settings = Settings()
        self.version = "1.0"

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        # Set the background color
        self.bg_color = (230, 230, 230)

        self.screen = pygame.display.set_mode((1200, 800))
        versiontitle = f"Alien Invasion {self.version}"
        pygame.display.set_caption(versiontitle)

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for  the game."""
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Helper method: Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # Added to avoid hang bug.
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the ship to the right.
                    self.ship.rect.x += 1
                elif event.key == pygame.K_LEFT:
                    # Move the ship to the left.
                    self.ship.rect.x -= 1
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    #Stop moving right
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    #Stop moving right
                    self.ship.moving_left = False

    def _update_screen(self):
        """Helper method: Update images on the screen,
        flip to the next screen. """
        # Redraw the screen during each pass throught the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
