class Settings:
    """Settings for Alien Invasion."""

    def __init__(self):
        """Initialize game settings."""
        # Screen settings
        self.screen_width = 1050
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
