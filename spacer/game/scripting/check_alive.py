from game.scripting.action import Action
from game.casting.particle import Particle, Smoke
from game.casting.loot import Loot
from constants import *
from random import randint


class CheckAlive(Action):
    """
    Checks if an Actor is alive

    The responsibility of CheckAlive is to remove dead objects and return
    add explosions and smokes if they object is part of a enemy or player group.
    """

    def execute(self, cast):
        """
        Checks actors to see if they're still alive and then removes them, it also starts the explosion.
        """
        super().__init__()
        bullet_list = cast.get_actors(PLAYER_BULLET)
        enemy_bullets = cast.get_actors(ENEMY_BULLETS)
        enemy_list = cast.get_actors(ENEMY_GROUP)
        player = cast.get_actors(SHIP_GROUP)
        loot = cast.get_actors(LOOT_GROUP)
        shield = cast.get_actors(SHIELD_GROUP)

        self.remove_items(bullet_list, PLAYER_BULLET, cast)
        self.remove_items(enemy_bullets, ENEMY_BULLETS, cast)
        self.remove_items(enemy_list, ENEMY_GROUP, cast)
        self.remove_items(player, SHIP_GROUP, cast)
        self.remove_items(loot, LOOT_GROUP, cast)
        self.remove_items(shield, SHIELD_GROUP, cast)

    def remove_items(self, cast_list, group, cast):
        """
        Removes items that are in a group list
        """
        sound = cast.get_first_actor(SOUND_GROUP)
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
                    sound.play_sound("explosion")
                if group == ENEMY_GROUP:
                    cast.get_first_actor(SCORE_GROUP).add_points(item.get_points())
                    if randint(0, 1) == 0:
                        num = randint(0, 100)
                        position = item._center.get_position()
                        if num < 85:
                            self.loot_create(cast, position, HEALTH_IMAGE, "health")
                        else:
                            self.loot_create(cast, position, SHIELD_IMAGE, "shield")
                if group == LOOT_GROUP:
                    ship = cast.get_first_actor(SHIP_GROUP)
                    value = item.get_value()
                    if item.get_loot_type() == "health":
                        ship.add_life(value)
                    elif item.get_loot_type() == "shield":
                        ship.add_shield(value)
                cast.remove_actor(group, item)

    def loot_create(self, cast, xy, img, loot_type):
        cast.add_actor(
            LOOT_GROUP,
            Loot(xy, img, loot_type),
        )
