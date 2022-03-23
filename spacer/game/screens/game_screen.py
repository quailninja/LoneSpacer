import arcade
from constants import *
from game.casting.cast import Cast
from game.casting.ship import Ship
from game.casting.score import Score
from game.casting.level import Level
from game.casting.bullet import Bullet
from game.services.keyboard_services import KeyboardService
from game.scripting.check_alive import CheckAlive
from game.scripting.enemy_fire import EnemyFire
from game.scripting.check_collision import CheckCollision
from game.scripting.explosion import Explosion
from game.scripting.smoke_effect import SmokeEffect
from game.scripting.spawn_enemies import SpawnEnemies
from game.scripting.script import Script
from game.screens.pause_screen import PauseScreen


class GameScreen(arcade.View):
    """Game director

    This is the main game screen, it keeps track of:
    -Player keyboard input
    -Score
    -Removing and creating objects

    Attributes:
        bag (class): player object
        flying_actors (list): all the rocks and jewels are put into this list
        score (int): the players score
    """

    def __init__(self):
        """
        Sets up the initial conditions of the game

        """
        super().__init__()
        self._background_img = arcade.load_texture(BACKGROUND_IMG)
        self._cast = Cast()
        self._cast.add_actor(SHIP_GROUP, Ship())
        self._cast.add_actor(LEVEL_GROUP, Level())
        self._cast.add_actor(SCORE_GROUP, Score())
        self._keyboard_services = KeyboardService()
        self._game_on = self._cast.get_first_actor(SHIP_GROUP)
        self._held_keys = set()
        self._scripts = Script()
        self._scripts.add_action("update", SpawnEnemies())
        self._scripts.add_action("update", EnemyFire())
        self._scripts.add_action("update", CheckCollision())
        self._scripts.add_action("update", Explosion())
        self._scripts.add_action("update", SmokeEffect())
        self._scripts.add_action("update", CheckAlive())

    def on_show(self):
        """
        Used to set the initial screen

        """
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsiblity of drawing all elements.
        """

        self.clear()
        arcade.draw_lrwh_rectangle_textured(
            0, 0, self.window.width, self.window.height, self._background_img
        )

        for item in self._cast.get_all_actors():
            item.draw()

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        for object in self._cast.get_all_actors():
            object.advance()

        self._keyboard_services.check_keys(self._game_on, self._held_keys, 0)

        for action in self._scripts.get_actions("update"):
            action.execute(self._cast)

        for object in self._cast.get_all_actors():
            object.advance()

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            ship = self._cast.get_first_actor(SHIP_GROUP)
            self._cast.add_actor(
                PLAYER_BULLET,
                Bullet(
                    ship._angle,
                    ship._center._x,
                    ship._center._y,
                    ship._velocity._dx,
                    ship._velocity._dy,
                    PLAYER_BULLET_IMG,
                ),
            )
        elif key == arcade.key.ESCAPE:
            pause = PauseScreen(self)
            self.window.show_view(pause)
        elif self._game_on:
            self._held_keys.add(key)

    def on_key_release(self, key, key_modifiers):
        if key in self._held_keys:
            self._held_keys.remove(key)
