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

    def __init__(self, game_view, sound):
        """Initiates pause screen

        Args:
            game_view (game_view): Current state of the game
        """
        super().__init__()
        self._background_img = arcade.load_texture(BACKGROUND_IMG)
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.game_view = game_view
        self.sounds = sound
        self.v_box = arcade.gui.UIBoxLayout()

        title = arcade.gui.UITextArea(
            text="PAUSED",
            width=220,
            height=75,
            font_size=30,
            font_name=TITLE_FONT,
        )

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
        instruction_view = InstructionView()
        instruction_view.setup(self)
        self.window.show_view(instruction_view)

    def on_quit(self, event: arcade.gui.UIOnClickEvent):
        """Quits the game

        Args:
            event (arcade.gui.UIOnClickEvent): Tracks mouse
        """
        arcade.exit()

    def on_draw(self):
        """Draws everything on the screen"""
        self.clear()
        self.window.set_mouse_visible(True)
        arcade.draw_lrwh_rectangle_textured(
            0, 0, self.window.width, self.window.height, self._background_img
        )
        game_screen = self.game_view._cast.get_all_actors()
        for item in game_screen:
            item.draw()

        self.manager.draw()

    def on_key_press(self, key, key_modifiers):
        """Keeps track of all keys that are pressed

        Args:
            key (int): What key is being pressed
            key_modifiers (int): I think this is also an integer.
            Checks to see if any modifiers like the shift key are being held down.
        """
        if key == arcade.key.ESCAPE:
            self.window.show_view(self.game_view)
