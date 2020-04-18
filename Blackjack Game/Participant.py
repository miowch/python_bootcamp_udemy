class Participant:

    def __init__(self):
        self.hand = []

    def hit(self, deck):
        card = deck.give_card()
        self.hand.append(card)

    def stay(self):
        pass

    def calculate_hand(self):
        score = 0
        aces = 0
        for card in self.hand:
            if card.index != 1 and card.index not in range(11, 14):
                score += card.index
            elif card.index in range(11, 14):  # each face card gives 10 points
                score += 10
            elif card.index == 1:
                aces += 1

        # ace gives 1 or 11 points whenever value is preferable to the participant
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
        for card in self.hand:
            print(str(card))
