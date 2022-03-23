from game.scripting.action import Action
from constants import *


class UpdateHP(Action):
    """
    Causes enemy ships to fire at player
    """

    def execute(self, cast):
        """
        Checks to make sure player is with a certain range and randomly shoots based of rate of fire.
        """
        player = cast.get_actors(SHIP_GROUP)
        health_bar = cast.get_first_actor(HEALTH_GROUP)
        if len(player) > 0:
            health_bar.update_hp(player[0].get_life())
