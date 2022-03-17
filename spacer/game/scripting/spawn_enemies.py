from game.scripting.action import Action
from game.casting.enemy import Enemy
import random as r
from constants import *


class SpawnEnemies(Action):
    def execute(self, cast):
        """
        Checks to make sure player is with a certain range and randomly shoots based of rate of fire.
        """
        player_list = cast.get_actors(SHIP_GROUP)
        if len(player_list) > 0:
            if r.randint(0, FIRST_ENEMY_SPAWN_RATE) == 0:
                cast.add_actor(
                    ENEMY_GROUP,
                    Enemy(
                        player_list[0],
                        r.randint(ENEMY_SHIP_RADIUS, SCREEN_WIDTH - ENEMY_SHIP_RADIUS),
                        SCREEN_HEIGHT - ENEMY_SHIP_RADIUS,
                    ),
                )
