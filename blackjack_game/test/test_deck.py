import unittest
from Deck import Deck


class TestDeck(unittest.TestCase):
    def testGiveCard(self):
        deck = Deck()
        card = deck.give_card()
        self.assertIsNotNone(card)

    if __name__ == '__main__':
        unittest.main()
