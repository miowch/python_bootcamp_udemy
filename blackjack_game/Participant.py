class Participant:
    """Participant of card game."""

    def __init__(self):
        """Participant without cards in their hand."""
        self.__hand = []

    def hit(self, deck):
        """Take top card from the deck."""
        card = deck.give_card()
        self.__hand.append(card)

    def calculate_hand(self):
        """
        Return participant's hand value.

        Each face card gives 10 points.
        Ace gives 1 or 11 points whenever value is preferable to the participant.
        """
        score = 0
        aces = 0
        for card in self.__hand:
            value = card.get_value()

            if value != 1 and value not in range(11, 14):
                score += value
            elif value in range(11, 14):
                score += 10
            elif value == 1:
                aces += 1

        if aces > 1:
            score += (aces - 1)
            aces = 1

        if aces == 1:
            if score in range(0, 11):
                score += 11
            else:
                score += 1

        return score

    def face_up_hand(self):
        """Show all cards in the hand."""
        for card in self.__hand:
            print(str(card))

    def count_cards_in_hand(self):
        """Return how many cards are in the hand."""
        return len(self.__hand)

    def empty_hand(self):
        """Remove all cards from the hand."""
        self.__hand = []

    def show_card(self, index):
        """Show particular card in the hand."""
        return str(self.__hand[index])
