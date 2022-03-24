import arcade


class KeyboardService(arcade.View):
    """
    Handles the keyboard inputs for the game

    """

    def __init__(self):
        super().__init__()

    def check_keys(self, item, keys, view1, view2=0):
        """
        Checks if a certain key is being pressed
        """
        if arcade.key.LEFT in keys:
            item.turn_left()

        if arcade.key.RIGHT in keys:
            item.turn_right()

        if arcade.key.UP in keys:
            item.engine("forward")

        if arcade.key.DOWN in keys:
            item.engine("reverse")

        elif arcade.key.Q in keys:
            arcade.close_window()
