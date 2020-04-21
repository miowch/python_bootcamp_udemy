class Participant:

    def __init__(self):
        self.__hand = []

    def hit(self, deck):
        card = deck.give_card()
        self.__hand.append(card)

    def stay(self):
        pass

    def calculate_hand(self):
        score = 0
        aces = 0
        for card in self.__hand:
            value = card.get_value()

            if value != 1 and value not in range(11, 14):
                score += value
            elif value in range(11, 14):  # each face card gives 10 points
                score += 10
            elif value == 1:
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
        for card in self.__hand:
            print(str(card))

    def count_cards_in_hand(self):
        return len(self.__hand)

    def empty_hand(self):
        self.__hand = []

    def show_card(self, index):
        return str(self.__hand[index])
