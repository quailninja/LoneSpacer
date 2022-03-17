from game.scripting.action import Action
from game.casting.particle import Particle, Smoke
from constants import *


class CheckAlive(Action):
    def execute(self, cast):
        """
        Checks actors to see if they're still alive and then removes them, it also starts the explosion.
        """
        bullet_list = cast.get_actors(PLAYER_BULLET)
        enemy_bullets = cast.get_actors(ENEMY_BULLETS)
        enemy_list = cast.get_actors(ENEMY_GROUP)
        player = cast.get_actors(SHIP_GROUP)

        self.remove_items(bullet_list, PLAYER_BULLET, cast)
        self.remove_items(enemy_bullets, ENEMY_BULLETS, cast)
        self.remove_items(enemy_list, ENEMY_GROUP, cast)
        self.remove_items(player, SHIP_GROUP, cast)

    def remove_items(self, cast_list, group, cast):
        """
        Removes items that are in a group list
        """
        for item in cast_list:
            if not item._alive:
                if group == ENEMY_GROUP or group == SHIP_GROUP:
                    for i in range(PARTICLE_COUNT):
                        explosions_list = cast.get_actors(EXPLOSION_GROUP)
                        particle = Particle(explosions_list)
                        particle.position = (item._center._x, item._center._y)
                        cast.add_actor(EXPLOSION_GROUP, particle)

                    smoke = Smoke(50)
                    smoke.position = (item._center._x, item._center._y)
                    cast.add_actor(SMOKE_GROUP, smoke)
                cast.remove_actor(group, item)
