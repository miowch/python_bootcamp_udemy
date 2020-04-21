from Participant import Participant


class Dealer(Participant):
    __bank = 0

    def accept_bet(self, bet):
        try:
            if bet > 0:
                self.__bank += int(bet)
                print(f"{bet} is accepted as a bet!")
            else:
                print("Bet is expected as natural number.")
        except TypeError or ValueError:
            print("Bet is expected as an integer.")

    def face_up_top_card(self):
        print(f"One of two dealer's cards is {str(self.hand[0])}.")

    def give_payoff(self):
        payoff = self.__bank
        self.__bank = 0
        return payoff

    def remove_bet(self):
        self.__bank = 0
