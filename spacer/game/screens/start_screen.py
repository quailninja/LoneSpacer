import arcade
import arcade.gui
from game.screens.game_screen import GameScreen
from game.screens.instruction_screen import InstructionView
from constants import *
from game.casting.debri import Debri
from game.casting.sound import Sounds


class StartScreen(arcade.View):
    def __init__(self):
        super().__init__()
        self._background_img = arcade.load_texture(BACKGROUND_IMG)
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.game_view = GameScreen()
        self.v_box = arcade.gui.UIBoxLayout()
        self.asteroid_list = []
        self.title_sound = Sounds()
        self.title_sound.play_sound("title", True)
        for x in range(7):
            asteroid = Debri()
            self.asteroid_list.append(asteroid)

        title = arcade.gui.UITextArea(
            text=SCREEN_TITLE,
            width=700,
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
        self.title_sound.stop_sound("title")
        self.window.show_view(self.game_view)

    def on_controls(self, event: arcade.gui.UIOnClickEvent):
        self.window.show_view(InstructionView(self))

    def on_quit(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(
            0, 0, self.window.width, self.window.height, self._background_img
        )
        for asteroid in self.asteroid_list:
            asteroid.draw()
        self.manager.draw()

    def update(self, delta_time):
        for asteroid in self.asteroid_list:
            asteroid.advance()
            asteroid.spin()
