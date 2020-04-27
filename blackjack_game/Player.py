from Participant import Participant


class Player(Participant):
    """Human player."""

    def __init__(self, coins):
        """Create player with some coins."""
        Participant.__init__(self)
        self.__money = coins
        self.__bet = 0

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
                self.__bet = bet
                return self.__bet

    def loss_deduction(self):
        """Deduct loss from account."""
        self.__money -= self.__bet
        self.__bet = 0

    def get_payoff(self):
        """Deposit a winnings into account."""
        self.__money += self.__bet
        self.__bet = 0

    def get_balance(self):
        """Return coins quantity player has."""
        return self.__money

    def get_bet(self):
        """Return bet."""
        return self.__bet
