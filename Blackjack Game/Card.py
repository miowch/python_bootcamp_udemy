class Card:

    def __init__(self, suit, index):
        self.suit = suit
        self.index = index

    def __str__(self):
        if self.index == 1:
            return f"Ace of {self.suit}"
        elif self.index in range(2,11):
            return f"{self.index} of {self.suit}"
        elif self.index == 11:
            return f"Jack of {self.suit}"
        elif self.index == 12:
            return f"Queen of {self.suit}"
        elif self.index == 13:
            return f"King of {self.suit}"
