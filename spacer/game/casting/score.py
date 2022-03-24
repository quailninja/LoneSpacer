from constants import *
from game.casting.actor import Actor


class Score(Actor):
    def __init__(self):
        super().__init__()
        self._score = 0
        self._center.change_position(250, SCREEN_HEIGHT - HUD_SPACE)
        self._font_size = HUD_FONT_SIZE
        self._font = HUD_FONT_NAME

    def add_points(self, num):
        self._score += num

    def draw(self):
        arcade.draw_text(
            f"Score: {self._score}",
            self._center._x,
            self._center._y,
            arcade.color.WHITE,
            self._font_size,
            font_name=self._font,
        )

    def get_score(self):
        return self._score

    def advance(self):
        pass
