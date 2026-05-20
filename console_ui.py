import os

# Enables ANSI colors in many Windows terminals
os.system("")

RESET = "\033[0m"
BOLD = "\033[1m"

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
GRAY = "\033[90m"

def color(text, ansi_color):
    return f"{ansi_color}{text}{RESET}"

def format_card(card):
    if card.type() == "monster":
        return color(str(card), RED)
    elif card.type() == "potion":
        return color(str(card), GREEN)
    elif card.type() == "weapon":
        return color(str(card), CYAN)

    return str(card)

def print_separator():
    print(color("=" * 60, GRAY))

def show_game(game):
    print()
    print_separator()
    print(color("SCOUNDREL", BOLD + MAGENTA))
    print_separator()

    print(f"{color('Remaining cards:', YELLOW)} {len(game.deck.cards)}")
    print(f"{color('Health:', GREEN)} {game.player.health}/20")

    if game.player.weapon:
        print(f"{color('Weapon:', CYAN)} {format_card(game.player.weapon)}")
        print(
            f"{color('Last monster killed with weapon:', RED)} "
            f"{game.player.last_monster_killed_with_weapon or 'none'}"
        )
    else:
        print(f"{color('Weapon:', CYAN)} none")

    print()
    print(color("Room:", BOLD + WHITE))

    for i, card in enumerate(game.room):
        print(f"  {color(str(i + 1) + '.', YELLOW)} {format_card(card)}")

    print_separator()

def ask_action(game):
    print()
    print(color("Choose a card by number.", WHITE))

    if game.can_run:
        print(f"You can also write {color('run', YELLOW)} to run away.")
    else:
        print(color("You cannot run away right now.", GRAY))

    while action := input(color("> ", BOLD + YELLOW)):
        if action == "run":
            return action
        elif action.isdigit() and 1 <= int(action) <= len(game.room):
            return action
        else:
            show_error("Invalid action. Please choose a valid card number or write 'run' to run away.")

def ask_fight_mode(game, monster):
    print()
    show_warning(f"You encountered monster {format_card(monster)}.")
    print("Choose how to fight:")

    if game.player.weapon:
        print(f"  1. Use weapon {format_card(game.player.weapon)}")
    else:
        print(color("  1. Use weapon unavailable: no weapon equipped", GRAY))

    print("  2. Fight barehanded")

    while True:
        action = input(color("> ", BOLD + YELLOW))

        if action == "1" or action == "weapon":
            if game.player.weapon:
                return "weapon"

            show_error("You don't have a weapon equipped.")

        elif action == "2" or action == "barehanded":
            return "barehanded"

        else:
            show_error("Invalid action. Write 'weapon' or 'barehanded'.")

def show_error(message):
    print(color(message, RED))

def show_success(message):
    print(color(message, GREEN))

def show_warning(message):
    print(color(message, YELLOW))

def show_rules():
    print_separator()
    print(color("SCOUNDREL - RULES", BOLD + MAGENTA))
    print_separator()
    print()
    print("Goal:")
    print("  Survive the dungeon and go through the entire deck.")
    print()
    print(color("Card types:", BOLD + WHITE))
    print(f"  {color('Spades   (♠)', RED)} = Monsters")
    print(f"  {color('Clubs    (♣)', RED)} = Monsters")
    print(f"  {color('Hearts   (♥)', GREEN)} = Potions")
    print(f"  {color('Diamonds (♦)', CYAN)} = Weapons")
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
    print_separator()
    input(color("Press Enter to start the game...", BOLD + YELLOW))
    print()