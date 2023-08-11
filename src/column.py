# Column
#
# A Column has a Direction and a Card stack

import unittest

from card import Card
from direction import Direction


class Column:
    def __init__(self, direction: Direction) -> None:
        self.direction = direction
        self.stack = list()

    def play(self, card: Card) -> None:
        self.stack.append(card)

    def top(self) -> Card:
        return self.stack[-1]


# -------------------------------------------


class ColumnTestCase(unittest.TestCase):
    def testColumn(self):
        Column(Direction.DESCENDING)


if __name__ == "__main__":
    unittest.main()
