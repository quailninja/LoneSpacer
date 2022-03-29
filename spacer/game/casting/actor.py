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
        _radius(int) = The size of the Actor
        _angle (int) = The direction the texture is facing
        _speed (int) = How fast the Actor can move.
        _scale (int) = Size of the texture
        _life (int) = The actors life
        _font_size (int) = Font size for text based actors.
        _font (str) = Type of font for text based actors
    """

    def __init__(self, img=0):
        """
        :parm img: Image for bullet, default is 0
        """
        self._center = Point()
        self._velocity = Velocity()
        self._alive = True
        if img != 0:
            self._texture = arcade.load_texture(img)
        self._radius = 0
        self._angle = 0
        self._speed = 0
        self._scale = 1
        self._life = 1
        self._font_size = HUD_FONT_SIZE
        self._font = HUD_FONT_NAME

    def advance(self):
        """
        All objects will use this to move on screen.  This will also do a life check.
        """
        self.wrap()
        self._center._x += self._velocity._dx
        self._center._y += self._velocity._dy
        if self._life < 1:
            self._alive = False

    def draw(self):
        """
        All objects will use this to render on screen
        """
        arcade.draw_scaled_texture_rectangle(
            self._center._x, self._center._y, self._texture, self._scale, self._angle
        )

    def wrap(self):
        """
        Moves actor from one side of the screen to the other
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

    def change_angle(self, num):
        """Changes angle"""
        self._angle = num

    def change_scale(self, num):
        """Changes scale
        :parm num: integer
        """
        self._scale = num

    def change_radius(self, num):
        """Changes radius
        :parm num: integer
        """
        self._radius = num

    def change_font(self, font):
        """Changes angle_correct
        :parm font: string, font name
        """
        self._font = font

    def change_font_size(self, num):
        """Changes angle_correct
        :parm num: integer
        """
        self._font_size = num

    def change_speed(self, num):
        """Changes _speed
        :parm num: integer
        """
        self._speed = num

    def change_life(self, num):
        """Changes _life
        :parm num: integer
        """
        self._life = num

    def kill(self):
        """changes _alive to false"""
        self._alive = False

    def add_damage(self, num):
        """Adds damage amount to actor"""
        self._life -= num

    def get_life(self):
        """
        Returns Actors current life
        """
        return self._life
