import random
from Card import Card

COLORS = ["red", "blue", "green", "yellow"]
NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
NUMBERS_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
OTHER_CARDS = ["skip", "reverse", "draw"]
# 4 blank cards
# 4 wild cards

class UnoDeck:
    _deck = []

    def __init__(self):
        self._initialize_deck()

    def get_top_14_cards(self):
        top_14_cards = self._deck[:14]
        self._deck = self._deck[14:]
        return top_14_cards

    def _initialize_deck(self):
        # red cards
        number_cards = [Card("red", "number", num) for num in NUMBERS]
        number_cards_2 = [Card("red", "number", num) for num in NUMBERS_2]
        skip_cards = [Card("red", "skip", -1) for _ in range(2)]
        reverse_cards = [Card("red", "reverse", -1) for _ in range(2)]
        draw_cards = [Card("red", "draw", -1) for _ in range(2)]
        self._deck.extend(number_cards)
        self._deck.extend(number_cards_2)
        self._deck.extend(skip_cards)
        self._deck.extend(reverse_cards)
        self._deck.extend(draw_cards)

        # green cards
        number_cards = [Card("green", "number", num) for num in NUMBERS]
        number_cards_2 = [Card("green", "number", num) for num in NUMBERS_2]
        skip_cards = [Card("green", "skip", -1) for _ in range(2)]
        reverse_cards = [Card("green", "reverse", -1) for _ in range(2)]
        draw_cards = [Card("green", "draw", -1) for _ in range(2)]
        self._deck.extend(number_cards)
        self._deck.extend(number_cards_2)
        self._deck.extend(skip_cards)
        self._deck.extend(reverse_cards)
        self._deck.extend(draw_cards)

        # blue cards
        number_cards = [Card("blue", "number", num) for num in NUMBERS]
        number_cards_2 = [Card("blue", "number", num) for num in NUMBERS_2]
        skip_cards = [Card("blue", "skip", -1) for _ in range(2)]
        reverse_cards = [Card("blue", "reverse", -1) for _ in range(2)]
        draw_cards = [Card("blue", "draw", -1) for _ in range(2)]
        self._deck.extend(number_cards)
        self._deck.extend(number_cards_2)
        self._deck.extend(skip_cards)
        self._deck.extend(reverse_cards)
        self._deck.extend(draw_cards)

        # yellow cards
        number_cards = [Card("yellow", "number", num) for num in NUMBERS]
        number_cards_2 = [Card("yellow", "number", num) for num in NUMBERS_2]
        skip_cards = [Card("yellow", "skip", -1) for _ in range(2)]
        reverse_cards = [Card("yellow", "reverse", -1) for _ in range(2)]
        draw_cards = [Card("yellow", "draw", -1) for _ in range(2)]
        self._deck.extend(number_cards)
        self._deck.extend(number_cards_2)
        self._deck.extend(skip_cards)
        self._deck.extend(reverse_cards)
        self._deck.extend(draw_cards)

        blank_card = [Card("blank", "blank", -1) for _ in range(4)]
        wild_card = [Card("wild", "wild", -1) for _ in range(4)]
        self._deck.extend(blank_card)
        self._deck.extend(wild_card)


    def get_shuffled_deck(self):
        random.shuffle(self._deck)
        return self._deck

    def play_card(self, card1, card2):
        pass

