from game.scripting.action import Action
from game.casting.enemy import Enemy
import random as r
from constants import *


class SpawnEnemies(Action):
    """Spawns enemy ships.

    The responsibility of SpawnEnemies is to check the level and spawn enemies according to the level.

    """

    def __init__(self):
        self._spawn_on = True

    def execute(self, cast):
        """
        Spawns enemies, it uses dictionaries to determine spawn location and
        enemy type.
        """

        enemy_list = cast.get_actors(ENEMY_GROUP)
        player_list = cast.get_actors(SHIP_GROUP)
        level = cast.get_first_actor(LEVEL_GROUP)
        spawn_location = {
            1: self.top_spawn,
            2: self.right_spawn,
            3: self.left_spawn,
            4: self.bottom_spawn,
        }
        enemy_type = {
            1: self.black_enemy,
            2: self.green_enemy,
            3: self.blue_enemy,
            4: self.red_enemy,
        }
        if len(player_list) > 0 and self._spawn_on:
            if (
                len(enemy_list) <= MAXIMUM_ENEMIES
                and r.randint(0, level.get_spawn_rate()) == 0
            ):
                if level.get_level() > 4:
                    for enemy in enemy_list:
                        cast.remove_actor(ENEMY_GROUP, enemy)
                    cast.add_actor(
                        ENEMY_GROUP,
                        Enemy(
                            player_list[0],
                            spawn_location[r.randint(1, 4)](),
                            self.boss(),
                        ),
                    )
                    boss = cast.get_first_actor(ENEMY_GROUP)
                    boss.set_boss()
                    boss.change_angle(0)
                    boss.change_angle_correct(-90)
                    boss.change_bullet_angle_correct(0)
                    boss.change_radius(BOSS_RADIUS)
                    level.set_boss()
                    self._spawn_on = False
                elif level.get_level() > 3:
                    cast.add_actor(
                        ENEMY_GROUP,
                        Enemy(
                            player_list[0],
                            spawn_location[r.randint(1, level._level)](),
                            enemy_type[level.level_4_spawn()](),
                        ),
                    )
                elif level.get_level() > 2:
                    cast.add_actor(
                        ENEMY_GROUP,
                        Enemy(
                            player_list[0],
                            spawn_location[r.randint(1, level._level)](),
                            enemy_type[level.level_3_spawn()](),
                        ),
                    )
                elif level.get_level() > 1:
                    cast.add_actor(
                        ENEMY_GROUP,
                        Enemy(
                            player_list[0],
                            spawn_location[r.randint(1, level._level)](),
                            enemy_type[level.level_2_spawn()](),
                        ),
                    )
                else:
                    cast.add_actor(
                        ENEMY_GROUP,
                        Enemy(
                            player_list[0],
                            spawn_location[1](),
                            enemy_type[level.level_1_spawn()](),
                        ),
                    )

    def top_spawn(self):
        x = r.randint(ENEMY_SHIP_RADIUS, SCREEN_WIDTH - ENEMY_SHIP_RADIUS)
        y = SCREEN_HEIGHT - ENEMY_SHIP_RADIUS - HUD_SPACE
        return [x, y]

    def bottom_spawn(self):
        x = r.randint(ENEMY_SHIP_RADIUS, SCREEN_WIDTH - ENEMY_SHIP_RADIUS)
        y = ENEMY_SHIP_RADIUS + 20
        return [x, y]

    def right_spawn(self):
        x = SCREEN_WIDTH - ENEMY_SHIP_RADIUS
        y = r.randint(ENEMY_SHIP_RADIUS, SCREEN_HEIGHT - ENEMY_SHIP_RADIUS)
        return [x, y]

    def left_spawn(self):
        x = ENEMY_SHIP_RADIUS
        y = r.randint(ENEMY_SHIP_RADIUS, SCREEN_HEIGHT - ENEMY_SHIP_RADIUS)
        return [x, y]

    def black_enemy(self):
        speed = SLOW_SPEED
        life = LOW_HEALTH
        rate = SLOW_SHOT_RATE
        range = MEDIUM_RANGE
        swarm = AVERAGE_SWARM
        img = ENEMY1_IMG
        points = BLACK_POINTS
        return [speed, life, rate, range, swarm, img, points]

    def green_enemy(self):
        speed = MEDIUM_SPEED
        life = LOW_HEALTH
        rate = FAST_SHOT_RATE
        range = CLOSE_RANGE
        swarm = CLOSE_SWARM
        img = ENEMY2_IMG
        points = GREEN_POINTS
        return [speed, life, rate, range, swarm, img, points]

    def blue_enemy(self):
        speed = SLOW_SPEED
        life = MEDIUM_HEALTH
        rate = AVERAGE_SHOT_RATE
        range = FAR_RANGE
        swarm = CLOSE_SWARM
        img = ENEMY3_IMG
        points = BLUE_POINTS
        return [speed, life, rate, range, swarm, img, points]

    def red_enemy(self):
        speed = FAST_SPEED
        life = HIGH_HEALTH
        rate = FAST_SHOT_RATE
        range = CLOSE_RANGE
        swarm = CLOSE_SWARM
        img = ENEMY4_IMG
        points = RED_POINTS
        return [speed, life, rate, range, swarm, img, points]

    def boss(self):
        speed = SLOW_SPEED
        life = BOSS_HEALTH
        rate = SLOW_SHOT_RATE
        range = BOSS_RANGE
        swarm = CLOSE_SWARM
        img = BOSS_IMG
        points = BOSS_POINTS
        return [speed, life, rate, range, swarm, img, points]
