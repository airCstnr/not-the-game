# Hand
#
# A hand can have maximum 6 Cards

import unittest

from card import Card
from deck import Deck
from state import State


class Hand:
    def __init__(self, maximum_cards_in_hand) -> None:
        self.cards = list()
        self.maximum_cards_in_hand = maximum_cards_in_hand

    def draw(self, card: Card) -> None:
        card.state = State.DRAWN
        self.cards.append(card)

    def count(self) -> int:
        return len(self.cards)

    def fill(self, deck: Deck):
        while self.count() < self.maximum_cards_in_hand and not deck.is_empty():
            card = deck.pick()
            self.draw(card)


# -------------------------------------------


class HandTestCase(unittest.TestCase):
    def testDraw(self):
        hand = Hand()
        card = Card(1)
        hand.draw(card)


if __name__ == "__main__":
    unittest.main()
