from Participant import Participant


class Player(Participant):

    def __init__(self):
        Participant.__init__(self)
        self.__money = 10

    def place_bet(self):
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
        self.__money -= loss

    def get_payoff(self, payoff):
        self.__money += payoff

    def get_balance(self):
        return self.__money
