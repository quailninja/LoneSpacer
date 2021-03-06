from game.scripting.action import Action
from game.casting.particle import Smoke
from constants import *
import random


class Explosion(Action):
    """
    Control the particles

    The responsibility of Explosion is to move the particles and remove them from
    once they have a certain my_alpha value.
    """

    def execute(self, cast, particles):
        particle_list = particles.get_particles(EXPLOSION_GROUP)
        for particle in particle_list:
            if particle.my_alpha <= PARTICLE_FADE_RATE:
                particle.remove_from_sprite_lists()
            else:
                particle.my_alpha -= PARTICLE_FADE_RATE
                particle.my_alpha = particle.my_alpha
                particle.center_x += particle.change_x
                particle.center_y += particle.change_y
                particle.change_y -= PARTICLE_GRAVITY

                if random.random() <= PARTICLE_SPARKLE_CHANCE:
                    particle.alpha = 255
                    particle.texture = arcade.make_circle_texture(
                        int(particle.width), arcade.color.WHITE
                    )
                else:
                    particle.texture = particle.normal_texture

                if random.random() <= SMOKE_CHANCE:
                    smoke = Smoke(5)
                    smoke.position = particle.position
                    particles.add_particle(SMOKE_GROUP, smoke)
