# The Game
#
# The Game is composed of 100 Cards shuffled in the Deck.
# Each Player (3 to 5) has one Hand with up to 6 Cards.
# There are 4 Columns: 2 Ascending, 2 Descending.
#
#

import unittest

from column import Column
from deck import Deck
from direction import Direction
from hand import Hand

PLAYERS_COUNT = 5


class Game:
    def __init__(self) -> None:
        self.deck = Deck()
        self.players = [Hand() for _ in range(PLAYERS_COUNT)]
        self.columns = [
            Column(Direction.ASCENDING),
            Column(Direction.ASCENDING),
            Column(Direction.DESCENDING),
            Column(Direction.DESCENDING),
        ]

    def start(self):
        print("------------------------")
        print("Welcome to NOT The Game!")
        print("------------------------")
        print()

        print(f"Players : {PLAYERS_COUNT}")

        print()


# -------------------------------------------


class GameTestCase(unittest.TestCase):
    def testGame(self):
        game = Game()
        self.assertEqual(game.deck.count(), 100)


if __name__ == "__main__":
    unittest.main()
