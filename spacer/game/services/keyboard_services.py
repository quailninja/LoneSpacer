import arcade
from constants import *
from game.casting.bullet import Bullet
from game.casting.shield import Shield


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

    def fire(self, cast):
        """Fires ships laser

        Args:
            cast (list): list of actors in the game
        """
        ship = cast.get_first_actor(SHIP_GROUP)
        cast.add_actor(
            PLAYER_BULLET,
            Bullet(
                ship._angle,
                ship._center._x,
                ship._center._y,
                ship._velocity._dx,
                ship._velocity._dy,
                PLAYER_BULLET_IMG,
                LOW_DAMAGE,
            ),
        )
        cast.get_first_actor(SOUND_GROUP).play_sound("player_laser")

    def shield_up(self, cast):
        """Sets ship shields

        Args:
            cast (list): list of actors in the game
        """
        ship = cast.get_actors(SHIP_GROUP)
        shield_status = cast.get_actors(SHIELD_GROUP)
        if len(shield_status) < 1 and len(ship) > 0:
            if ship[0].get_shield_count() > 0:
                cast.add_actor(
                    SHIELD_GROUP,
                    Shield(ship[0], SHIELD_IMG),
                )
                ship[0].remove_shield(1)
                cast.get_first_actor(SOUND_GROUP).play_sound("shield_up")
