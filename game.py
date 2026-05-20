from deck import Deck
from player import Player

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.room = []
        self.can_run = True
        self.can_heal = True
        self.game_over = False
        self.victory = False

    def start(self):
        self.can_run = True
        self.can_heal = True
        self.fill_room()

    def fill_room(self):
        # Draw cards until the room has 4 cards or the deck is empty,
        while len(self.room) < 4 and not self.deck.is_empty():
            card = self.deck.draw()
            if card:
                self.room.append(card)

    def get_card(self, index):
        if index < 0 or index >= len(self.room):
            return None

        return self.room[index]

    def choose_card(self, index, fight_mode=None):
        # The player chooses a card from the room
        if index < 0 or index >= len(self.room):
            return "Invalid index"
        card = self.room[index]
        result = "card_used"
        if card.type() == "monster":
            if fight_mode == "weapon":
                success = self.player.fight_with_weapon(card)

                if not success:
                    return "weapon_not_allowed"

            elif fight_mode == "barehanded":
                self.player.fight_barehanded(card)

            else:
                return "fight_mode_required"
        elif card.type() == 'potion':
            if self.can_heal:
                self.player.drink_potion(card)
                self.can_heal = False # You can't heal again in the same room
                result = "potion_used"
            else:
                result = "potion_not_effective"
        elif card.type() == 'weapon':
            self.player.equip_weapon(card)
        # After using the card, it is removed from the room
        self.room.pop(index)
        # The room is filled with new cards if we have one card left
        if len(self.room) == 1:
            self.fill_room()
            self.can_run = True
            self.can_heal = True
        # If a card has already been chosen, you can't escape
        else:
            self.can_run = False
        
        return result

    def run_away(self):
        if self.can_run:
            # Put the cards from the room at the bottom of the deck
            self.deck.put_bottom(self.room)
            self.room = []  # Empty the room
            self.can_run = False  # You can't run away again
            self.fill_room()  # Fill the room with new cards
            return "ran_away"
        
        return "cannot_run"


    def check_end_conditions(self):
        if self.player.is_dead():
            self.game_over = True
            self.victory = False
        elif self.deck.is_empty() and not self.room:
            self.game_over = True
            self.victory = True