import arcade
from pyglet import media


class Sound:
    def __init__(self, file):
        self._sound = arcade.Sound(file)
        self._player = 0

    def play_music_effect(self, repeat=False):
        self._player = self._sound.play(loop=repeat)

    def stop(self):
        self._player.pause()
        self._player.delete()


# class Music:
#     def __init__(self, file):
#         self._sound = media.load(file)
#         self._player = media.Player()

#     def play(self, repeat=True):
#         self._player.loop = repeat
#         self._player.queue(self._sound)
#         self._player.play()

#     def stop(self):
#         self._player.pause()
#         self._player.delete()
#         if self._player in media.Source._players:
#             media.Source._players.remove(self._player)


class Sounds:
    def __init__(self):
        self._sound_list = {
            "player_laser": Sound("spacer/assets/sounds/laser.wav"),
            "enemy_laser": Sound("spacer/assets/sounds/enemy_laser.wav"),
            "explosion": Sound("spacer/assets/sounds/explosion.wav"),
            "background": Sound("spacer/assets/sounds/background_music.mp3"),
            "title": Sound("spacer/assets/sounds/title_loop.mp3"),
        }

    def play_sound(self, key, loop=False):
        """
        Plays a sound based on key
        """
        self._sound_list[key].play_music_effect(loop)

    def stop_sound(self, key):
        self._sound_list[key].stop()

    def advance(self):
        pass

    def draw(self):
        pass
