from game.casting.actor import Actor
from constants import *


class Shield(Actor):
    """
    A shield that goes around the ship

    This class is responsible for all shields in the game.

    Arguments
    _player_ship (class): The players ship

    """

    def __init__(self, player_ship, img):
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
        self._player_ship = player_ship
        self.change_radius(SHIELD_RADIUS)
        self.change_life(SHIELD_LIFE)
        self.change_scale(SHIELD_SCALE)

    def advance(self):
        """Tracks shield life"""
        super().advance()
        self._center.change_position(
            self._player_ship._center.get_x(), self._player_ship._center.get_y()
        )
