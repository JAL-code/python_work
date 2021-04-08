# Import modules
import pygame
import sys

from settings import Settings
from ship import Ship
from bullet import Bullet

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
        # Set the screen mode - Minimize or Max
        self.screen = pygame.display.set_mode((1200, 800))
        # Use full screen
        versiontitle = f"README.mdvasion {self.version}"
        pygame.display.set_caption(versiontitle)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for  the game."""
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()

            # Get rid of bullets that have disappeared.
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            print(len(self.bullets))

    def _check_events(self):
        """Helper method: Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # Added to avoid hang bug.
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            #Start moving right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            #Start moving left 
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()
        elif event.key == pygame.K_v:
            self.screen = pygame.display.set_mode((1200, 800))
        elif event.key == pygame.K_f:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            print(self.screen.get_rect().width) # 1920
            self.settings.screen_height = self.screen.get_rect().height
            print(self.screen.get_rect().height) # 1080
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            #Stop moving right
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            #Stop moving left 
            self.ship.moving_left = False        

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        """Helper method: Update images on the screen,
        flip to the next screen. """
        # Redraw the screen during each pass throught the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
