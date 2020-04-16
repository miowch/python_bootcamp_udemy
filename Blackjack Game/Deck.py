import Card


class Deck:
    deck = []

    def __init__(self):
        for card_suit in ('spades', 'hearts', 'diamonds', 'clubs'):
            for card_index in range(1, 14):
                card = Card.Card(card_suit, card_index)
                self.deck.append(card)

    def pop(self, card_index):
        self.deck.pop(card_index)

    def __len__(self):
        return len(self.deck)
