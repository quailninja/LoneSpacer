import arcade
from constants import *


class InstructionView(arcade.View):
    """Instruction Screen
    This is the first screen shown to players when the game starts.
    Attributes:
        return_view (class): Previous screen
    """

    def __init__(self):
        super().__init__()
        self.return_view = 0

    def setup(self, view):
        self.return_view = view

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
        key_up_down = arcade.load_texture("spacer/assets/images/key_up_down.png")
        key_right_left = arcade.load_texture("spacer/assets/images/key_right_left.png")
        key_escape = arcade.load_texture("spacer/assets/images/key_esc.png")
        spacebar = arcade.load_texture("spacer/assets/images/spacebar.png")
        key_p = arcade.load_texture("spacer/assets/images/key_p.png")
        key_s = arcade.load_texture("spacer/assets/images/key_s.png")
        background_img = arcade.load_texture(BACKGROUND_IMG)

        self.clear()
        arcade.draw_lrwh_rectangle_textured(
            0, 0, self.window.width, self.window.height, background_img
        )
        arcade.draw_scaled_texture_rectangle(
            SCREEN_WIDTH - 15, SCREEN_HEIGHT - 15, x_key, 1.2
        )
        start_y = self.window.height - 100
        start_x = self.window.width / 2
        arcade.draw_text(
            "Controls",
            start_x,
            start_y,
            arcade.color.WHITE,
            font_size=TITLE_FONT_SIZE,
            anchor_x="center",
            font_name=TITLE_FONT,
        )

        start_y -= TITLE_LINE_HEIGHT
        arcade.draw_scaled_texture_rectangle(start_x - 80, start_y + 10, spacebar, 0.13)
        arcade.draw_text(
            "= Fire",
            start_x + 30,
            start_y,
            arcade.color.WHITE,
            font_size=DEFAULT_FONT_SIZE,
            anchor_x="center",
            font_name=HUD_FONT_NAME,
        )
        start_y -= DEFAULT_LINE_HEIGHT
        arcade.draw_scaled_texture_rectangle(
            start_x - 35, start_y + 10, key_up_down, 0.15
        )
        arcade.draw_text(
            "= Move the Ship",
            start_x + 90,
            start_y,
            arcade.color.WHITE,
            font_size=DEFAULT_FONT_SIZE,
            anchor_x="center",
            font_name=HUD_FONT_NAME,
        )
        start_y -= DEFAULT_LINE_HEIGHT
        arcade.draw_scaled_texture_rectangle(
            start_x - 50, start_y + 10, key_right_left, 0.15
        )
        arcade.draw_text(
            "= Turn the Ship",
            start_x + 90,
            start_y,
            arcade.color.WHITE,
            font_size=DEFAULT_FONT_SIZE,
            anchor_x="center",
            font_name=HUD_FONT_NAME,
        )
        start_y -= DEFAULT_LINE_HEIGHT
        arcade.draw_scaled_texture_rectangle(
            start_x - 34, start_y + 10, key_escape, 0.18
        )
        arcade.draw_text(
            "= Pause",
            start_x + 45,
            start_y,
            arcade.color.WHITE,
            font_size=DEFAULT_FONT_SIZE,
            anchor_x="center",
            font_name=HUD_FONT_NAME,
        )

        start_y -= DEFAULT_LINE_HEIGHT
        arcade.draw_scaled_texture_rectangle(start_x - 34, start_y + 10, key_p, 0.18)
        arcade.draw_text(
            "= Show FPS",
            start_x + 50,
            start_y,
            arcade.color.WHITE,
            font_size=DEFAULT_FONT_SIZE,
            anchor_x="center",
            font_name=HUD_FONT_NAME,
        )

        start_y -= DEFAULT_LINE_HEIGHT

        arcade.draw_scaled_texture_rectangle(start_x - 34, start_y + 10, key_s, 0.18)
        arcade.draw_text(
            "= Shield",
            start_x + 45,
            start_y,
            arcade.color.WHITE,
            font_size=DEFAULT_FONT_SIZE,
            anchor_x="center",
            font_name=HUD_FONT_NAME,
        )

        start_y -= DEFAULT_LINE_HEIGHT

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """Waits to detect mouse click from user
        Args:
            uses arcades on_mouse_press to detect mouse click
            then it changes the screen
        """
        if (
            SCREEN_WIDTH - 5 > _x > SCREEN_WIDTH - 25
            and SCREEN_HEIGHT - 5 > _y > SCREEN_HEIGHT - 25
        ):
            self.window.show_view(self.return_view)

    def on_key_press(self, key, key_modifiers):
        """Keeps track of all keys that are pressed

        Args:
            key (int): What key is being pressed
            key_modifiers (int): I think this is also an integer.
            Checks to see if any modifiers like the shift key are being held down.
        """
        if key == arcade.key.ESCAPE:
            self.window.show_view(self.return_view)
