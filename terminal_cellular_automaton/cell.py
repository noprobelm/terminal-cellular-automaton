from typing import Protocol, Tuple

from .coordinate import Coordinate


class Cell(Protocol):
    """A protocol to reference when creating a new type of cell

    A cell is primarily defined by its neighbors. A class that conforms to this protocol shoud have an __init__ method
    which accepts a coordinate, and a get_neighbors method that will retreive valid neighbors based on a maximum
    possible coordinate

    Attributes:
        coord (Coordinate): The coordinate of a given cell
        neighbors (Tuple[Coordinate, ...]): All valid neighbors of a cell based on the coordinate attribute
    """

    coord: Coordinate
    neighbors: Tuple[Coordinate, ...]

    def __init__(self, coord: Coordinate) -> None:
        """Initializes an instance of a cell. The coord attr should be set here"""
        ...

    def get_neighbors(self, max_coord: Coordinate) -> list[Coordinate]:
        """Accesses members of a cell's neighborhood and returns a list of valid neighbors

        This is usually achieved by checking coordinates against a maximum possible coordinate. The
        Coordinate.__contains__ special method is available for determining neighbors.

        Args:
            max_coord (Coordinate): The maximum possible coordinate of a neighbor (usually the max coord of the
                underlying matrix)

        Returns:
            A list of all valid neighbors
        """
        ...


class MooreCell:
    """A cell that references members of a MooreNeighborhood

    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
    | 4 | C | 5 |
    +---+---+---+
    | 6 | 7 | 8 |
    +---+---+---+

    """

    neighbors: Tuple[Coordinate, ...] = (
        # Upper left
        Coordinate(-1, -1),
        # Upper
        Coordinate(0, -1),
        # Upper right
        Coordinate(1, -1),
        # Right
        Coordinate(1, 0),
        # Lower right
        Coordinate(1, 1),
        # Lower
        Coordinate(0, 1),
        # Lower left
        Coordinate(-1, 1),
        # Left
        Coordinate(-1, 0),
    )

    def __init__(self, coord: Coordinate) -> None:
        """Initializes an instance of the MooreCell class"""
        self.coord = coord

    def get_neighbors(self, max_coord: Coordinate) -> list[Coordinate]:
        """Gets neighbors based on the max coord

        Args:
            max_coord (Coordinate): The maximum possible coordinate of a neighbor (usually the max coord of the
                underlying matrix)

        Returns:
            A list of all valid neighbors

        """
        neighbors = []
        for nc in self.neighbors:
            n = nc + self.coord
            if n in max_coord:
                neighbors.append(n)

        return neighbors
