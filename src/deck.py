# Deck
#
# A Deck has 100 Cards shuffeled and can be picked

import unittest

from card import Card


class Deck:
    def __init__(self) -> None:
        self.cards = list(Card(x) for x in range(1, 101))

    def pick(self) -> Card:
        return self.cards.pop()


# -------------------------------------------


class DeckTestCase(unittest.TestCase):
    def testPick(self):
        deck = Deck()
        self.assertIsInstance(deck.pick(), Card)


if __name__ == "__main__":
    unittest.main()
