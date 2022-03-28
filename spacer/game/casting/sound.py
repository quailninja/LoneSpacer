import arcade
from constants import *


class Sound:
    """Sound is used to create effects and music

    The responsibility of the sound class is to play sounds.

    Attributes:
        _sound (class): Loads a sound file
        _player (int): What player is being used for the sound
    """

    def __init__(self, file):
        self._sound = arcade.Sound(file)
        self._player = 0

    def play_music_effect(self, repeat=False):
        """Play music or effect

        Args:
            repeat (bool, optional): Whether sound will repeat. Defaults to False.
        """
        self._player = self._sound.play(loop=repeat)

    def stop(self):
        """Stop music from playing, this is only for sounds that repeat was True"""
        self._player.pause()
        self._player.delete()


class Sounds:
    """Sounds used to track all sounds in the game

    The responsibility of the healthbar class is to keep track of an actors health.

    Attributes:
        _sound_list (dict): Dictionary used to keep track off all sound in the game.
    """

    def __init__(self):
        self._sound_list = {
            "player_laser": Sound(PLAYER_LASER),
            "enemy_laser": Sound(ENEMY_LASER),
            "explosion": Sound(EXPLOSION),
            "background": Sound(BACKGROUND_MUSIC),
            "title": Sound(TITLE_MUSIC),
            "missile": Sound(MISSILE),
        }

    def play_sound(self, key, loop=False):
        """
        Plays a sound based on key
        """
        self._sound_list[key].play_music_effect(loop)

    def stop_sound(self, key):
        """Stops the sound from playing.  Only need if loop was true in play sound.

        Args:
            key (dict key): The dictionary item that is playing sound
        """
        self._sound_list[key].stop()

    def advance(self):
        """Not Implemented"""
        pass

    def draw(self):
        """Not Implemented"""
        pass
