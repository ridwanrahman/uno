class Card:
    def __init__(self, color, card_type, value):
        self.color = color
        self.card_type = card_type
        self.value = value

    def __repr__(self):
        return f"{self.color}{self.value if self.value != -1 else "-"+self.card_type}"
