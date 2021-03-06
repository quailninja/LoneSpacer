from game.casting.actor import Actor
from constants import *
import math


class Bullet(Actor):
    """
    Bullets

    This class is responsible for all bullets in the game.

    """

    def __init__(self, angle, ship_x, ship_y, ship_dx, ship_dy, img, damage):
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
        self.change_radius(BULLET_RADIUS)
        self.change_speed(BULLET_SPEED)
        self.change_life(BULLET_LIFE)
        self.change_scale(BULLET_SCALE)
        self.change_angle(angle)
        self._center.change_position(ship_x, ship_y)
        self._damage = damage
        self._velocity.change_velocity(
            ship_dx + math.cos(math.radians(self._angle + 90)) * self._speed,
            ship_dy + math.sin(math.radians(self._angle + 90)) * self._speed,
        )

    def get_damage(self):
        return self._damage

    def advance(self):
        """
        The advance was changed so that the bullet will die after so many frames
        each from update takes one life from the bullet
        """
        super().advance()
        self._life -= 1
