class StaticSettings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 1200
        self.bg_color = "grey"
        self.background1 = "images/background.png"

        self.caption = "Alien Invasion"


class DynamicSettings:
    def __init__(self):
        self.ship_speed = 1

        self.bullet_speed = 2

        self.shooting_speed = 5

        self.delay = 1 / self.shooting_speed
