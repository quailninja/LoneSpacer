import arcade


class Sound:
    def __init__(self, file):
        self._sound = arcade.load_sound(file)

    def play(self, loop):
        arcade.play_sound(self._sound, looping=loop)


class Sounds:
    def __init__(self):
        self._sound_list = {
            "player_laser": Sound("spacer/assets/sounds/laser.wav"),
            "enemy_laser": Sound("spacer/assets/sounds/enemy_laser.wav"),
            "explosion": Sound("spacer/assets/sounds/explosion.wav"),
            "background": Sound("spacer/assets/sounds/background_music.mp3"),
        }

    def play_sound(self, key, loop=False):
        """
        Plays a sound based on key
        """
        self._sound_list[key].play(loop)

    def advance(self):
        pass

    def draw(self):
        pass
