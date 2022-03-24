from constants import *
from game.screens.start_screen import StartScreen
import arcade
from pyglet import font
from game.casting.sound import Sounds

font.add_file("spacer/assets/text/SpaceMission-rgyw9.otf")
font.add_file("spacer/assets/text/RaceGuard-7bPoE.otf")


def main():
    """Main Function

    This starts the arcade window and gives the start view
    """

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = StartScreen()
    Sounds().play_sound("background", True)
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
