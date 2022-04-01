from game.casting.actor import Actor
from constants import *
import math
from random import choice, randint


class Debris(Actor):
    """Actors used for title screen

    The responsibility of the debris class is to randomly generate debris for each
    the title screen.

    Attributes:
        _spin_type (int): Random integer generated to determine spin amount.
    """

    def __init__(self):
        super().__init__("spacer/assets/images/debris" + str(randint(1, 15)) + ".png")
        self._speed = choice([i for i in range(-4, 4) if i not in [0]])
        self._spin_type = choice([i for i in range(-4, 4) if i not in [0]])
        self._center.change_position(
            randint(1, SCREEN_WIDTH - self._radius),
            randint(1, SCREEN_HEIGHT - self._radius),
        )
        self._direction = randint(1, 300)
        self._velocity.change_velocity(
            math.cos(math.radians(randint(0, 360))) * self._speed,
            math.sin(math.radians(randint(0, 360))) * self._speed,
        )

    def spin(self):
        """
        Makes debris objects on title screen rotate
        """
        self._angle += self._spin_type
