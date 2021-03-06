from game.scripting.action import Action
from game.casting.bullet import Bullet
from game.casting.missile import Missile
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
        sounds = cast.get_first_actor(SOUND_GROUP)
        in_range = False
        for enemy in cast_list:
            for player in player_list:
                if enemy._center._y > player._center._y - (enemy._range):
                    in_range = True
                elif enemy._center._y < player._center._y + (enemy._range):
                    in_range = True
                if enemy._center._x > player._center._x - (enemy._range):
                    in_range = True
                elif enemy._center._x < player._center._x + (enemy._range):
                    in_range = True
            # TODO - Possibly change bullet img
            if in_range and r.randint(0, enemy._shot_rate) == 45:
                cast.add_actor(
                    ENEMY_BULLETS,
                    Bullet(
                        enemy._angle - enemy._bullet_angle_correct,
                        enemy._center._x,
                        enemy._center._y,
                        enemy._velocity._dx,
                        enemy._velocity._dy,
                        ENEMY_BULLET_IMG,
                        HIGH_DAMAGE if enemy.check_boss() else LOW_DAMAGE,
                    ),
                )
                sounds.play_sound("enemy_laser")
            if (
                enemy._boss
                and r.randint(0, FASTEST_SHOT_RATE) == 0
                and len(player_list) == 1
            ):
                cast.add_actor(
                    ENEMY_GROUP,
                    Missile(
                        enemy._angle,
                        enemy._center._x,
                        enemy._center._y,
                        player_list[0],
                    ),
                )
                sounds.play_sound("missile")
