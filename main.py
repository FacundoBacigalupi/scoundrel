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

    last_message = None

    while not game.game_over:
        show_game(game)

        if last_message:
            message_type, message_text = last_message

            if message_type == "success":
                show_success(message_text)
            elif message_type == "warning":
                show_warning(message_text)
            elif message_type == "error":
                show_error(message_text)

            last_message = None

        action = ask_action(game)

        if action == "run":
            result = game.run_away()

            if result == "ran_away":
                last_message = ("success", "You ran away. New cards have been loaded into the room.")
            elif result == "cannot_run":
                last_message = ("error", "You can't run away now.")
        else:
            index = int(action) - 1
            card = game.get_card(index)
            if card is None:
                show_error("Invalid card.")
            elif card.type() == "monster":
                old_health = game.player.health

                fight_mode = ask_fight_mode(game, card)
                result = game.choose_card(index, fight_mode)

                new_health = game.player.health
                
                if result == "weapon_not_allowed":
                    last_message = ("error", "You can't use the weapon against this monster.")

                elif result == "fight_mode_required":
                    last_message = ("warning", "Choose weapon or barehanded.")

                else:
                    damage = old_health - new_health

                    if damage > 0:
                        last_message = ("warning", f"You defeated {card} and took {damage} damage. Health: {new_health}/20.")
                    else:
                        last_message = ("success", f"You defeated {card} without taking damage.")
            else:
                old_health = game.player.health
                old_weapon = game.player.weapon

                result = game.choose_card(index)

                new_health = game.player.health

                if result == "potion_used":
                    healed = new_health - old_health

                    if healed > 0:
                        last_message = ("success", f"The potion healed you for {healed}. Health: {new_health}/20.")
                    else:
                        last_message = ("warning", "You used a potion, but your health was already full.")

                elif result == "potion_not_effective":
                    last_message = ("warning", "The potion had no effect because you already used a potion in this room.")

                elif result == "weapon_equipped":
                    if old_weapon:
                        last_message = ("success", f"You replaced {old_weapon} with {card}.")
                    else:
                        last_message = ("success", f"You equipped {card} as your weapon.")

        game.check_end_conditions()

    if game.victory:
        show_success("You won!")
    else:
        show_error("You lost!")


if __name__ == "__main__":
    main()