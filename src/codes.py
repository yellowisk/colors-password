#!/usr/bin/env python3
"""
Contem o código secreto e a função para verificar o palpite.
"""

from colors import *
from random import sample

# Lista de cores disponíveis
COLORS = [RED, GREEN, BLUE, YELLOW, ORANGE, BLACK, WHITE]
CODE_LENGTH = 4  # Tamanho do código secreto

HIST = []  # Histórico de palpites
RES = []  # Histórico de resultados
CODE = sample(COLORS, CODE_LENGTH)  # Código secreto


def guess_code(guess, print_result=True, code=CODE):
    """
    Função para verificar o palpite do jogador.

    guessed_code: lista de 4 cores

    Retorna uma tupla com a quantidade de cores corretas e a quantidade de cores
    na posição correta.
    """
    # Se o código for inválido, retorna (0, 0)
    if (
        # Se alguma cor não estiver na lista de cores
        any(c not in COLORS for c in guess)
        # Se houver cores repetidas ou menos de 4 cores
        or len(set(guess)) < CODE_LENGTH
    ):
        return (0, 0)

    correct_colors = sum(c in code for c in guess)
    correct_positions = sum(c == g for c, g in zip(code, guess))

    HIST.append(guess)
    RES.append((correct_colors, correct_positions))

    # Imprime o palpite e o resultado
    if len(RES) < 10 and print_result:
        print(f"({len(RES)}):    ", *guess, f" => {RES[-1]}     ")
    elif len(RES) == 10 and print_result:
        print(f"({len(HIST)}):   ", *guess, f" => {RES[-1]}     ")

    # Retorna o resultado
    return RES[-1]
