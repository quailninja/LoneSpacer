from game.scripting.action import Action
from game.casting.particle import Smoke
from constants import *


class SmokeEffect(Action):
    def execute(self, cast):
        """Update this particle"""
        smoke_list = cast.get_actors(SMOKE_GROUP)
        for smoke in smoke_list:
            if smoke.alpha <= PARTICLE_FADE_RATE:
                # Remove faded out particles
                smoke.remove_from_sprite_lists()
            else:
                # Update values
                smoke.alpha -= SMOKE_FADE_RATE
                smoke.center_x += smoke.change_x
                smoke.center_y += smoke.change_y
                smoke.scale += SMOKE_EXPANSION_RATE
