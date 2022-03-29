import arcade
from constants import *
from game.casting.cast import Cast
from game.casting.ship import Ship
from game.casting.shield import Shield
from game.casting.score import Score
from game.casting.level import Level
from game.casting.health_bar import HealthBar
from game.casting.shield_bar import ShieldBar
from game.services.keyboard_services import KeyboardService
from game.services.fps import FPS
from game.scripting.check_alive import CheckAlive
from game.scripting.enemy_fire import EnemyFire
from game.scripting.check_collision import CheckCollision
from game.scripting.explosion import Explosion
from game.scripting.smoke_effect import SmokeEffect
from game.scripting.spawn_enemies import SpawnEnemies
from game.scripting.update_hud import UpdateHUD
from game.scripting.script import Script
from game.scripting.check_level import CheckLevel
from game.scripting.check_win import CheckWin
from game.screens.pause_screen import PauseScreen
from game.screens.win_loss_screen import EndView
from game.scripting.hud import HUD


class GameScreen(arcade.View):
    """Game Screen

    This is the main game screen, it keeps track of:
    -Player keyboard input
    -Score
    -Removing and creating objects

    Attributes:
        _background_img: Loads background image for game
        _cast (class): A list of all actors in the game
        _keyboard_services(class): Tracks keys that are pressed
        _game_on (class): Players ship, needed to stop bug with keyboard services
        _held_keys (set): Keeps track of keys that are held
        _scripts (class): A list of of scripts to run
    """

    def __init__(self, sounds, demo):
        """
        Sets up the initial conditions of the game

        """
        super().__init__()
        self._background_img = arcade.load_texture(BACKGROUND_IMG)
        self._cast = Cast()
        self._cast.add_actor(SHIP_GROUP, Ship())
        self._cast.add_actor(LEVEL_GROUP, Level(demo))
        self._cast.add_actor(SCORE_GROUP, Score())
        self._cast.add_actor(HUD_GROUP, HealthBar())
        self._cast.add_actor(HUD_GROUP, ShieldBar())
        self._cast.add_actor(SOUND_GROUP, sounds)
        self._keyboard_services = KeyboardService()
        self._fps = FPS()
        self._game_on = self._cast.get_first_actor(SHIP_GROUP)
        self._held_keys = set()
        self._scripts = Script()
        self._scripts.add_action("update", SpawnEnemies())
        self._scripts.add_action("update", EnemyFire())
        self._scripts.add_action("update", CheckCollision())
        self._scripts.add_action("update", Explosion())
        self._scripts.add_action("update", SmokeEffect())
        self._scripts.add_action("update", CheckLevel())
        self._scripts.add_action("update", UpdateHUD())
        self._scripts.add_action("update", CheckWin())
        self._scripts.add_action("update", CheckAlive())
        self._scripts.add_action("update", HUD())

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
        self._fps.calculate_FPS()
        arcade.draw_lrwh_rectangle_textured(
            0, 0, self.window.width, self.window.height, self._background_img
        )

        for item in self._cast.get_all_actors():
            item.draw()

        self._fps.draw_FPS()

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        start_time = self._fps.start_time()

        for object in self._cast.get_all_actors():
            object.advance()

        self._keyboard_services.check_keys(self._game_on, self._held_keys)

        self.check_win()

        for action in self._scripts.get_actions("update"):
            action.execute(self._cast)

        for object in self._cast.get_all_actors():
            object.advance()

        self._fps.processing(start_time)

    def on_key_press(self, key, key_modifiers):
        """Keeps track of all keys that are pressed

        Args:
            key (int): What key is being pressed
            key_modifiers (int): I think this is also an integer.
            Checks to see if any modifiers like the shift key are being held down.
        """
        if key == arcade.key.SPACE:
            self._keyboard_services.fire(self._cast)
            self._cast.get_first_actor(SOUND_GROUP).play_sound("player_laser")
        elif key == arcade.key.ESCAPE:
            pause = PauseScreen(self)
            self.window.show_view(pause)
        elif key == arcade.key.P:
            self._fps.turn_on_off()
        elif key == arcade.key.S:
            self._keyboard_services.shield_up(self._cast)
        elif self._game_on:
            self._held_keys.add(key)

    def on_key_release(self, key, key_modifiers):
        """Keeps track of all keys that are released

        Args:
            key (int): What key is being released
            key_modifiers (int): Other key modifiers like shift key
        """
        if key in self._held_keys:
            self._held_keys.remove(key)

    def check_win(self):
        """Checks if current game has met game ending conditions"""
        level = self._cast.get_first_actor(LEVEL_GROUP)
        if level.check_win():
            self.window.show_view(EndView(True))
        elif level.check_lost():
            self.window.show_view(EndView(False))
