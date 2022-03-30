from random import randint
from game.casting.actor import Actor
from constants import *


class Loot(Actor):
    """
    Anything dropped by enemies

    This class is responsible for all loot in the game.

    Attributes:
        _loot_type (str): List item type as a string
        _spin (float): Random number for how fast item spins
    """

    def __init__(self, xy, img, loot_type):
        """
        :parm xy: This is a list of the x y coordinates
        :parm img: Image Bullet will use
        :parm loot_type: String, item name
        """
        super().__init__(img)
        self.change_scale(0.25)
        self.change_radius = 8
        self._center.change_position(xy[0], xy[1])
        self._loot_type = loot_type
        num = randint(0, 100)
        if self._loot_type == "health":
            if num < 50:
                self._value = 1
            elif num < 75:
                self._value = 2
            elif num < 90:
                self._value = 3
            else:
                self._value = 4
        else:
            if num < 90:
                self._value = 1
            elif num < 98:
                self._value = 2
            else:
                self._value = 3

    def get_loot_type(self):
        """Returns _loot_type

        Returns:
            str: self._loot_type
        """
        return self._loot_type

    def get_value(self):
        """Returns _value

        Returns:
            int: self._value
        """
        return self._value

    def advance(self):
        super().advance()
        self._angle += 0.33
