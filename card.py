class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def value(self):
        # 2-10 they are worth their number
        # J = 11, Q = 12, K = 13, A = 14
        if self.rank.isdigit():
            return int(self.rank)
        elif self.rank == 'J':
            return 11
        elif self.rank == 'Q':
            return 12
        elif self.rank == 'K':
            return 13
        elif self.rank == 'A':
            return 14
        return 0

    def type(self):
        # monster, potion, weapon
        if self.suit in ['♠', '♣']:
            return 'monster'
        elif self.suit in ['♥']:
            return 'potion'
        else:
            return 'weapon'

    def __str__(self):
        # Example: "A♠", "7♥", "10♦"
        return f"{self.rank}{self.suit}"