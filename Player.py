import random

class Player:
    def __init__(self, name, point=0):
        self._name = name
        self._points = point
        self._cards  = []

    @property
    def name(self):
        return self._name

    def give_card_to_player(self, card):
        self._cards.append(card)

    def has_number_of_cards(self):
        return len(self._cards)

    def present_first_card(self):
        """
        This func will select a random card from the player's card list
        """
        index = random.randint(0, len(self._cards) - 1)
        return self._cards.pop(index)

    def present_card(self):
        return self._cards.pop()

    def __repr__(self):
        return f"{self._name}"
