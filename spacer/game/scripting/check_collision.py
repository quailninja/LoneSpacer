from game.scripting.action import Action
from constants import *


class CheckCollision(Action):
    """
    Check for collisions with bullets and ships.

    The responsibility of CheckCollision is to check if items have collided with eachother.
    It then updates the life of that Actor.
    """

    def execute(self, cast):
        """
        Checks to see if bullets have collided with the player or enemy ships.
        """
        enemies = cast.get_actors(ENEMY_GROUP)
        bullet_list = cast.get_actors(PLAYER_BULLET)
        enemy_bullets = cast.get_actors(ENEMY_BULLETS)
        player_list = cast.get_actors(SHIP_GROUP)
        loot_list = cast.get_actors(LOOT_GROUP)
        shield_list = cast.get_actors(SHIELD_GROUP)
        missile_list = []
        enemy_list = []

        for actor in enemies:
            if actor._radius == MISSILE_RADIUS:
                missile_list.append(actor)
            else:
                enemy_list.append(actor)
        if len(shield_list) > 0:
            self.check_collision_ships(enemy_list, shield_list)
            self.check_collision_bullets(missile_list, shield_list)
            self.check_collision_bullets(enemy_bullets, shield_list)
        else:
            self.check_collision_bullets(enemy_bullets, player_list)
            self.check_collision_bullets(missile_list, player_list)
            self.check_collision_ships(enemy_list, player_list)
        self.check_collision_bullets(bullet_list, enemies)
        for loot in loot_list:
            for player in player_list:
                distance = loot._radius + player._radius
                if (
                    abs(loot._center._x - player._center._x) < distance
                    and abs(loot._center._y - player._center._y) < distance
                ):
                    loot.kill()

        for ship1 in enemy_list:
            for ship2 in enemy_list:
                distance = ship1._radius + ship2._radius
                if (
                    abs(ship1._center._x - ship2._center._x) < distance
                    and abs(ship1._center._y - ship2._center._y) < distance
                ):
                    if ship1._center._y < ship2._center._y:
                        ship1._center._y -= ship1._swarm_distance
                    elif ship1._center._y > ship2._center._y:
                        ship1._center._y += ship1._swarm_distance

                    if ship1._center._x < ship2._center._x:
                        ship1._center._x -= ship1._swarm_distance

                    elif ship1._center._x > ship2._center._x:
                        ship1._center._x += ship1._swarm_distance

    def check_collision_bullets(self, bullets, ships):
        for bullet in bullets:
            for ship in ships:
                distance = bullet._radius + ship._radius
                if (
                    abs(bullet._center._x - ship._center._x) < distance
                    and abs(bullet._center._y - ship._center._y) < distance
                ):
                    bullet.kill()
                    ship.add_damage(bullet.get_damage())

    def check_collision_ships(self, ships1, ships2):
        for ship1 in ships1:
            for ship2 in ships2:
                distance = ship1._radius + ship2._radius
                if (
                    abs(ship1._center._x - ship2._center._x) < distance
                    and abs(ship1._center._y - ship2._center._y) < distance
                ):
                    ship1._life -= 1
                    ship2._life -= 1
