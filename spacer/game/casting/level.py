from constants import *
import random as r
from game.casting.actor import Actor


class Level(Actor):
    """Keeps track of current level

    The responsibility of the level class is the keep track of what level the player is on.

    Attributes:
        _level (int): The game level
        _spawn_rate (int): How fast Enemies spawn
    """

    def __init__(self, demo):
        super().__init__()
        self._level = 1
        self._spawn_rate = MEDIUM_SPAWN_RATE
        self._center.change_position(20, SCREEN_HEIGHT - HUD_SPACE)
        self._demo = demo
        self._boss = False
        self._win = False
        self._lost = False

    def level_1_spawn(self):
        """Returns a 1

        Returns:
            int: Returns 1
        """
        return 1

    def level_2_spawn(self):
        """Level 2 enemy spawns

        Returns:
            int: Returns a 1 or 2
        """
        spawn_chance = r.randint(1, 100)
        if spawn_chance < 70:
            return 1
        else:
            return 2

    def level_3_spawn(self):
        """Level 3 enemy spawns

        Returns:
            int: Returns 1; 2 or 3
        """
        spawn_chance = r.randint(1, 100)
        if spawn_chance < 60:
            return 1
        elif spawn_chance < 80:
            return 2
        else:
            return 3

    def level_4_spawn(self):
        """Level 4 enemy spawns

        Returns:
            int: Returns 1; 2; 3; or 4
        """
        spawn_chance = r.randint(1, 100)
        if spawn_chance < 35:
            return 1
        elif spawn_chance < 60:
            return 2
        elif spawn_chance < 90:
            return 3
        else:
            return 4

    def level_up(self):
        """Increases current level"""
        self._level += 1

    def get_level(self):
        """Returns current level

        Returns:
            int: Returns _level
        """
        return self._level

    def set_boss(self):
        """Sets the game as lost"""
        self._boss = True

    def set_loss(self):
        """Sets the game as lost"""
        self._lost = True

    def set_win(self):
        """Sets the game as lost"""
        self._win = True

    def check_win(self):
        """Checks for win

        Returns:
            bool: Return True or False
        """
        return self._win

    def check_lost(self):
        """Checks for player loss

        Returns:
            bool: Return True or False
        """
        return self._lost

    def get_spawn_rate(self):
        """Returns spawn rate

        Returns:
            int: Returns _spawn_rate
        """
        return self._spawn_rate

    def get_boss(self):
        """Returns _boss status

        Returns:
            int: Returns True or False
        """
        return self._boss

    def get_demo_mode(self):
        """Returns if game is in demo mode

        Returns:
            int: Returns _demo
        """
        return self._demo

    def draw(self):
        """Draws current level as integer unless it's a boss level"""
        if self._level < 5:
            arcade.draw_text(
                f"Level: {self._level}",
                self._center._x,
                self._center._y,
                arcade.color.WHITE,
                self._font_size,
                font_name=self._font,
            )
        else:
            arcade.draw_text(
                f"Level: BOSS",
                self._center._x,
                self._center._y,
                arcade.color.WHITE,
                self._font_size,
                font_name=self._font,
            )

    def advance(self):
        """Not used"""
        pass
