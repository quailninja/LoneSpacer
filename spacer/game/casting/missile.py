from game.casting.enemy import Enemy
from constants import *


class Missile(Enemy):
    """
    Missiles

    This class is responsible for all bullets in the game.

    """

    def __init__(self, angle, ship_x, ship_y, player_ship):
        """
        :parm angle: This is the ships current angle
        :parm ship_x: Ships x location
        :parm ship_y: Ships y Location
        :parm img: Image Bullet will use
        parmaters get the ships current angel, location and speed and then match it
        and adds bullet speed. 0 - speed, 1 - life, 2- distance,
        3- rate, 4- swarm_distance, 5 - img, 6 - points
        """
        super().__init__(
            player_ship,
            [ship_x, ship_y],
            [MISSILE_SPEED, MISSILE_LIFE, 0, 5, CLOSE_SWARM, MISSILE_IMG, 1],
        )
        self._radius = MISSILE_RADIUS
        self._scale = MISSILE_SCALE
        self._angle = angle
        self._angle_correct = -90
