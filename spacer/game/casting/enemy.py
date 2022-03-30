from game.casting.actor import Actor
from constants import *
import math


class Enemy(Actor):
    """Actors used for enemies

    The responsibility of the enemy class is to generate enemies for the player.

    Attributes:
        _player_ship (class): The players ship used for tracking enemy
        _range (int): Distance from player needed to fire enemy
        _shot_rate (int): How fast the enemy can fire enemy
        _swarm_distance (int): How close enemy ships will get to eachother
        _points (int): How many points the enemy is worth
        _bullet_angel_correct(int): Needed for enemies bullet img to orient correctly on the screen.
        _angel_correct(int): This is used for the enemy tracking, it will orient the
        enemy image to the correct position when trying to face the player.
        _boss (bool): Whether the enemy is a boss or not
    """

    def __init__(self, player_ship, xy, stat):
        """
        :parm player_ship: This is the player ship, needed for enemy tracking
        :parm xy: The x and y points for the enemy to spawn
        :parm stat: A list of stats values for the enemy 0 - speed, 1 - life, 2- range,
        3- rate, 4- swarm_distance, 5 - img, 6 - points
        """
        super().__init__(stat[5])
        self._center.change_position(xy[0], xy[1])
        self.change_scale(ENEMY_SHIP_SCALE)
        self.change_radius(ENEMY_SHIP_RADIUS)
        self.change_speed(stat[0])
        self.change_life(stat[1])
        self.change_angle(45)
        self._player_ship = player_ship
        self._bullet_angle_correct = 180
        self._angle_correct = 90
        self._range = stat[2]
        self._shot_rate = stat[3]
        self._swarm_distance = stat[4]
        self._points = stat[6]
        self._boss = False

    def advance(self):
        """
        This function will move the current sprite towards the player ship
        based off the players location.  This will also have the enemy ships angle
        or point there ship in the direction of the player.
        """
        start_x = self._center._x
        start_y = self._center._y

        dest_x = self._player_ship._center._x
        dest_y = self._player_ship._center._y

        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        self._angle = math.degrees(angle) + self._angle_correct

        if self._center._y < self._player_ship._center._y - (self._range):
            self._center._y += min(
                self._speed, self._player_ship._center._y - self._center._y
            )
        elif self._center._y > self._player_ship._center._y + (self._range):
            self._center._y -= min(
                self._speed, self._center._y - self._player_ship._center._y
            )

        if self._center._x < self._player_ship._center._x - (self._range):
            self._center._x += min(
                self._speed, self._player_ship._center._x - self._center._x
            )

        elif self._center._x > self._player_ship._center._x + (self._range):
            self._center._x -= min(
                self._speed, self._center._x - self._player_ship._center._x
            )

        if self._life < 1:
            self._alive = False

    def set_boss(self):
        """Changes boss to true"""
        self._boss = True

    def change_angle_correct(self, num):
        """Changes angle_correct"""
        self._angle_correct = num

    def check_boss(self):
        """checks boss to be true"""
        return self._boss

    def get_points(self):
        """Return _points

        Returns:
            int: Return items point value
        """
        return self._points
