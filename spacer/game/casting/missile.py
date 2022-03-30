from game.casting.enemy import Enemy
from constants import *


class Missile(Enemy):
    """
    Missiles

    This class is responsible for all bullets in the game.

    Attributes:
        _damage (int): How much damage missile does
    """

    def __init__(self, angle, ship_x, ship_y, player_ship):
        """
        :parm angle: This is the ships current angle
        :parm ship_x: Ships x location
        :parm ship_y: Ships y Location
        :parm player_ship: Tracks player ship
        """
        super().__init__(
            player_ship,
            [ship_x, ship_y],
            [MISSILE_SPEED, MISSILE_LIFE, 0, 5, CLOSE_SWARM, MISSILE_IMG, 1],
        )
        self.change_radius(MISSILE_RADIUS)
        self.change_scale(MISSILE_SCALE)
        self.change_angle(angle)
        self.change_angle_correct(-90)
        self._damage = LOW_DAMAGE

    def get_damage(self):
        return self._damage
