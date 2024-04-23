#!/usr/bin/env python3
"""
Módulo que simula o jogo de Senha diversas vezes e mede a taxa de acerto da estratégia do jogador.
"""

from random import sample
from time import time
from sys import argv


def run_game(max_guesses=10, n_games=10000):
    """
    Função que roda o jogo de Senha diversas vezes e mede a taxa de acerto da estratégia do jogador.
    """
    from codes import guess_code, COLORS, CODE_LENGTH, HIST, RES

    wins = 0
    start = time()
    qtd_palpites = 0

    print()

    for i in range(n_games):
        from player import player

        code = sample(COLORS, CODE_LENGTH)
        HIST = []
        RES = []

        for _ in range(max_guesses):
            guess = player(HIST, RES)
            result = guess_code(guess, print_result=False, code=code)
            HIST.append(guess)
            RES.append(result)
            if result == (4, 4):
                wins += 1
                break

        win_rate = wins / (i + 1)
        qtd_palpites += len(HIST)

        print(
            "\033[F",
            f"       win rate {win_rate* 100:.3f}%",
            f" | Game {i} of {n_games} ({i/n_games * 100:.3f}%)",
            f" | Average guesses: {qtd_palpites/(i+1):.3f}",
            f" | Time {time() - start:.3f}s (estimated {(time() - start)/(i+1) * n_games:.3f}s)",
            end="\n",
            sep="",
        )
        # print("\033[F", end="")

    print(
        "\033[F",
        f"Final: win rate {(wins/n_games)* 100:.3f}%",
        f" | Game {n_games} of {n_games} ({n_games/n_games * 100:.3f}%)",
        f" | Average guesses: {qtd_palpites/n_games:.3f}",
        f" | Time {time() - start:.3f}s",
        end=" " * 100 + "\n",
        sep="",
    )


if __name__ == "__main__":
    if len(argv) == 3:
        run_game(int(argv[1]), int(argv[2]))
    elif len(argv) == 2:
        run_game(n_games=int(argv[1]))
    else:
        run_game()
