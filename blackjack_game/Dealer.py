from Participant import Participant


class Dealer(Participant):
    """Computer dealer."""

    __bank = 0

    def accept_bet(self, bet):
        """Put a bet into casino's account."""
        try:
            if bet > 0:
                self.__bank += int(bet)
                print(f"{bet} is accepted as a bet!")
            else:
                print("Bet is expected as natural number.")
        except ValueError:
            print("Bet is expected as an integer.")

    def face_up_top_card(self):
        """Show top card of a hand."""
        print(f"One of two dealer's cards is {self.show_card(0)}.")

    def give_payoff(self):
        """Payoff a bet from casino's account."""
        payoff = self.__bank
        self.__bank = 0
        return payoff

    def remove_bet(self):
        """Zero casino's account."""
        self.__bank = 0
