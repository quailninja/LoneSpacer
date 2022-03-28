import arcade
import arcade.gui
from constants import *
from game.screens.instruction_screen import InstructionView

# TODO - Figure out how to add restart button
class PauseScreen(arcade.View):
    """Pause Screen

    This is the pause screen, it pauses the game:

    Attributes:
        _background_img: Loads background image for game
        manager (class): Creates an instance of a UImanager class from arcade
        game_view (class): Current game state
        v_box (class): Controls layout of pause menu, instance of UIBoxLayout
    """

    def __init__(self, game_view):
        """Initiates pause screen

        Args:
            game_view (game_view): Current state of the game
        """
        super().__init__()
        self._background_img = arcade.load_texture(BACKGROUND_IMG)
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.game_view = game_view
        self.v_box = arcade.gui.UIBoxLayout()

        title = arcade.gui.UITextArea(
            text="PAUSED",
            width=220,
            height=75,
            font_size=30,
            font_name=TITLE_FONT,
        )
        # self.game_view._cast.get_first_actor(SOUND_GROUP).pause()

        self.v_box.add(title).with_space_around(bottom=20)

        resume_button = arcade.gui.UIFlatButton(text="Resume", width=200)
        self.v_box.add(resume_button.with_space_around(bottom=20))

        control_button = arcade.gui.UIFlatButton(text="Controls", width=200)
        self.v_box.add(control_button.with_space_around(bottom=20))

        quit_button = arcade.gui.UIFlatButton(text="Quit", width=200)
        self.v_box.add(quit_button.with_space_around(bottom=20))

        resume_button.on_click = self.on_resume
        control_button.on_click = self.on_controls
        quit_button.on_click = self.on_quit

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x", anchor_y="center_y", child=self.v_box
            )
        )

    def on_resume(self, event: arcade.gui.UIOnClickEvent):
        """Resumes game

        Args:
            event (arcade.gui.UIOnClickEvent): Tracks mouse
        """
        self.window.show_view(self.game_view)

    def on_controls(self, event: arcade.gui.UIOnClickEvent):
        """Shows InstructionView

        Args:
            event (arcade.gui.UIOnClickEvent): Tracks mouse
        """
        self.window.show_view(InstructionView(self))

    def on_quit(self, event: arcade.gui.UIOnClickEvent):
        """Quits the game

        Args:
            event (arcade.gui.UIOnClickEvent): Tracks mouse
        """
        arcade.exit()

    def on_draw(self):
        """Draws everything on the screen"""
        self.clear()
        arcade.draw_lrwh_rectangle_textured(
            0, 0, self.window.width, self.window.height, self._background_img
        )
        self.game_view._cast.get_first_actor(SCORE_GROUP).draw()
        self.game_view._cast.get_first_actor(LEVEL_GROUP).draw()
        self.game_view._cast.get_first_actor(SHIP_GROUP).draw()
        self.game_view._cast.get_first_actor(HEALTH_GROUP).draw()
        self.manager.draw()
