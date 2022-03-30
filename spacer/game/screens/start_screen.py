import arcade
import arcade.gui
from game.screens.game_screen import GameScreen
from game.screens.instruction_screen import InstructionView
from constants import *
from game.casting.debris import Debris
from game.casting.sound import Sounds


class StartScreen(arcade.View):
    """Start Screen

    This is the start screen:

    Attributes:
        _background_img: Loads background image for game
        manager (class): Creates an instance of a UIManager class from arcade
        game_view (class): Current game state
        v_box (class): Controls layout of pause menu, instance of UIBoxLayout
        debris_list (list): A list of randomly generated debris items
        demo (bool): Demo mode for professor and testing
        demo_label: This lets the player know if demo mode is enabled
        sound (class): Instance of Sounds class
    """

    def __init__(self):
        super().__init__()
        self._background_img = arcade.load_texture(BACKGROUND_IMG)
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.v_box = arcade.gui.UIBoxLayout()
        self.debris_list = []
        self.demo = False
        self.demo_label = ""
        self.sounds = Sounds()
        self.sounds.play_sound("title", True)
        for x in range(DEBRIS_AMOUNT):
            debris = Debris()
            self.debris_list.append(debris)

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

        demo_button = arcade.gui.UIFlatButton(text=f"Demo Mode", width=200)
        self.v_box.add(demo_button.with_space_around(bottom=20))

        control_button = arcade.gui.UIFlatButton(text="Controls", width=200)
        self.v_box.add(control_button.with_space_around(bottom=20))

        quit_button = arcade.gui.UIFlatButton(text="Quit", width=200)
        self.v_box.add(quit_button.with_space_around(bottom=20))

        start_button.on_click = self.on_start
        quit_button.on_click = self.on_quit
        control_button.on_click = self.on_controls
        demo_button.on_click = self.on_demo

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
        self.sounds.play_sound("background", True)
        game_view = GameScreen(self.sounds, self.demo)
        self.window.show_view(game_view)

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

    def on_demo(self, event: arcade.gui.UIOnClickEvent):
        """Quits the game, in case the didn't want to play

        Args:
            event (arcade.gui.UIOnClickEvent): tracks mouse
        """
        if self.demo:
            self.demo = False
            self.demo_label = ""
        else:
            self.demo = True
            self.demo_label = "Demo Mode On"

    def on_draw(self):
        """Draws everything on start screen"""
        self.clear()
        arcade.draw_lrwh_rectangle_textured(
            0, 0, self.window.width, self.window.height, self._background_img
        )
        for debris in self.debris_list:
            debris.draw()
        self.manager.draw()
        arcade.draw_text(
            self.demo_label,
            20,
            SCREEN_HEIGHT - 20,
            arcade.color.WHITE,
            font_size=DEFAULT_FONT_SIZE,
            font_name=HUD_FONT_NAME,
        )

    def update(self, delta_time):
        """Moves all debris on the screen

        Args:
            delta_time (_type_): tells us how much time has actually elapsed
        """
        for debris in self.debris_list:
            debris.advance()
            debris.spin()

        self.manager
