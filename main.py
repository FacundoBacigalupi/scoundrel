from game import Game
from console_ui import show_game, ask_action, show_rules


def main():
    show_rules()

    game = Game()
    game.start()

    while not game.game_over:
        show_game(game)

        action = ask_action(game)

        if action == "run":
            game.run_away()
        else:
            index = int(action) - 1
            game.choose_card(index)

        game.check_end_conditions()

    if game.victory:
        print("You won!")
    else:
        print("You lost!")


if __name__ == "__main__":
    main()