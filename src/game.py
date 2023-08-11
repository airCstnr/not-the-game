# The Game
#
# The Game is composed of 100 Cards shuffled in the Deck.
# Each Player (3 to 5) has one Hand with up to 6 Cards.
# There are 4 Columns: 2 Ascending, 2 Descending.
#
#

import random
import unittest

from card import Card
from column import Column
from deck import Deck
from direction import Direction
from hand import Hand

PLAYERS_COUNT = 5


class Game:
    def __init__(self) -> None:
        self.cards = self.generateCards()
        self.deck = Deck(self.cards)
        self.players = [Hand() for _ in range(PLAYERS_COUNT)]
        self.columns = [
            Column(Direction.ASCENDING),
            Column(Direction.ASCENDING),
            Column(Direction.DESCENDING),
            Column(Direction.DESCENDING),
        ]

    def generateCards(self) -> list:
        cards = list(Card(x) for x in range(1, 101))
        random.shuffle(cards)
        return cards

    def renderAllCards(self):
        pass

    def start(self):
        print("------------------------")
        print("Welcome to NOT The Game!")
        print("------------------------")
        print()

        print(f"Players : {PLAYERS_COUNT}")

        print()

        self.renderAllCards()

        print()


# -------------------------------------------


class GameTestCase(unittest.TestCase):
    def testGame(self):
        game = Game()
        self.assertEqual(game.deck.count(), 100)


if __name__ == "__main__":
    unittest.main()
