from Participant import Participant


class Player(Participant):
    """Human player."""
    def __init__(self, coins):
        """Create player with some coins."""
        Participant.__init__(self)
        self.__money = coins

    def place_bet(self):
        """Place a bet taking into account player's coins."""
        while True:
            try:
                bet = int(input("Place a bet, please: "))
                if bet in range(1, self.__money+1):
                    return bet
                elif bet <= 0:
                    print("Bet should be a positive number.\n")
                    continue
                else:
                    print("Looks like you don't have enough money.\n")
                    continue
            except ValueError:
                print("Provide your bet as an integer, please.")
                continue

    def loss_deduction(self, loss):
        """Deduct loss from account."""
        self.__money -= loss

    def get_payoff(self, payoff):
        """Deposit a winnings into account."""
        self.__money += payoff

    def get_balance(self):
        """Return coins quantity player has."""
        return self.__money
