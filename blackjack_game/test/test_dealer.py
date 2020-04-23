import unittest
from unittest.mock import patch
from io import StringIO
from Dealer import Dealer


class TestDealer(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_accept_bet(self, mock_stdout):
        dealer = Dealer()
        dealer.accept_bet(1)
        self.assertEqual("1 is accepted as a bet!\n", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_not_accept_negative_bet(self, mock_stdout):
        dealer = Dealer()
        dealer.accept_bet(-1)
        self.assertEqual("Bet is expected as natural number.\n", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_not_accept_not_integer_bet(self, mock_stdout):
        dealer = Dealer()
        with self.assertRaises(Exception):
            dealer.accept_bet("one")
            self.assertEqual("Bet is expected as an integer.\n", mock_stdout.getvalue())

    def test_give_payoff(self):
        dealer = Dealer()
        dealer._Dealer__bank = 1
        self.assertEqual(1, dealer.give_payoff())

    if __name__ == '__main__':
        unittest.main()
