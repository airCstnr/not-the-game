# The Game
#
# The Game is composed of 100 Cards shuffled in the Deck.
# Each Player (3 to 5) has one Hand with up to 6 Cards.
# There are 4 Columns: 2 Ascending, 2 Descending.


import unittest

from card import Card
from column import Column
from deck import Deck
from direction import Direction
from hand import Hand
from renderer import Renderer
from player import Player

PLAYERS_COUNT = 5
CARDS_COUNT = 10
MAXIMUM_CARDS_IN_HAND = 6


class Game:
    def __init__(self) -> None:
        self.cards = self.generateCards()
        self.deck = Deck(self.cards)
        Player.deck = self.deck
        self.players = list()
        for index in range(PLAYERS_COUNT):
            hand = Hand(MAXIMUM_CARDS_IN_HAND)
            hand.fill(self.deck)
            self.players.append(Player(index + 1, hand))
        self.columns = [
            Column(Direction.ASCENDING),
            Column(Direction.ASCENDING),
            Column(Direction.DESCENDING),
            Column(Direction.DESCENDING),
        ]

    def generateCards(self) -> list:
        return list(Card(x) for x in range(1, CARDS_COUNT + 1))

    def start(self):
        Renderer.renderBanner()

        print(f"Players : {PLAYERS_COUNT}")
        print()

        for current_player in self.players:
            current_player.playTurn()
            print()

        print("------------------------")


# -------------------------------------------


class GameTestCase(unittest.TestCase):
    def testGame(self):
        game = Game()
        self.assertEqual(game.deck.count(), 0)


if __name__ == "__main__":
    unittest.main()
