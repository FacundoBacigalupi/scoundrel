from card import Card
import random

class Deck:
    def __init__(self):
        self.cards = self.create_scoundrel_deck()
        self.shuffle()

    def create_scoundrel_deck(self):
        # ♠: 2-A
        # ♣: 2-A
        # ♥: 2-10
        # ♦: 2-10
        suits = ['♠', '♣', '♥', '♦']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        deck = []
        for suit in suits:
            for rank in ranks:
                if suit in ['♥', '♦'] and rank in ['J', 'Q', 'K', 'A']:
                    continue  # There are no J, Q, K, or A's in hearts and diamonds.
                deck.append(Card(suit, rank))
        return deck

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if self.cards:
            return self.cards.pop(0)  # Take the card from the top
        return None  # There are no cards to draw.

    def put_bottom(self, cards: list[Card]):
        random.shuffle(cards)  # Shuffle the cards before placing them at the bottom
        self.cards.extend(cards)  # Add the cards to the bottom of the deck

    def is_empty(self):
        return len(self.cards) == 0