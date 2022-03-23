from constants import *
import random as r
from game.casting.actor import Actor


class Level(Actor):
    def __init__(self):
        super().__init__()
        self._level = 1
        self._spawn_rate = MEDIUM_SPAWN_RATE
        self._center.change_position(20, SCREEN_HEIGHT - HUD_SPACE)
        self._font_size = HUD_FONT_SIZE
        self._font = HUD_FONT_NAME

    def level_1_spawn(self):
        return 1

    def level_2_spawn(self):
        spawn_chance = r.randint(1, 100)
        if spawn_chance < 70:
            return 1
        else:
            return 2

    def level_3_spawn(self):
        spawn_chance = r.randint(1, 100)
        if spawn_chance < 60:
            return 1
        elif spawn_chance < 80:
            return 2
        else:
            return 3

    def level_4_spawn(self):
        spawn_chance = r.randint(1, 100)
        if spawn_chance < 35:
            return 1
        elif spawn_chance < 60:
            return 2
        elif spawn_chance < 90:
            return 3
        else:
            return 4

    def draw(self):
        arcade.draw_text(
            f"Level: {self._level}",
            self._center._x,
            self._center._y,
            arcade.color.WHITE,
            self._font_size,
            font_name=self._font,
        )

    def advance(self):
        pass
