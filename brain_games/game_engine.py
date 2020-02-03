import brain_games.games
from brain_games.cli import run

def game_run(game_name):
    player_name = run(game_name.RULES)

    score = 0

    while score < 3:

        answer, correct = game_name.run_game()

        if answer != correct:
            print(
                f"'{answer}' is wrong answer ;(.",
                f"Correct answer was '{correct}'.",
            )
            print(f"Let's try again, {player_name}!")
            return
        print("Correct")
        score += 1

    print(f"Congratulations, {player_name}!")


if __name__ == "__main__":
    game_run()
