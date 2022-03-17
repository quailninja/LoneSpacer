from game.scripting.action import Action
from constants import *


class CheckCollision(Action):
    def execute(self, cast):
        """
        Checks to see if actors have the bag.
        Updates scores and removes dead items.
        :return:
        """
        enemy_list = cast.get_actors(ENEMY_GROUP)
        bullet_list = cast.get_actors(PLAYER_BULLET)
        enemy_bullets = cast.get_actors(ENEMY_BULLETS)
        player_list = cast.get_actors(SHIP_GROUP)
        for bullet in bullet_list:
            for enemy in enemy_list:
                distance = bullet._radius + enemy._radius
                if (
                    abs(bullet._center._x - enemy._center._x) < distance
                    and abs(bullet._center._y - enemy._center._y) < distance
                ):
                    bullet._alive = False
                    enemy._life -= 1

        for bullet in enemy_bullets:
            for player in player_list:
                distance = bullet._radius + player._radius
                if (
                    abs(bullet._center._x - player._center._x) < distance
                    and abs(bullet._center._y - player._center._y) < distance
                ):
                    bullet._alive = False
                    player._life -= 1
