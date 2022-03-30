from game.casting.actor import Actor
from constants import *


class Announcement(Actor):
    """
    Bullets

    This class is responsible for all bullets in the game.

    """

    def __init__(self, message):
        """
        :parm angle: This is the ships current angle
        :parm ship_x: Ships x location
        :parm ship_y: Ships y Location
        :parm ship_dx: Ships speed on x axis
        :parm ship_dy: Ships speed on Y axis
        :parm img: Image Bullet will use
        parmaters get the ships current angel, location and speed and then match it
        and adds bullet speed.
        """
        super().__init__()
        self.change_life(ANNOUNCEMENT_TIME)
        self._center.change_position(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self._message = message

    def draw(self):
        arcade.draw_text(
            self._message,
            self._center._x,
            self._center._y,
            arcade.color.WHITE,
            self._font_size,
            font_name=self._font,
        )

    def advance(self):
        """
        The advance was changed so that the bullet will die after so many frames
        each from update takes one life from the bullet
        """
        super().advance()
        self._life -= 1
