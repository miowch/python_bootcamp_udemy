import unittest
from Participant import Participant
from Card import Card


class TestParticipant(unittest.TestCase):
    def setUp(self):
        self.ace_card = Card('♦️', 1)
        self.number_card = Card('♥️', 10)
        self.jack_card = Card('♠️', 11)
        self.queen_card = Card('♣️', 12)
        self.king_card = Card('♠️', 13)

    # TODO: Find out how to use mocking instead of accessing private variables.
    def test_calculate_number_card_in_hand(self):
        hand = Participant()
        hand._Participant__hand.append(self.number_card)
        self.assertEqual(self.number_card.get_value(), hand.calculate_hand())

    def test_calculate_face_card_jack_in_hand(self):
        hand = Participant()
        hand._Participant__hand.append(self.jack_card)
        self.assertEqual(10, hand.calculate_hand())

    def test_calculate_face_card_queen_in_hand(self):
        hand = Participant()
        hand._Participant__hand.append(self.queen_card)
        self.assertEqual(10, hand.calculate_hand())

    def test_calculate_face_card_king_in_hand(self):
        hand = Participant()
        hand._Participant__hand.append(self.king_card)
        self.assertEqual(10, hand.calculate_hand())

    def test_calculate_ace_card_in_hand(self):
        hand = Participant()
        hand._Participant__hand.append(self.ace_card)
        self.assertEqual(11, hand.calculate_hand())

    def test_calculate_four_aces_in_hand(self):
        hand = Participant()
        for i in range(1, 5):
            hand._Participant__hand.append(self.ace_card)
        self.assertEqual(14, hand.calculate_hand())

    def test_calculate_hand_with_different_cards(self):
        hand = Participant()
        hand._Participant__hand.append(self.ace_card)
        hand._Participant__hand.append(self.number_card)
        hand._Participant__hand.append(self.queen_card)
        self.assertEqual(21, hand.calculate_hand())

    def test_calculate_empty_hand(self):
        hand = Participant()
        self.assertEqual(0, hand.calculate_hand())

    if __name__ == '__main__':
        unittest.main()
