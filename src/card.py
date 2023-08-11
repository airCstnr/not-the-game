# Card
#
# A Card has a value between 1 and 100

import unittest

from state import State

class Card:
    class OutOfRangeException(Exception):
        pass

    def __init__(self, value) -> None:
        self._setValue(value)
        self.state = State.AVAILABLE

    def _setValue(self, value) -> None:
        if 1 <= value <= 100:
            self.value = value
            return
        raise self.OutOfRangeException


# -------------------------------------------


class CardTestCase(unittest.TestCase):
    def testSetValue(self):
        card = Card(1)
        self.assertEqual(card.value, 1)

    def testOutOfRange(self):
        with self.assertRaises(Card.OutOfRangeException):
            Card(0)


if __name__ == "__main__":
    unittest.main()
