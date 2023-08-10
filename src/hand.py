# Hand
#
# A hand can have maximum 6 Cards
import unittest

from card import Card


class Hand:
    cards = list()

    def draw(self, card: Card) -> None:
        self.cards.append(card)


# -------------------------------------------


class HandTestCase(unittest.TestCase):
    def testDraw(self):
        hand = Hand()
        card = Card(1)
        hand.draw(card)


if __name__ == "__main__":
    unittest.main()
