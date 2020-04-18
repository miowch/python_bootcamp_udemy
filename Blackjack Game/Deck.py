from Card import Card
from random import shuffle


class Deck:
    deck = []

    def __init__(self):
        for card_suit in ('spades', 'hearts', 'diamonds', 'clubs'):
            for card_index in range(1, 14):
                card = Card(card_suit, card_index)
                self.deck.append(card)

    def shuffle(self):
        shuffle(self.deck)

    def give_card(self):  # removes and returns the last card in the deck
        return self.deck.pop()

    def __len__(self):
        return len(self.deck)
