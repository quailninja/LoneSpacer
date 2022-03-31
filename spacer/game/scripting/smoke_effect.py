from game.scripting.action import Action
from game.casting.particle import Smoke
from constants import *


class SmokeEffect(Action):
    """The way the smoke moves.

    The responsibility of SmokeEffect is to move the smoke once it is created and then delete it after it's fade rate is
    reaches a the Particle Fade Rate
    """

    def execute(self, cast, particles):
        smoke_list = particles.get_particles(SMOKE_GROUP)
        for smoke in smoke_list:
            if smoke.alpha <= PARTICLE_FADE_RATE:
                smoke.remove_from_sprite_lists()
            else:
                smoke.alpha -= SMOKE_FADE_RATE
                smoke.center_x += smoke.change_x
                smoke.center_y += smoke.change_y
                smoke.scale += SMOKE_EXPANSION_RATE
