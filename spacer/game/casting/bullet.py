from game.casting.actor import Actor
from constants import *
import math


class Bullet(Actor):

    """
    The bullet will have the same speed as the ship when being created
    The life is set to allow the bullet to die after so many frames
    """

    def __init__(self, angle, ship_x, ship_y, ship_dx, ship_dy, img):
        """
        :parm angle: This is the ships current angle
        :parm ship_x: Ships x location
        :parm ship_y: Ships y Location
        :parm ship_dx: Ships speed on x axis
        :parm ship_dy: Ships speed on Y axis
        parmaters get the ships current angel, location and speed and then match it
        and adds bullet speed.
        """
        super().__init__(img)
        self._radius = BULLET_RADIUS
        self._speed = BULLET_SPEED
        self._life = BULLET_LIFE
        self._scale = BULLET_SCALE
        self._angle = angle
        self._center._x = ship_x
        self._center._y = ship_y
        self._velocity._dx = (
            ship_dx + math.cos(math.radians(self._angle + 90)) * self._speed
        )
        self._velocity._dy = (
            ship_dy + math.sin(math.radians(self._angle + 90)) * self._speed
        )

    def advance(self):
        """
        The advance was changed so that the bullet will die after so many frames
        each from update takes one life from the bullet
        """
        super().advance()
        self._life -= 1
        if self._life < 1:
            self._alive = False