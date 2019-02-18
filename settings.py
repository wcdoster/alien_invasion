class Settings():

    def __init__(self):
        #Screen Settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230,230,230)

        #ships
        self.ship_speed_factor = 5
        self.ships_left = 3

        #bullets
        self.bullet_speed_factor = 5
        self.bullet_width = 500
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #aliens
        self.alien_speed_factor = 4
        self.fleet_drop_speed = 10
        self.fleet_direction = 1