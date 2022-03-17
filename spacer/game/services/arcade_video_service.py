import arcade


class ArcadeVideoService:
    def __init__(self):

        self.duck = 0

    def draw_image(self, x, y, texture, scale, angle, alpha):
        arcade.draw_scaled_texture_rectangle(x, y, texture, scale, angle, alpha)
