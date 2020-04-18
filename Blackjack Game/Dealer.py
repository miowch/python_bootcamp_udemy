from Participant import Participant


class Dealer(Participant):
    bank = 0

    def accept_bet(self, bet):
        try:
            if bet > 0:
                self.bank += int(bet)
                print(f"{bet} is accepted as a bet!")
            else:
                print("Bet is expected as natural number.")
        except TypeError or ValueError:
            print("Bet is expected as an integer.")

    def face_up_top_card(self):
        print(str(self.hand[0]))
