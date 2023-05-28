from square import Square
from cube_color import CubeColor

class Cube:
    """
        A class to represent a cube object.

        Attributes:
        -----------
        base : Square
            The square object representing the base of the cube.
        color : CubeColor
            The color of the cube, defined by the CubeColor enum.

        Methods:
        --------
        get_volume() -> float:
            Returns the volume of the cube.
        get_surface() -> float:
            Returns the surface area of the cube.
        """

    def __init__(self, length: int, color: CubeColor):
        self.base = Square(length)
        self.color = color

    def __str__(self):
        return f"Cube: {self.base.__str__()} color: {self.color}"

    def get_volume(self):
        return pow(self.base.edge_length, 3)

    def get_surface(self):
        return 6 * self.base.get_surface()
