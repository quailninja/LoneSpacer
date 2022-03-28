from constants import *
from game.casting.actor import Actor


class Score(Actor):
    """Players Score

    The score class is responsible for keeping track of the players score.

    Attributes:
        _score (int): Players score
    """

    def __init__(self):
        super().__init__()
        self._score = 0
        self._center.change_position(250, SCREEN_HEIGHT - HUD_SPACE)

    def add_points(self, num):
        """Adds points to the players score

        Args:
            num (int): Number of points to add to the score
        """
        self._score += num

    def draw(self):
        """Modified from parent class to draw text"""
        arcade.draw_text(
            f"Score: {self._score}",
            self._center._x,
            self._center._y,
            arcade.color.WHITE,
            self._font_size,
            font_name=self._font,
        )

    def get_score(self):
        """Gets current score

        Returns:
            int: Returns current score
        """
        return self._score

    def advance(self):
        """Not needed"""
        pass
