#!/usr/bin/env python3
"""
Módulo de entrada do jogo.

Este arquivo é responsável por analisar os argumentos de linha de comando e chamar a função principal do jogo.

Argumentos:
--terminal, -t: Usa o terminal como interface de jogo
--max-guesses, -m: Número máximo de tentativas
--speed, -s: Velocidade de cada tentativa

Exemplo:
$ python main.py --terminal --max-guesses 10
$ python main.py
"""

import argparse

parser = argparse.ArgumentParser(description="Advinhe a senha secreta!")

# Interface de jogo, GUI por padrão
parser.add_argument(
    "--terminal",
    "-t",
    action="store_false",
    help="Usa o terminal como interface de jogo",
)

# Número de tentativas, 10 por padrão
parser.add_argument(
    "--max-guesses",
    "-m",
    type=int,
    default=10,
    help="Número máximo de tentativas",
)

# Velocidade do jogo, 0.5 por padrão
parser.add_argument(
    "--speed",
    "-s",
    type=float,
    default=0.5,
    help="Velocidade de cada tentativa",
)

# Se for para jogar o jogo interativo
parser.add_argument(
    "--interactive",
    "-i",
    action="store_true",
    help="Usa o jogo interativo",
)

if __name__ == "__main__":
    args = parser.parse_args()

    if args.terminal:
        from game import main

    else:
        from terminal import main

    main(args.max_guesses, args.speed, args.interactive)
