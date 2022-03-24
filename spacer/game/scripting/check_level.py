from game.scripting.action import Action
from constants import *


class CheckLevel(Action):
    """
    Causes enemy ships to fire at player
    """

    def execute(self, cast):
        """
        Checks to make sure player is with a certain range and randomly shoots based of rate of fire.
        """
        score = cast.get_first_actor(SCORE_GROUP).get_score()
        level = cast.get_first_actor(LEVEL_GROUP)
        if score > LEVEL_TWO and level.get_level() < 2:
            level.level_up()
        elif score > LEVEL_THREE and level.get_level() < 3:
            level.level_up()
        elif score > LEVEL_FOUR and level.get_level() < 4:
            level.level_up()
