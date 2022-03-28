from game.casting.actor import Actor
from constants import *
import math
from random import choice, randint


class Debri(Actor):
    """Actors used for title screen

    The responsibility of the debri class is to randomly generate debri for each
    the title screen.

    Attributes:
        _spin_type (int): Random integer generated to determine spin amount.
    """

    def __init__(self):
        super().__init__("spacer/assets/images/debri" + str(randint(1, 15)) + ".png")
        self._angle = 0
        self._radius = 10
        self._speed = choice([i for i in range(-4, 4) if i not in [0]])
        self._spin_type = choice([i for i in range(-4, 4) if i not in [0]])
        self._center.change_position(
            randint(1, SCREEN_WIDTH - self._radius),
            randint(1, SCREEN_HEIGHT - self._radius),
        )
        self._direction = randint(1, 300)
        self._velocity._dx = math.cos(math.radians(self._direction)) * self._speed
        self._velocity._dy = math.sin(math.radians(self._direction)) * self._speed

    def spin(self):
        """
        Makes debri objects on title screen rotate
        """
        self._angle += self._spin_type
