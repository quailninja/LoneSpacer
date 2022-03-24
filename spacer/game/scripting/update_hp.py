from game.scripting.action import Action
from constants import *


class UpdateHP(Action):
    """
    Updates hit poitns for healthbar
    """

    def execute(self, cast):
        """
        Checks what actors have healthbars and updates them.
        """
        player = cast.get_actors(SHIP_GROUP)
        health_bar = cast.get_first_actor(HEALTH_GROUP)
        if len(player) > 0:
            health_bar.update_hp(player[0].get_life())
