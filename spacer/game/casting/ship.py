from game.casting.actor import Actor
from constants import *
import math


class Ship(Actor):

    """
    The ship, well that's about it.
    """

    def __init__(self):
        super().__init__(SHIP_IMG)
        self._center._x = SCREEN_WIDTH / 2
        self._center._y = SCREEN_HEIGHT / 2
        self._scale = SHIP_SCALE
        self._radius = SHIP_RADIUS
        self._speed = SHIP_THRUST_AMOUNT
        self._shield_active = False
        self._life = PLAYER_LIFE
        self._onecount = True

    def turn_right(self):
        """
        Turns the ship right
        """
        self._angle -= SHIP_TURN_AMOUNT

    def turn_left(self):
        """
        Turns the ship left
        """
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

    def advance(self):
        """
        Checks the players life to see if they are still alive
        """
        super().advance()
        if self._life < 1:
            self._alive = False

    def one_count(self):
        """
        I'm having trouble with only having one explosion in the game, this is a tempory fix.
        """
        self._onecount = False

    def get_life(self):
        """
        Returns Actors current life
        """
        return self._life
