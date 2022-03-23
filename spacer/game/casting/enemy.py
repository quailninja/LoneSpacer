from game.casting.actor import Actor
from constants import *
import math


class Enemy(Actor):
    def __init__(self, player_ship, x, y):
        """
        :parm player_ship: This is the player ship, need for enemy tracking
        :parm x: for point class, this is were enemy will spawn on x axis
        :parm y: for point class, this is were enemy will spawn on y axis
        """
        super().__init__(ENEMY_BLACK_IMG)
        self._center.change_position(x, y)
        self._scale = ENEMY_SHIP_SCALE
        self._radius = ENEMY_SHIP_RADIUS
        self._speed = ENEMY_SHIP_THRUST_AMOUNT
        self._player_ship = player_ship
        self._angle = 45
        self._life = 1

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

        self._angle = math.degrees(angle) + 90
        if self._center._y < self._player_ship._center._y - (ENEMY_DISTANCE):
            self._center._y += min(
                ENEMY_SPEED, self._player_ship._center._y - self._center._y
            )
        elif self._center._y > self._player_ship._center._y + (ENEMY_DISTANCE):
            self._center._y -= min(
                ENEMY_SPEED, self._center._y - self._player_ship._center._y
            )

        if self._center._x < self._player_ship._center._x - (ENEMY_DISTANCE):
            self._center._x += min(
                ENEMY_SPEED, self._player_ship._center._x - self._center._x
            )

        elif self._center._x > self._player_ship._center._x + (ENEMY_DISTANCE):
            self._center._x -= min(
                ENEMY_SPEED, self._center._x - self._player_ship._center._x
            )

        if self._life < 1:
            self._alive = False
