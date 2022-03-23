from game.scripting.action import Action
from game.casting.bullet import Bullet
import random as r
from constants import *


class EnemyFire(Action):
    """
    Causes enemy ships to fire at player
    """

    def execute(self, cast):
        """
        Checks to make sure player is with a certain range and randomly shoots based of rate of fire.
        """
        cast_list = cast.get_actors(ENEMY_GROUP)
        player_list = cast.get_actors(SHIP_GROUP)
        in_range = False
        for item in cast_list:
            for player in player_list:
                if item._center._y > player._center._y - (ENEMY_DISTANCE):
                    in_range = True
                elif item._center._y < player._center._y + (ENEMY_DISTANCE):
                    in_range = True
                if item._center._x > player._center._x - (ENEMY_DISTANCE):
                    in_range = True
                elif item._center._x < player._center._x + (ENEMY_DISTANCE):
                    in_range = True
            if in_range and r.randint(0, ENEMY_SHOT_RATE) == 45:
                cast.add_actor(
                    ENEMY_BULLETS,
                    Bullet(
                        item._angle - 180,
                        item._center._x,
                        item._center._y,
                        item._velocity._dx,
                        item._velocity._dy,
                        ENEMY_BULLET_IMG,
                    ),
                )
