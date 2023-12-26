"""Use this module to create commonly accessed patterns"""

from .coordinate import Coordinate
from .matrix import Matrix2D
from .state import ConwayState
import re


class Pattern(Matrix2D):
    def __init__(self, xmax: int, ymax: int, coords: list[Coordinate]):
        super().__init__(xmax, ymax)
        for x in range(xmax + 1):
            for y in range(ymax + 1):
                coord = Coordinate(x, y)
                if coord in coords:
                    self[coord] = ConwayState(True)
                else:
                    self[coord] = ConwayState(False)

    @classmethod
    def from_file(cls, path: str):
        with open(path, "r") as f:
            lines = f.readlines()

        coords = []
        for line in lines[1:]:
            line = line.split(" ")
            coords.append(Coordinate(int(line[0]), int(line[1])))

        xmax = max(c.x for c in coords)
        ymax = max(c.y for c in coords)

        return cls(xmax, ymax, coords)

    @classmethod
    def from_rle(cls, path: str):
        with open(path, "r") as f:
            lines = f.readlines()
        coords = []
        for row, line in enumerate(lines):
            if line.strip().startswith("#"):
                continue
            if "=" in line:
                data = re.search(r"(x = \d+).*(y = \d+)", line).groups()
                x = int(re.search(r"\d+", data[0]).group())
                y = int(re.search(r"\d+", data[1]).group())
            else:
                cells = "".join(line.strip() for line in lines[row:])
                nums = []
                n = 1
                x = 0
                y = 0
                for c in cells:
                    if c == "!":
                        return cls(x, y, coords)
                    elif c == "$":
                        x = 0
                        y += 1
                    elif c.isdigit():
                        nums.append(c)
                    elif c == "o":
                        n = int("".join(nums))
                        for _ in range(n):
                            coords.append(Coordinate(x, y))
                            x += 1

        return cls(x, y, coords)


class Glider(Pattern):
    def __init__(self):
        coords = []
        for x, y in [[0, 2], [1, 0], [2, 1], [1, 2], [2, 2]]:
            coords.append(Coordinate(x, y))
        super().__init__(2, 2, coords)


class Pulsar(Pattern):
    def __init__(self):
        coords = []
        for x, y in [
            [2, 0],
            [3, 0],
            [4, 0],
            [8, 0],
            [9, 0],
            [10, 0],
            [2, 5],
            [3, 5],
            [4, 5],
            [8, 5],
            [9, 5],
            [10, 5],
            [2, 7],
            [3, 7],
            [4, 7],
            [8, 7],
            [9, 7],
            [10, 7],
            [2, 12],
            [3, 12],
            [4, 12],
            [8, 12],
            [9, 12],
            [10, 12],
            [0, 2],
            [0, 3],
            [0, 4],
            [0, 8],
            [0, 9],
            [0, 10],
            [5, 2],
            [5, 3],
            [5, 4],
            [5, 8],
            [5, 9],
            [5, 10],
            [7, 2],
            [7, 3],
            [7, 4],
            [7, 8],
            [7, 9],
            [7, 10],
            [12, 2],
            [12, 3],
            [12, 4],
            [12, 8],
            [12, 9],
            [12, 10],
        ]:
            coords.append(Coordinate(x, y))
        super().__init__(12, 12, coords)


class CloverLeaf(Pattern):
    def __init__(self):
        coords = []
        for x, y in [
            [3, 0],
            [5, 0],
            [1, 1],
            [2, 1],
            [3, 1],
            [5, 1],
            [6, 1],
            [7, 1],
            [0, 2],
            [4, 2],
            [8, 2],
            [0, 3],
            [2, 3],
            [6, 3],
            [8, 3],
            [1, 4],
            [2, 4],
            [4, 4],
            [6, 4],
            [7, 4],
            [1, 6],
            [2, 6],
            [4, 6],
            [6, 6],
            [7, 6],
            [0, 7],
            [2, 7],
            [6, 7],
            [8, 7],
            [0, 8],
            [4, 8],
            [8, 8],
            [1, 9],
            [2, 9],
            [3, 9],
            [5, 9],
            [6, 9],
            [7, 9],
            [3, 10],
            [5, 10],
        ]:
            coords.append(Coordinate(x, y))

        super().__init__(8, 10, coords)


class CloverLeafInterchange(Pattern):
    def __init__(self):
        coords = []
        for x, y in [
            [4, 0],
            [8, 0],
            [3, 1],
            [5, 1],
            [7, 1],
            [9, 1],
            [3, 2],
            [5, 2],
            [7, 2],
            [9, 2],
            [1, 3],
            [2, 3],
            [5, 3],
            [7, 3],
            [10, 3],
            [11, 3],
            [0, 4],
            [5, 4],
            [7, 4],
            [12, 4],
            [1, 5],
            [2, 5],
            [3, 5],
            [4, 5],
            [8, 5],
            [9, 5],
            [10, 5],
            [11, 5],
            [1, 7],
            [2, 7],
            [3, 7],
            [4, 7],
            [8, 7],
            [9, 7],
            [10, 7],
            [11, 7],
            [0, 8],
            [5, 8],
            [7, 8],
            [12, 8],
            [1, 9],
            [2, 9],
            [5, 9],
            [7, 9],
            [10, 9],
            [11, 9],
            [3, 10],
            [5, 10],
            [7, 10],
            [9, 10],
            [3, 11],
            [5, 11],
            [7, 11],
            [9, 11],
            [4, 12],
            [8, 12],
        ]:
            coords.append(Coordinate(x, y))
        super().__init__(12, 12, coords)
