def show_game(game):
    print("Remaining cards in deck:", len(game.deck.cards))
    print("Health:", game.player.health)

    if game.player.weapon:
        print("Weapon:", game.player.weapon)
        print("Last monster killed with weapon:", game.player.last_monster_killed_with_weapon or "none")
    else:
        print("Weapon: none")

    print("Room:")
    for i, card in enumerate(game.room):
        print(f"{i + 1}. {card}")


def ask_action(game):
    print()
    print("Choose a card by number.")
    print("You can also write 'run' to run away if allowed.")

    while action := input("> "):
        if action == "run":
            return action
        elif action.isdigit() and 1 <= int(action) <= len(game.room):
            return action
        else:
            print("Invalid action. Please choose a valid card number or write 'run' to run away.")

def show_rules():
    print("=" * 60)
    print("SCOUNDREL - RULES")
    print("=" * 60)
    print()
    print("Goal:")
    print("  Survive the dungeon and go through the entire deck.")
    print()
    print("Card types:")
    print("  Spades   (♠) = Monsters")
    print("  Clubs    (♣) = Monsters")
    print("  Hearts   (♥) = Potions")
    print("  Diamonds (♦) = Weapons")
    print()
    print("Basic rules:")
    print("  - You start with 20 health.")
    print("  - Each room has up to 4 cards.")
    print("  - You choose one card at a time from the room.")
    print("  - When the room has 1 card left, new cards are drawn until it has 4 again.")
    print()
    print("Monsters:")
    print("  - If you fight barehanded, you lose health equal to the monster value.")
    print("  - If you fight with a weapon, damage is reduced by the weapon value.")
    print("  - Damage cannot go below 0.")
    print()
    print("Weapons:")
    print("  - A diamond card becomes your equipped weapon.")
    print("  - Equipping a new weapon replaces the old one.")
    print("  - After killing a monster with a weapon, that weapon can only be used")
    print("    against monsters with a lower value than the last monster killed with it.")
    print()
    print("Potions:")
    print("  - A heart card heals you by its value.")
    print("  - Health cannot go above 20.")
    print("  - Usually, only one potion can heal you per room.")
    print()
    print("Running away:")
    print("  - You may run away from a room if allowed.")
    print("  - Running away puts the current room at the bottom of the deck.")
    print("  - You cannot run away twice in a row.")
    print()
    print("Game over:")
    print("  - You win if you survive the entire dungeon.")
    print("  - You lose if your health reaches 0 or less.")
    print()
    print("=" * 60)
    print()