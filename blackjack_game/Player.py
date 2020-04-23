from Participant import Participant


class Player(Participant):
    """Human player."""

    def __init__(self, coins):
        """Create player with some coins."""
        Participant.__init__(self)
        self.__money = coins

    def __input_bet(self):
        """Validate input as int"""
        while True:
            try:
                bet = int(input("Place a bet, please: "))
                return bet
            except:
                print("Provide your bet as an integer, please.\n")
                continue

    def __validate_bet(self, bet):
        """Validate bet taking into account player's coins."""
        if bet <= 0:
            print("Bet should be a positive number.\n")
            return False
        if bet not in range(1, self.__money+1):
            print("Looks like you don't have enough money.\n")
            return False
        return True

    def place_bet(self):
        """Place a bet"""
        while True:
            bet = self.__input_bet()
            if self.__validate_bet(bet):
                return bet

    def loss_deduction(self, loss):
        """Deduct loss from account."""
        if loss <= self.__money:
            self.__money -= loss
        else:
            print('Oops! Player\'s loss was calculated incorrectly.')
            raise Exception

    def get_payoff(self, payoff):
        """Deposit a winnings into account."""
        self.__money += payoff

    def get_balance(self):
        """Return coins quantity player has."""
        return self.__money
