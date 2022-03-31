import arcade
from constants import *
import random
import math


class Smoke(arcade.SpriteCircle):
    """
    Smoke

    This class is responsible for all particles in the game
    #TODO - Try to get this working for ship thrusters

    Attributes:
        change_y(int): part of arcade, this is akin to velocity
        scale(int): Size of the smoke, helps it grow
    """

    def __init__(self, size):
        super().__init__(size, arcade.color.LIGHT_GRAY, soft=True)
        self.change_y = SMOKE_RISE_RATE
        self.scale = SMOKE_START_SCALE

    def advance(self):
        """Not Implemented"""
        pass


class Particle(arcade.SpriteCircle):
    """
    Particles

    This class is responsible for all particles in the game
    #TODO - Try to get this working for ship thrusters

    Attributes:
        color (class): random color from arcade colors
        normal_texture (self): this is a snap shot of it's self to help create sparkle effect
        speed (int): how fast the particle will move
        direction(int): random direction of the particle
        change_x(int): part of arcade, this is akin to velocity
        change_y(int): part of arcade, this is akin to velocity
        my_alpha(int): particles opacity
    """

    def __init__(self):
        color = random.choice(PARTICLE_COLORS)
        super().__init__(PARTICLE_RADIUS, color)
        self.normal_texture = self.texture
        speed = random.random() * PARTICLE_SPEED_RANGE + PARTICLE_MIN_SPEED
        direction = random.randrange(360)
        self.change_x = math.sin(math.radians(direction)) * speed
        self.change_y = math.cos(math.radians(direction)) * speed
        self.my_alpha = 255

    def advance(self):
        """Not Implemented"""
        pass
