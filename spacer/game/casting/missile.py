from game.casting.actor import Actor
from constants import *
import math


class Missile(Actor):
    """
    Missiles

    This class is responsible for all bullets in the game.

    """

    def __init__(self, angle, ship_x, ship_y, ship_dx, ship_dy, player_ship):
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
        super().__init__(MISSILE_IMG)
        self._radius = MISSILE_RADIUS
        self._speed = MISSILE_SPEED
        self._life = MISSILE_LIFE
        self._scale = MISSILE_SCALE
        self._player_ship = player_ship
        self._angle = angle
        self._center._x = ship_x
        self._center._y = ship_y
        self._range = 0
        self._shot_rate = 5
        self._boss = False
        self._points = 1
        self._swarm_distance = CLOSE_SWARM

    def advance(self):
        """
        This function will move the current sprite towards the player ship
        based off the players location.  This will also have the enemy ships angle
        or point there ship in the direciton of the player.
        """
        start_x = self._center._x
        start_y = self._center._y

        dest_x = self._player_ship._center._x
        dest_y = self._player_ship._center._y

        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        self._angle = math.degrees(angle) - 90
        if self._center._y < self._player_ship._center._y:
            self._center._y += min(
                self._speed, self._player_ship._center._y - self._center._y
            )
        elif self._center._y > self._player_ship._center._y:
            self._center._y -= min(
                self._speed, self._center._y - self._player_ship._center._y
            )

        if self._center._x < self._player_ship._center._x:
            self._center._x += min(
                self._speed, self._player_ship._center._x - self._center._x
            )

        elif self._center._x > self._player_ship._center._x:
            self._center._x -= min(
                self._speed, self._center._x - self._player_ship._center._x
            )
        if self._life < 1:
            self._alive = False
