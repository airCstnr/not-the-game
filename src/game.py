# The Game
#
# The Game is composed of 100 Cards shuffled in the Deck.
# Each Player (3 to 5) has one Hand with up to 6 Cards.
# There are 4 Columns: 2 Ascending, 2 Descending.
#
#

import unittest

from tabulate import tabulate

from card import Card
from column import Column
from deck import Deck
from direction import Direction
from hand import Hand

PLAYERS_COUNT = 5
CARDS_COUNT = 10
MAXIMUM_CARDS_IN_HAND = 6


class Game:
    def __init__(self) -> None:
        self.cards = self.generateCards()
        self.deck = Deck(self.cards)
        self.players = [Hand(MAXIMUM_CARDS_IN_HAND) for _ in range(PLAYERS_COUNT)]
        self.columns = [
            Column(Direction.ASCENDING),
            Column(Direction.ASCENDING),
            Column(Direction.DESCENDING),
            Column(Direction.DESCENDING),
        ]

    def generateCards(self) -> list:
        return list(Card(x) for x in range(1, CARDS_COUNT + 1))

    def renderAllCards(self) -> None:
        values = [[card.value, card.state.value] for card in self.cards]
        print(tabulate(values, headers=["Card", "State"]))
        # "Available", "Drawn", "Played"
        print()

    def renderBanner(self) -> None:
        print("------------------------")
        print("Welcome to NOT The Game!")
        print("------------------------")
        print()

    def start(self):
        self.renderBanner()

        print(f"Players : {PLAYERS_COUNT}")
        print()

        self.renderAllCards()

        current_player_index = 0
        current_player = self.players[current_player_index]

        print(
            f"Player {current_player_index + 1 } has "
            f"{current_player.count()} cards."
        )

        current_player.fill(self.deck)

        print(
            f"Player {current_player_index + 1 } has "
            f"{current_player.count()} cards."
        )

        print()

        self.renderAllCards()

        print("------------------------")


# -------------------------------------------


class GameTestCase(unittest.TestCase):
    def testGame(self):
        game = Game()
        self.assertEqual(game.deck.count(), CARDS_COUNT)


if __name__ == "__main__":
    unittest.main()
