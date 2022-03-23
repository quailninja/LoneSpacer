from game.scripting.action import Action
from constants import *


class CheckCollision(Action):
    """
    Check for collisions with bullets and ships.

    The responsibility of CheckCollision is to check if ships and bullet_speed
    have collided.  It then updates the life of that Actor.
    """

    def execute(self, cast):
        """
        Checks to see if bullets have collided with the player or enemy ships.
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

        for ship1 in enemy_list:
            for ship2 in enemy_list:
                distance = ship1._radius + ship2._radius
                if (
                    abs(ship1._center._x - ship2._center._x) < distance
                    and abs(ship1._center._y - ship2._center._y) < distance
                ):
                    if ship1._center._y < ship2._center._y:
                        ship1._center._y -= FLOCK_DISTANCE
                    elif ship1._center._y > ship2._center._y:
                        ship1._center._y += FLOCK_DISTANCE

                    if ship1._center._x < ship2._center._x:
                        ship1._center._x -= FLOCK_DISTANCE

                    elif ship1._center._x > ship2._center._x:
                        ship1._center._x += FLOCK_DISTANCE
