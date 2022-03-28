import arcade


class KeyboardService(arcade.View):
    """
    Handles the keyboard inputs for the game

    """

    def __init__(self):
        super().__init__()

    def check_keys(self, player, keys):
        """
        Checks if a certain key is being pressed
        """
        if arcade.key.LEFT in keys:
            player.turn_left()

        if arcade.key.RIGHT in keys:
            player.turn_right()

        if arcade.key.UP in keys:
            player.engine("forward")

        if arcade.key.DOWN in keys:
            player.engine("reverse")

        if arcade.key.Q in keys:
            arcade.close_window()
