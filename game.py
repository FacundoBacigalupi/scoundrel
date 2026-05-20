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

    def choose_card(self, index):
        # The player chooses a card from the room
        if index < 0 or index >= len(self.room):
            return "Invalid index"
        card = self.room[index]
        if card.type() == 'monster':
            # The player chooses whether to fight bare-handed or with a weapon if they have one
            print(f"Choose how to fight the monster {card}.")
            print("Write 'weapon' to use your weapon or 'barehanded' to fight bare-handed.")
            finish = False
            while not finish:
                action = input("> ")
                if action == "weapon" and self.player.weapon:
                    self.player.fight_with_weapon(card)
                    finish = True
                elif action == "barehanded":
                    self.player.fight_barehanded(card)
                    finish = True
                elif action == "weapon" and not self.player.weapon:
                    print("You don't have a weapon equipped.")
                else:
                    print("Invalid action. Please write 'weapon' or 'barehanded'.")
        elif card.type() == 'potion' and self.can_heal:
            self.player.drink_potion(card)
            self.can_heal = False  # You can't heal again in the same room
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

    def run_away(self):
        if self.can_run:
            # Put the cards from the room at the bottom of the deck
            self.deck.put_bottom(self.room)
            self.room = []  # Empty the room
            self.can_run = False  # You can't run away again
            self.fill_room()  # Fill the room with new cards
            print("You ran away. New cards have been loaded into the room.")
        else:
            print("You can't run away now.")


    def check_end_conditions(self):
        if self.player.is_dead():
            self.game_over = True
            self.victory = False
        elif self.deck.is_empty() and not self.room:
            self.game_over = True
            self.victory = True