from constants import *
from game.casting.actor import Actor


class HealthBar(Actor):
    """Healthbar used to track health

    The responsibility of the healthbar class is to keep track of an actors health.

    Attributes:
        _current_hp (int): The actors current health
        _max_hp (int): The actors max health
    """

    def __init__(self):
        super().__init__()
        self._score = 0
        self._center.change_position(600, SCREEN_HEIGHT - HUD_FONT_SIZE)
        self._font_size = HUD_FONT_SIZE
        self._font = HUD_FONT_NAME
        self._current_hp = 0
        self._max_hp = PLAYER_LIFE

    def draw(self):
        """
        An instance of draw. Changed from actor class to create health bar.
        """
        if self._current_hp < self._max_hp:
            arcade.draw_rectangle_filled(
                self._center._x,
                self._center._y,
                width=HEALTHBAR_WIDTH,
                height=HEALTHBAR_HEIGHT,
                color=arcade.color.RED,
            )

        health_width = HEALTHBAR_WIDTH * (self._current_hp / self._max_hp)

        arcade.draw_rectangle_filled(
            self._center._x - 0.5 * (HEALTHBAR_WIDTH - health_width),
            self._center._y,
            width=health_width,
            height=HEALTHBAR_HEIGHT,
            color=arcade.color.GREEN,
        )
        arcade.draw_text(
            f"Health:   {self._current_hp}/{self._max_hp}",
            self._center._x - HEALTHBAR_WIDTH - 40,
            self._center._y - 10,
            arcade.color.WHITE,
            self._font_size,
            font_name=self._font,
        )

    def update_hp(self, hp):
        """
        Used to update healthbar of actor
        """
        self._current_hp = hp

    def advance(self):
        pass
