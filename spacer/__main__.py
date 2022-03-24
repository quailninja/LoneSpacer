from constants import *
from game.screens.start_screen import StartScreen
import arcade
from pyglet import font


font.add_file("spacer/assets/text/SpaceMission-rgyw9.otf")
font.add_file("spacer/assets/text/RaceGuard-7bPoE.otf")


def main():
    """Main Function

    This starts the arcade window and gives the start view
    """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, fullscreen=True)
    WIDTH, HEIGHT = window.get_size()
    window.set_viewport(0, WIDTH, 0, HEIGHT)
    start_view = StartScreen()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
