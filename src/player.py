# Player
#
# At its turn, a Player must play 2 Cards or 1 if the Deck is empty.
# If the Player can't play a Card, the Game is over.
# After playing, the Player fills its hand.
# If all Cards are played, the Game is won.

from renderer import Renderer
from hand import Hand


class Player:
    deck = None
    
    def __init__(self, index: int, hand: Hand) -> None:
        self.index = index
        self.hand = hand

    def playTurn(self) -> None:
        Renderer.renderPlayerHand(self.index, self.hand.count())
        self.hand.fill(self.deck)
        Renderer.renderPlayerHand(self.index, self.hand.count())
