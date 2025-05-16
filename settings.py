class Settings:
    """Class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialise game's settings."""
        # Screen settings - width/height overruled when running full screen.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)
        # Ship settings
        self.ship_speed = 4
        # Bullet settings
        self.bullet_speed = 4
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (60, 60, 60)
        self.bullet_limit = 5
        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # Fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
