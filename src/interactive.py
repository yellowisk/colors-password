#!/usr/bin/env python3
"""
Módulo que implementa a interface interativa do jogo.

"""


def match_input_to_colors(code):
    """
    Função que transforma o input do usuário em objetos da classe Color.

    Como entrada, aceita-se qualquer string que comece com a palavra correspondente a uma cor, sem ambiguidades.

    Parâmetros:
    - code: lista de strings com as cores

    Retorna:
    - lista de objetos da classe Color
    """

    from colors import RED, GREEN, BLUE, YELLOW, ORANGE, BLACK, WHITE

    color_dict = {
        "vermelho": RED,
        "verde": GREEN,
        "azul": BLUE,
        "amarelo": YELLOW,
        "laranja": ORANGE,
        "preto": BLACK,
        "branco": WHITE,
    }

    for i, c in enumerate(code):
        for color in color_dict:
            if color.startswith(c.lower()):
                code[i] = color_dict[color]
                break

    return code


def player(guess_hist, res_hist):
    """
    Função principal do jogador.

    Esta função deve retornar o seu palpite, que deve ser uma lista de 4 cores.
    As cores disponíveis são: RED, GREEN, BLUE, YELLOW, ORANGE, BLACK, WHITE.

    Parâmetros:
    - guess_hist: lista de palpites anteriores
    - res_hist: lista de resultados anteriores

    Retorna:
    - lista de 4 cores

    Exemplo:
    return [RED, GREEN, BLUE, YELLOW]
    """
    # print to delete the last line in stdin
    code = input().split()
    print("\033[F", end="")

    return match_input_to_colors(code)
