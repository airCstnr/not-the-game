# Deck
#
# A Deck has Cards that can be picked

import unittest

import random

from card import Card


class Deck:
    def __init__(self, cards: list) -> None:
        self.cards = cards.copy()
        random.shuffle(self.cards)

    def pick(self) -> Card:
        return self.cards.pop()

    def count(self) -> int:
        return len(self.cards)


# -------------------------------------------


class DeckTestCase(unittest.TestCase):
    deck = Deck([Card(3)])

    def testCount(self):
        self.assertEqual(self.deck.count(), 1)

    def testPick(self):
        card = self.deck.pick()
        self.assertIsInstance(card, Card)
        self.assertEqual(card.value, 3)

    def testCountAfter(self):
        self.assertEqual(self.deck.count(), 1)


if __name__ == "__main__":
    unittest.main()
