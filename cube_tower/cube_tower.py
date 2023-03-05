from enum import Enum
from cube import Cube
from random import randint, choice


class CubeColor(Enum):
    WHITE = 0
    BLACK = 1


class CubeTower:
    """
        A class representing a tower made of cubes.

        Attributes:
        tower (list): A list of Cube objects representing the tower.

        Methods:
        __init__(): Creates an empty CubeTower object.
        __str__(): Returns a string representation of the CubeTower object.
        add_cube(cube): Adds a Cube object to the top of the tower if the cube meets certain conditions.
        randomize_tower(): Static method that generates a random amount of cubes.
        """

    def __init__(self):
        self.tower = None

    def __str__(self):
        if self.tower is not None:
            return "".join([f"{i}-" + self.tower[i].__str__() + '\n' for i in range(len(self.tower) - 1, 0, -1)])

    def add_cube(self, cube):
        """
            Adds a Cube object to the top of the tower if the cube meets certain conditions.
            new cube must be different color and smaller in surface then current top cube in the tower

            Args:
            cube (Cube): The Cube object to add to the tower.

            Returns:
            None
        """
        if self.tower is None:
            self.tower = [cube]
        else:
            top_index = len(self.tower) - 1
            top_cube_color = self.tower[top_index].color
            top_cube_length = self.tower[top_index].base.get_surface()
            if top_cube_color != cube.color and top_cube_length > cube.base.get_surface():
                self.tower.append(cube)

    @staticmethod
    def randomize_tower():
        """
            Generates a random tower of cubes.

            Yields:
            Cube: A Cube object with random edge length and color.
        """
        n = randint(1, 101)
        for i in range(n):
            edge = randint(1, 101)
            color = choice([CubeColor.WHITE, CubeColor.BLACK])
            yield Cube(edge, color)

