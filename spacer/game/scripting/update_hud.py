from game.scripting.action import Action
from constants import *


class UpdateHUD(Action):
    """
    Updates hit poitns for healthbar
    """

    def execute(self, cast):
        """
        Checks what actors have healthbars and updates them.
        """
        player = cast.get_actors(SHIP_GROUP)
        shield = cast.get_actors(SHIELD_GROUP)
        hud_bars = cast.get_actors(HUD_GROUP)
        if len(player) > 0:
            hud_bars[0].update_hp(player[0].get_life())
            if len(shield) > 0:
                hud_bars[1].update_shield(
                    shield[0].get_life(), player[0].get_shield_count()
                )
            else:
                hud_bars[1].update_shield(0, player[0].get_shield_count())
