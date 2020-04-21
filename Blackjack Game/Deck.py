from Card import Card
from random import shuffle


class Deck:
    __deck = []

    def __init__(self):
        for card_suit in ('spades', 'hearts', 'diamonds', 'clubs'):
            for card_index in range(1, 14):
                card = Card(card_suit, card_index)
                self.__deck.append(card)

        shuffle(self.__deck)

    def shuffle(self):
        shuffle(self.__deck)

    def give_card(self):  # removes and returns the last card in the deck
        return self.__deck.pop()

    def assemble(self):
        self.__deck.clear()
        self.__init__()

    def __len__(self):
        return len(self.__deck)
