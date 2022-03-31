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

    def execute(self, cast, particles):
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
        announcements = cast.get_actors(ANNOUNCEMENT_GROUP)

        self.remove_items(bullet_list, PLAYER_BULLET, cast)
        self.remove_items(enemy_bullets, ENEMY_BULLETS, cast)
        self.remove_items(enemy_list, ENEMY_GROUP, cast, particles)
        self.remove_items(player, SHIP_GROUP, cast, particles)
        self.remove_items(loot, LOOT_GROUP, cast)
        self.remove_items(shield, SHIELD_GROUP, cast)
        self.remove_items(announcements, ANNOUNCEMENT_GROUP, cast)

    def remove_items(self, cast_list, group, cast, particles=None):
        """
        Removes items that are in a group list
        """
        sound = cast.get_first_actor(SOUND_GROUP)
        for item in cast_list:
            if not item._alive:
                if group == ENEMY_GROUP or group == SHIP_GROUP:
                    for i in range(PARTICLE_COUNT):
                        particle = Particle()
                        particle.position = (item._center._x, item._center._y)
                        particles.add_particle(EXPLOSION_GROUP, particle)

                    smoke = Smoke(50)
                    smoke.position = (item._center._x, item._center._y)
                    particles.add_particle(SMOKE_GROUP, smoke)
                    sound.play_sound("explosion")
                if group == ENEMY_GROUP and item._radius != MISSILE_RADIUS:
                    cast.get_first_actor(SCORE_GROUP).add_points(item.get_points())
                    if randint(0, 4) == 0:
                        num = randint(0, 100)
                        position = item._center.get_position()
                        if num < 80:
                            self.loot_create(cast, position, HEALTH_IMAGE, "health")
                        else:
                            self.loot_create(cast, position, SHIELD_IMAGE, "shield")
                if group == LOOT_GROUP:
                    ship = cast.get_actors(SHIP_GROUP)
                    value = item.get_value()
                    if len(ship) > 0:
                        if item.get_loot_type() == "health":
                            ship[0].add_life(value)
                        elif item.get_loot_type() == "shield":
                            ship[0].add_shield(value)
                if group == SHIELD_GROUP:
                    cast.get_first_actor(SOUND_GROUP).play_sound("shield_down")
                cast.remove_actor(group, item)

    def loot_create(self, cast, xy, img, loot_type):
        cast.add_actor(
            LOOT_GROUP,
            Loot(xy, img, loot_type),
        )
