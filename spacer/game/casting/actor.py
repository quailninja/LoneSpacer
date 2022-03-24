import arcade
from game.casting.point import *
from constants import *


class Actor(arcade.Sprite):
    """A base class for most objects in the game.

    This will be the class that is inherited from for most objects in the game.add()

    Attributes:
        _center(class) = The Point class, the actors current position.
        _velocity(class) = The Velocity class, the actors direction.
        _alive(boolean) = Wether the Actor is dead or alive.
        _texture(method) = Set the image on screen to display of Actor
        _radius = The size of the Actor
        _angle = The direction the texture is facing
        _speed = How fast the Actor can move.
        _scale = Size of the texture
    """

    def __init__(self, img=0, sound=0):
        self._center = Point()
        self._velocity = Velocity()
        self._alive = True
        if img != 0:
            self._texture = arcade.load_texture(img)
        self._radius = 0
        self._angle = 0
        self._speed = 0
        self._scale = 1

    def advance(self):
        """
        All objects will use this to move on screen.  All life checks
        for objects that can be destroyed should be put in this function.
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
            self._center._y += SCREEN_HEIGHT - HUD_SPACE
        if self._center._y > SCREEN_HEIGHT - HUD_SPACE:
            self._center._y -= SCREEN_HEIGHT - HUD_SPACE

    def change_texture(self, img):
        """
        This will allow the players to change the texture of a given actor.
        """
        self._texture = arcade.load_texture(img)

    def load_sound(self, file):
        self._sound = arcade.load_sound(file)

    def play_sound(self):
        arcade.play_sound(self._sound)
