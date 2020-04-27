import unittest
from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout
from Card import Card
from Dealer import Dealer
from Deck import Deck
from Player import Player
import blackjack


class TestBlackjack(unittest.TestCase):

    @patch('builtins.input')
    @patch('Deck.Deck.give_card')
    def test_hit_hit_moves(self, mock_give_card, mock_input):
        player = Player(2)
        deck = Deck()
        queen = Card('♥️', 12)
        ace = Card('♠️', 1)

        mock_give_card.side_effect = [queen, ace]
        mock_input.side_effect = ['hit', 'hit']

        trap = StringIO()  # Do not print out
        with redirect_stdout(trap):
            blackjack.player_makes_moves(deck, player)

        self.assertEqual(21, player.calculate_hand())

    @patch('builtins.input')
    @patch('Deck.Deck.give_card')
    def test_hit_stay_moves(self, mock_give_card, mock_input):
        player = Player(2)
        deck = Deck()
        card = Card('♥️', 9)
        mock_give_card.return_value = card
        mock_input.side_effect = ['hit', 'stay']

        trap = StringIO()
        with redirect_stdout(trap):
            blackjack.player_makes_moves(deck, player)

        self.assertEqual(9, player.calculate_hand())

    @patch('builtins.input')
    def test_stay_move(self, mock_input):
        player = Player(2)
        deck = Deck()
        mock_input.return_value = 'stay'

        trap = StringIO()
        with redirect_stdout(trap):
            blackjack.player_makes_moves(deck, player)

        self.assertEqual(0, player.calculate_hand())

    @patch('builtins.input')
    @patch('Deck.Deck.give_card')
    def test_unsupported_move(self, mock_give_card, mock_input):
        player = Player(2)
        deck = Deck()
        card = Card('♥️', 9)
        mock_give_card.return_value = card
        mock_input.side_effect = ['take', 'hit', 'stay']

        trap = StringIO()
        with redirect_stdout(trap):
            blackjack.player_makes_moves(deck, player)

        self.assertEqual(9, player.calculate_hand())

    @patch('builtins.input')
    @patch('Deck.Deck.give_card')
    def test_empty_input_as_move(self, mock_give_card, mock_input):
        player = Player(2)
        deck = Deck()
        card = Card('♥️', 9)
        mock_give_card.return_value = card
        mock_input.side_effect = [None, 'hit', 'stay']

        trap = StringIO()
        with redirect_stdout(trap):
            blackjack.player_makes_moves(deck, player)

        self.assertEqual(9, player.calculate_hand())

    @patch('builtins.input')
    def test_play_again(self, mock_input):
        deck = Deck()
        dealer = Dealer()
        player = Player(2)

        mock_input.return_value = 'yes'
        self.assertTrue(blackjack.play_again(deck, dealer, player))

    @patch('builtins.input')
    def test_not_play_again(self, mock_input):
        deck = Deck()
        dealer = Dealer()
        player = Player(2)

        mock_input.return_value = 'meh'
        trap = StringIO()
        with redirect_stdout(trap):
            self.assertFalse(blackjack.play_again(deck, dealer, player))

    if __name__ == '__main__':
        unittest.main()
