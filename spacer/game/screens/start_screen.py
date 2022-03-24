import arcade
import arcade.gui
from game.screens.game_screen import GameScreen
from game.screens.instruction_screen import InstructionView
from constants import *
from game.casting.debri import Debri
from game.casting.sound import Sounds

# TODO - Add demo button to make game shorter
class StartScreen(arcade.View):
    """Start Screen

    This is the start screen:

    Attributes:
        _background_img: Loads background image for game
        manager (class): Creates an instance of a UImanager class from arcade
        game_view (class): Current game state
        v_box (class): Controls layout of pause menu, instance of UIBoxLayout
        debri_list (list): A list of randomly generated debri items
        title_sound (class): Instances of Sounds class
    """

    def __init__(self):
        super().__init__()
        self._background_img = arcade.load_texture(BACKGROUND_IMG)
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.v_box = arcade.gui.UIBoxLayout()
        self.debri_list = []
        self.sounds = Sounds()
        self.sounds.play_sound("title", True)
        self.game_view = GameScreen(self.sounds)
        for x in range(7):
            debri = Debri()
            self.debri_list.append(debri)

        title = arcade.gui.UITextArea(
            text=SCREEN_TITLE,
            width=685,
            height=75,
            font_size=TITLE_SIZE,
            font_name=TITLE_FONT,
        )
        self.v_box.add(title).with_space_around(bottom=20)

        start_button = arcade.gui.UIFlatButton(text="Start", width=200)
        self.v_box.add(start_button.with_space_around(bottom=20))

        control_button = arcade.gui.UIFlatButton(text="Controls", width=200)
        self.v_box.add(control_button.with_space_around(bottom=20))

        quit_button = arcade.gui.UIFlatButton(text="Quit", width=200)
        self.v_box.add(quit_button.with_space_around(bottom=20))

        start_button.on_click = self.on_start
        quit_button.on_click = self.on_quit
        control_button.on_click = self.on_controls

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x", anchor_y="center_y", child=self.v_box
            )
        )

    def on_start(self, event: arcade.gui.UIOnClickEvent):
        """Start Button - it starts the game

        Args:
            event (arcade.gui.UIOnClickEvent): tracks mouse
        """
        self.sounds.stop_sound("title")
        self.sounds.play_sound("background")
        self.window.show_view(self.game_view)

    def on_controls(self, event: arcade.gui.UIOnClickEvent):
        """Shows the instruction screen

        Args:
            event (arcade.gui.UIOnClickEvent): tracks mouse
        """
        self.window.show_view(InstructionView(self))

    def on_quit(self, event: arcade.gui.UIOnClickEvent):
        """Quits the game, in case the didn't want to play

        Args:
            event (arcade.gui.UIOnClickEvent): tracks mouse
        """
        arcade.exit()

    def on_draw(self):
        """Draws everything on start screen"""
        self.clear()
        arcade.draw_lrwh_rectangle_textured(
            0, 0, self.window.width, self.window.height, self._background_img
        )
        for debri in self.debri_list:
            debri.draw()
        self.manager.draw()

    def update(self, delta_time):
        """Moves all debri on the screen

        Args:
            delta_time (_type_): tells us how much time has actually elapsed
        """
        for debri in self.debri_list:
            debri.advance()
            debri.spin()
