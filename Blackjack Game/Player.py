from Participant import Participant


class Player(Participant):

    def __init__(self):
        Participant.__init__(self)
        self.money = 10

    def place_bet(self):
        while True:
            try:
                bet = int(input("Place a bet, please: "))
                if bet <= self.money:
                    return bet
                else:
                    print("Looks like you don't have enough money.\nPlace another bet, please.")
                    continue
            except TypeError or ValueError:
                print("Provide your bet as an integer, please.")
                continue
