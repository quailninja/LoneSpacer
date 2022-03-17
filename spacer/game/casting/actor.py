import arcade
from game.casting.point import *
from constants import *


class Actor(arcade.Sprite):

    """
    This is the standard for all objects in the game.
    """

    def __init__(self, img):
        self._center = Point()
        self._velocity = Velocity()
        self._alive = True
        self._texture = arcade.load_texture(img)
        self._radius = 0
        self._direction = 0
        self._angle = 0
        self._speed = 0
        self._direction = 0
        self._scale = 1

    def advance(self):
        """
        All objects will use this to move on screen
        """
        self.wrap()
        self._center._x += self._velocity._dx
        self._center._y += self._velocity._dy

    def draw(self):
        """
        All objects will use this to render on screen
        """
        arcade.draw_scaled_texture_rectangle(
            self._center._x, self._center._y, self._texture, self._scale, self._angle
        )

    def wrap(self):
        """
        This allows objects to appear if they are moving from top to bottom by adding
        or subtracting the width and the height
        """
        if self._center._x < 0:
            self._center._x += SCREEN_WIDTH
        if self._center._x > SCREEN_WIDTH:
            self._center._x -= SCREEN_WIDTH
        if self._center._y < 0:
            self._center._y += SCREEN_HEIGHT
        if self._center._y > SCREEN_HEIGHT:
            self._center._y -= SCREEN_HEIGHT

    def change_texture(self, img):
        self._texture = arcade.load_texture(img)