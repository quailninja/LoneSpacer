from game.scripting.action import Action
from game.casting.announcement import Announcement
from constants import *


class CheckLevel(Action):
    """
    Checks to see if next level has been achieved
    """

    def execute(self, cast):
        """
        Updates level based on game condition
        """
        score = cast.get_first_actor(SCORE_GROUP).get_score()
        level = cast.get_first_actor(LEVEL_GROUP)
        if level.get_demo_mode():
            if score > DEMO_LEVEL_TWO and level.get_level() < 2:
                level.level_up()
                cast.add_actor(ANNOUNCEMENT_GROUP, Announcement("Level 2"))
            elif score > DEMO_LEVEL_THREE and level.get_level() < 3:
                level.level_up()
                cast.add_actor(ANNOUNCEMENT_GROUP, Announcement("Level 3"))
            elif score > DEMO_LEVEL_FOUR and level.get_level() < 4:
                level.level_up()
                cast.add_actor(ANNOUNCEMENT_GROUP, Announcement("Level 4"))
            elif score > DEMO_LEVEL_BOSS and level.get_level() < 5:
                level.level_up()
                cast.add_actor(ANNOUNCEMENT_GROUP, Announcement("Boss Level!!!"))
        else:
            if score > LEVEL_TWO and level.get_level() < 2:
                level.level_up()
                cast.add_actor(ANNOUNCEMENT_GROUP, Announcement("Level 2"))
            elif score > LEVEL_THREE and level.get_level() < 3:
                level.level_up()
                cast.add_actor(ANNOUNCEMENT_GROUP, Announcement("Level 3"))
            elif score > LEVEL_FOUR and level.get_level() < 4:
                level.level_up()
                cast.add_actor(ANNOUNCEMENT_GROUP, Announcement("Level 4"))
            elif score > LEVEL_BOSS and level.get_level() < 5:
                level.level_up()
                cast.add_actor(ANNOUNCEMENT_GROUP, Announcement("Boss Level!!!"))
