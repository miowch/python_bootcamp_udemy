class Card:
    """Playing card."""

    __suit = ''
    __index = 0

    def __init__(self, suit, index):
        """Playing card with suit and index."""
        self.__suit = suit
        self.__index = index

    def __str__(self):
        """Show what card it is."""
        if self.__index == 1:
            return f"Ace of {self.__suit}"
        if self.__index in range(2, 11):
            return f"{self.__index} of {self.__suit}"
        if self.__index == 11:
            return f"Jack of {self.__suit}"
        if self.__index == 12:
            return f"Queen of {self.__suit}"
        if self.__index == 13:
            return f"King of {self.__suit}"

    def get_value(self):
        """Show playing card index."""
        return self.__index
