import arcade
from constants import *
import random
import math


class Smoke(arcade.SpriteCircle):
    """This represents a puff of smoke"""

    def __init__(self, size):
        super().__init__(size, arcade.color.LIGHT_GRAY, soft=True)
        self.change_y = SMOKE_RISE_RATE
        self.scale = SMOKE_START_SCALE

    def advance(self):
        pass


class Particle(arcade.SpriteCircle):
    """Explosion of particles"""

    def __init__(self, my_list):
        color = random.choice(PARTICLE_COLORS)
        super().__init__(PARTICLE_RADIUS, color)
        self.normal_texture = self.texture
        speed = random.random() * PARTICLE_SPEED_RANGE + PARTICLE_MIN_SPEED
        direction = random.randrange(360)
        self.change_x = math.sin(math.radians(direction)) * speed
        self.change_y = math.cos(math.radians(direction)) * speed
        self.my_alpha = 255

    def advance(self):
        pass
