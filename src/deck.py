# Deck
#
# A Deck has 100 Cards shuffeled and can be picked

import unittest
import random

from card import Card


class Deck:
    def __init__(self) -> None:
        self.cards = list(Card(x) for x in range(1, 101))
        random.shuffle(self.cards)

    def pick(self) -> Card:
        return self.cards.pop()

    def count(self) -> int:
        return len(self.cards)


# -------------------------------------------


class DeckTestCase(unittest.TestCase):
    def testPick(self):
        deck = Deck()
        for _ in range(6):
            card = deck.pick()
            self.assertIsInstance(card, Card)
            print(card.value)


if __name__ == "__main__":
    unittest.main()
