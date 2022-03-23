class Point:
    """Point

    This class is used to help keep track of where all objects are in the game.

    Attributes:
        _x (int): x axis point
        _y (int): y axis point
    """

    def __init__(self):
        self._x = 0
        self._y = 0

    def change_position(self, x, y):
        self._x = x
        self._y = y

    def add_xy(self):
        self._x += 5
        self._y += 5

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y


class Velocity:
    """Velocity

    This keeps track of how fast moving objects are going

    Attributes:
        dx (int): how fast an object moves on the x axis point
        dy (int): how fast an ojbect moves on the y axis point

    """

    def __init__(self):
        self._dx = 0
        self._dy = 0

    def change_velocity(self, dx, dy):
        self._x = dx
        self._y = dy

    def change_angle(self):
        pass

    def get_dx(self):
        return self._dx

    def get_dy(self):
        return self._dy
