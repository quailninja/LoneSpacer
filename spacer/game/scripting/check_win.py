from game.scripting.action import Action
from constants import *


class CheckWin(Action):
    """
    Checks to see if next level has been achieved
    """

    def execute(self, cast):
        """
        Updates level based on game condition
        """
        enemy_list = cast.get_actors(ENEMY_GROUP)
        player_list = cast.get_actors(SHIP_GROUP)
        level = cast.get_first_actor(LEVEL_GROUP)
        if len(player_list) == 0:
            level.set_loss()
        if level.get_boss() and len(enemy_list) == 0:
            level.set_win()
