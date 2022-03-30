from game.casting.actor import Actor
from constants import *
import math


class Ship(Actor):

    """
    The ship, well that's about it.

        _shield_count (int): How many shields the player has
        _onecount (bool): Stops the game from creating more than one explosion for the player.
    """

    def __init__(self):
        super().__init__(SHIP_IMG)
        self._center.change_position(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.change_scale(SHIP_SCALE)
        self.change_radius(SHIP_RADIUS)
        self.change_speed(SHIP_THRUST_AMOUNT)
        self.change_life(PLAYER_LIFE)
        self._shield_count = 1
        self._onecount = True

    def turn_right(self):
        """
        Turns the ship right
        """
        self._angle -= SHIP_TURN_AMOUNT

    def turn_left(self):
        """Turns the ship left"""
        self._angle += SHIP_TURN_AMOUNT

    def engine(self, direction):
        """
        Allows the ship to go forward or backwards
        """
        if direction == "forward":
            self._velocity._dx += math.cos(math.radians(self._angle + 90)) * self._speed
            self._velocity._dy += math.sin(math.radians(self._angle + 90)) * self._speed
        elif direction == "reverse":
            self._velocity._dx -= math.cos(math.radians(self._angle + 90)) * self._speed
            self._velocity._dy -= math.sin(math.radians(self._angle + 90)) * self._speed
        self.speed_check()

    def speed_check(self):
        """
        Does not let the ship continue into an infinite speed which would break reality and time
        as we know it, destorying the known universe.
        """
        if self._velocity._dx > SHIP_MAX_SPEED:
            self._velocity._dx = SHIP_MAX_SPEED
        elif self._velocity._dx < -SHIP_MAX_SPEED:
            self._velocity._dx = -SHIP_MAX_SPEED
        if self._velocity._dy > SHIP_MAX_SPEED:
            self._velocity._dy = SHIP_MAX_SPEED
        elif self._velocity._dy < -SHIP_MAX_SPEED:
            self._velocity._dy = -SHIP_MAX_SPEED

    def one_count(self):
        """
        I'm having trouble with only having one explosion in the game, this is a tempory fix.
        """
        self._onecount = False

    def add_shield(self, num):
        """Adds shields

        Args:
            num (int): add shields to _shield_count
        """
        self._shield_count += num

    def remove_shield(self, num):
        """Subtracts shields

        Args:
            num (int): add shields to _shield_count
        """
        self._shield_count -= num

    def add_life(self, num):
        """
        Returns Actors current life
        """
        self._life += num
        if self.get_life() > PLAYER_LIFE:
            self._life = PLAYER_LIFE

    def get_shield_count(self):
        """Return _shield_count

        Returns:
            int: _shield_count
        """
        return self._shield_count
