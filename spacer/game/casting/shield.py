from game.casting.actor import Actor
from constants import *


class Shield(Actor):
    """
    A shield that goes around the ship

    This class is responsible for all shields in the game.

    """

    def __init__(self, ship_x, ship_y, ship_dx, ship_dy, img):
        """
        :parm angle: This is the ships current angle
        :parm ship_x: Ships x location
        :parm ship_y: Ships y Location
        :parm ship_dx: Ships speed on x axis
        :parm ship_dy: Ships speed on Y axis
        :parm img: Image Bullet will use
        parmaters get the ships current angel, location and speed and then match it
        and adds bullet speed.
        """
        super().__init__(img)
        self._radius = 0
        self._speed = 0
        self._life = 0
        self._scale = 0
        self._center._x = ship_x
        self._center._y = ship_y
        self._velocity._dx = 0
        self._velocity._dy = 0

    def advance(self):
        """
        The advance was changed so that the bullet will die after so many frames
        each from update takes one life from the bullet
        """
        super().advance()

        if self._life < 1:
            self._alive = False
