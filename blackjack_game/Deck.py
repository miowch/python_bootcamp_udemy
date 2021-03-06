from random import shuffle
from Card import Card


class Deck:
    """Standard 52-card deck."""

    __deck = []

    def __init__(self):
        """Create shuffled deck."""
        self.assemble()

    def assemble(self):
        self.__deck.clear()
        for card_suit in ('♠️', '♥️', '♦️', '♣️'):
            for card_index in range(1, 14):
                card = Card(card_suit, card_index)
                self.__deck.append(card)
        shuffle(self.__deck)

    def give_card(self):
        """Return top card from the deck."""
        return self.__deck.pop(0)

    def __len__(self):
        """Return cards quantity in the deck."""
        return len(self.__deck)
