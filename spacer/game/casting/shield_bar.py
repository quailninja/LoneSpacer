from constants import *
from game.casting.actor import Actor


class ShieldBar(Actor):
    """Healthbar used to track health

    The responsibility of the healthbar class is to keep track of an actors health.

    Attributes:
        _current_shield (int): The current shield value
        _max_shield (int): The max shield amount
        _shield_activations (int): The number of shields the player has
    """

    def __init__(self):
        super().__init__()
        self._center.change_position(825, SCREEN_HEIGHT - HUD_FONT_SIZE)
        self._current_shield = 0
        self._max_shield = 10
        self._shield_activations = 0

    def draw(self):
        """
        An instance of draw. Changed from actor class to create health bar.
        """
        if self._current_shield < self._max_shield:
            arcade.draw_rectangle_filled(
                self._center._x,
                self._center._y,
                width=SHIELDBAR_WIDTH,
                height=SHIELDBAR_HEIGHT,
                color=arcade.color.DARK_BLUE_GRAY,
            )

        shield_width = SHIELDBAR_WIDTH * (self._current_shield / self._max_shield)

        arcade.draw_rectangle_filled(
            self._center._x - 0.5 * (SHIELDBAR_WIDTH - shield_width),
            self._center._y,
            width=shield_width,
            height=SHIELDBAR_HEIGHT,
            color=arcade.color.LIGHT_BLUE,
        )
        arcade.draw_text(
            f"Shield:  {self._current_shield}/{self._max_shield}",
            self._center._x - SHIELDBAR_WIDTH - 60,
            self._center._y - 10,
            arcade.color.WHITE,
            self._font_size,
            font_name=self._font,
        )
        arcade.draw_text(
            f"Shields:{self._shield_activations}",
            self._center._x + SHIELDBAR_WIDTH + 20,
            self._center._y - 10,
            arcade.color.WHITE,
            self._font_size,
            font_name=self._font,
        )

    def update_shield(self, shield, num_shields):
        """
        Used to update healthbar of actor
        :parm shield (int): Players shield life
        :parm num_shields (int): Number of shields a player can activate left
        """
        self._current_shield = shield
        self._shield_activations = num_shields

    def advance(self):
        """Not Implemented"""
        pass
