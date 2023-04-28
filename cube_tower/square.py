class Square:
    """
      A class representing a square with a given edge length.

      Attributes:
      -----------
      edge_length : int or float
          The length of the edges of the square.

      Methods:
      --------
      __init__(length: int or float):
          Initializes a new Square object with the given edge length.

      __str__() -> str:
          Returns a string representation of the Square object.

      get_surface() -> int or float:
          Returns the surface area of the Square.

      get_perimeter() -> int or float:
          Returns the perimeter of the Square.
      """

    def __init__(self, length: int):
        self.edge_length = length

    def __str__(self):
        return f"{self.edge_length} x {self.edge_length}"

    def get_surface(self):
        return self.edge_length * 2

    def get_perimeter(self):
        return self.edge_length * 4

