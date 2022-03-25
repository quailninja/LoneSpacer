import arcade
from constants import *


class EndView(arcade.View):
    """Instruction Screen
    This is the first screen shown to players when the game starts.
    Attributes:
        return_view (class): Previous screen
    """

    def __init__(self, win):
        super().__init__()
        self.win = win

    def on_show(self):
        """Updates the background and resets user view
        Args:
            changes back ground color and also the viewport the view port change doesn't seem necessary
        """
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        """Draws users view
        Args:
            Instructions given to user on screen using arcades draw_text function
        """
        x_key = arcade.load_texture("spacer/assets/images/numeralX.png")
        background_img = arcade.load_texture(BACKGROUND_IMG)

        self.clear()
        arcade.draw_lrwh_rectangle_textured(
            0, 0, self.window.width, self.window.height, background_img
        )
        arcade.draw_scaled_texture_rectangle(
            SCREEN_WIDTH - 15, SCREEN_HEIGHT - 15, x_key, 1.2
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
            "Click to exit",
            start_x,
            start_y,
            arcade.color.WHITE,
            font_size=14,
            anchor_x="center",
            font_name=HUD_FONT_NAME,
        )

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """Waits to detect mouse click from user
        Args:
            uses arcades on_mouse_press to detect mouse click
            then it changes the screen
        """
        arcade.exit()
