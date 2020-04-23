import unittest
from unittest.mock import patch
from io import StringIO
from Player import Player


class TestPlayer(unittest.TestCase):

    @patch('builtins.input', return_value='1')
    def test_place_bet(self, mock_input):
        player = Player(2)
        bet = player.place_bet()
        self.assertEqual(1, bet)

    @patch('builtins.input', return_value='2')
    def test_place_all_money_as_bet(self, mock_input):
        player = Player(2)
        bet = player.place_bet()
        self.assertEqual(2, bet)

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_attempt_place_bet_more_than_players_money(self, mock_stdout, mock_input):
        player = Player(2)
        mock_input.side_effect = [3, 2]
        player.place_bet()
        self.assertEqual('Looks like you don\'t have enough money.\n\n', mock_stdout.getvalue())

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_attempt_place_zero_bet(self, mock_stdout, mock_input):
        player = Player(2)
        mock_input.side_effect = [0, 2]
        player.place_bet()
        self.assertEqual('Bet should be a positive number.\n\n', mock_stdout.getvalue())

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_attempt_place_negative_bet(self, mock_stdout, mock_input):
        player = Player(2)
        mock_input.side_effect = [-1, 2]
        player.place_bet()
        self.assertEqual('Bet should be a positive number.\n\n', mock_stdout.getvalue())

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_attempt_place_string_as_bet(self, mock_stdout, mock_input):
        player = Player(2)
        mock_input.side_effect = ['1.9', 2]
        player.place_bet()
        self.assertEqual('Provide your bet as an integer, please.\n\n', mock_stdout.getvalue())

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_attempt_place_empty_string_as_bet(self, mock_stdout, mock_input):
        player = Player(2)
        mock_input.side_effect = ['', 2]
        player.place_bet()
        self.assertEqual('Provide your bet as an integer, please.\n\n', mock_stdout.getvalue())

    def test_get_balance_after_payoff(self):
        player = Player(2)
        player.get_payoff(1)
        self.assertEqual(3, player.get_balance())

    def test_get_balance_after_loss_deduction(self):
        player = Player(2)
        player.loss_deduction(1)
        self.assertEqual(1, player.get_balance())

    @patch('sys.stdout', new_callable=StringIO)
    def test_loss_more_than_players_money(self, mock_stdout):
        player = Player(2)
        with self.assertRaises(Exception):
            player.loss_deduction(3)
            self.assertEqual('Oops! Player\'s loss was calculated incorrectly.\n', mock_stdout.getvalue())

    if __name__ == '__main__':
        unittest.main()
