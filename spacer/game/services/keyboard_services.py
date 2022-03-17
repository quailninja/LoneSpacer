import arcade


class KeyboardService(arcade.View):
    """
    Handles the keyboard inputs for the game

    Attributes:
        _item_move (class): A class that can be moved by the player
        move_speed (int): how fast the player can move the object
        width (int): screen width
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

        if arcade.key.ESCAPE in keys:
            self.window.show_view(view1)

        elif arcade.key.Q in keys:
            arcade.close_window()

        elif arcade.key.ENTER and view2 != 0:
            self.window.show_view(view2)
