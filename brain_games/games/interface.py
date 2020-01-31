from .calc import calc
from .even import even


def game_run(player_name, game_name):
    score = 0

    while score < 3:

        if game_name == "calc":
            res = calc()
        elif game_name == "even":
            res = even()

        if res["output"] == res["correct"]:
            print("Correct")
            score += 1
        else:
            print(
                f"'{res['output']}' is wrong answer ;(.",
                f"Correct answer was '{res['correct']}'.",
            )
            print(f"Let's try again, {player_name}!")
            break
    else:
        print(f"Congratulations, {player_name}!")


if __name__ == "__main__":
    game_run()
