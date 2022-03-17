from constants import *
from game.screens.instruction_screen import InstructionView
import arcade


def main():
    """Main Function

    This starts the arcade window and gives the instruction view
    """

    # Start Arcade window and pull up the instructions screen
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
