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
        """Changes position of the point

        Args:
            x (int): Changes the x position of the point
            y (int): Changes the y position of the point
        """
        self._x = x
        self._y = y

    def get_x(self):
        """Returns the x position of the point

        Returns:
            int: Returns x
        """
        return self._x

    def get_y(self):
        """Returns the y position of the point

        Returns:
            int: Returns y
        """
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
        """Changes velocity of an object

        Args:
            dx (int): changes the x direction
            dy (int): changes the y direction
        """
        self._dx = dx
        self._dy = dy

    def get_dx(self):
        """Returns x direciton

        Returns:
            int: Returns dx
        """
        return self._dx

    def get_dy(self):
        """Returns y direciton

        Returns:
            int: Returns dy
        """
        return self._dy
