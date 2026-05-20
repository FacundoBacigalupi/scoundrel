from game import Game
from console_ui import (
    show_game,
    ask_action,
    ask_fight_mode,
    show_rules,
    show_success,
    show_warning,
    show_error,
)


def main():
    show_rules()

    game = Game()
    game.start()

    while not game.game_over:
        show_game(game)

        action = ask_action(game)

        if action == "run":
            result = game.run_away()

            if result == "ran_away":
                show_success("You ran away. New cards have been loaded into the room.")
            elif result == "cannot_run":
                show_error("You can't run away now.")
        else:
            index = int(action) - 1
            card = game.get_card(index)
            if card is None:
                show_error("Invalid card.")
            elif card.type() == "monster":
                fight_mode = ask_fight_mode(game, card)
                result = game.choose_card(index, fight_mode)
                if result == "weapon_not_allowed":
                    show_error("You can't use the weapon against this monster.")
                elif result == "fight_mode_required":
                    show_warning("Choose weapon or barehanded.")
            else:
                old_health = game.player.health
                result = game.choose_card(index)
                new_health = game.player.health

                if result == "potion_used":
                    healed = new_health - old_health

                    if healed > 0:
                        show_success(f"The potion healed you for {healed}. Health: {new_health}/20.")
                    else:
                        show_warning("You used a potion, but your health was already full.")

                elif result == "potion_not_effective":
                    show_warning("The potion had no effect because you already used a potion in this room.")

                elif result == "weapon_equipped":
                    show_success(f"You equipped {card}.")

        game.check_end_conditions()

    if game.victory:
        show_success("You won!")
    else:
        show_error("You lost!")


if __name__ == "__main__":
    main()