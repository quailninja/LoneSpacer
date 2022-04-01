import arcade
from constants import *


class EndView(arcade.View):
    """Won/Loss Screen
    This is the end of game and will either show Victory or Defeat
    Attributes:
        win (bool): If the game was won or lost
        game_view (class): Game Screen used to show score
    """

    def __init__(self, win, game_view):
        super().__init__()
        self.win = win
        self._game_view = game_view

    def on_draw(self):
        """Draws users view
        Args:
            Instructions given to user on screen using arcades draw_text function
        """
        background_img = arcade.load_texture(BACKGROUND_IMG)

        self.clear()
        arcade.draw_lrwh_rectangle_textured(
            0, 0, self.window.width, self.window.height, background_img
        )
        start_y = self.window.height / 2 + 150
        start_x = self.window.width / 2
        if self.win:
            arcade.draw_text(
                "Victory!!!!",
                start_x,
                start_y,
                arcade.color.WHITE,
                font_size=TITLE_FONT_SIZE,
                anchor_x="center",
                font_name=TITLE_FONT,
            )

        else:
            arcade.draw_text(
                "Defeat",
                start_x,
                start_y,
                arcade.color.WHITE,
                font_size=TITLE_FONT_SIZE,
                anchor_x="center",
                font_name=TITLE_FONT,
            )

        start_y -= DEFAULT_LINE_HEIGHT
        arcade.draw_text(
            "Thanks for playing.",
            start_x,
            start_y,
            arcade.color.WHITE,
            font_size=DEFAULT_FONT_SIZE,
            anchor_x="center",
            font_name=HUD_FONT_NAME,
        )
        start_y -= DEFAULT_LINE_HEIGHT
        arcade.draw_text(
            "Press Escape to Exit",
            start_x,
            start_y,
            arcade.color.WHITE,
            font_size=14,
            anchor_x="center",
            font_name=HUD_FONT_NAME,
        )
        self._game_view._cast.get_first_actor(SCORE_GROUP).draw()

    def on_key_press(self, key, key_modifiers):
        """Waits to detect mouse click from user
        Args:
            uses arcades on_mouse_press to detect mouse click
            then it changes the screen
        """
        if key == arcade.key.ESCAPE:
            arcade.exit()

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass
