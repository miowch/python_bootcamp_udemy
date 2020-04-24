import unittest
from Card import Card


class TestCard(unittest.TestCase):
    def testGetValue(self):
        card = Card('♠️', 1)
        self.assertEqual(1, card.get_value())

    def testAceDisplay(self):
        card = Card('♠️', 1)
        self.assertEqual('Ace of ♠️', str(card))

    def testNumberCardDisplay(self):
        card = Card('♥️', 10)
        self.assertEqual('10 of ♥️', str(card))

    def testJackCardDisplay(self):
        card = Card('♦️', 11)
        self.assertEqual('Jack of ♦️', str(card))

    def testQueenCardDisplay(self):
        card = Card('♣️', 12)
        self.assertEqual('Queen of ♣️', str(card))

    def testKingCardDisplay(self):
        card = Card('♥️', 13)
        self.assertEqual('King of ♥️', str(card))

    if __name__ == '__main__':
        unittest.main()
