#!/usr/bin/env python3
"""
Front-end do jogo utilizando Pygame.

Este arquivo é responsável por desenhar o jogo na tela e chamar a função `player` do arquivo `player.py`.
"""
try:
    import pygame
except ImportError:
    print(
        "Pygame não foi instalado. Por favor, cheque o README para mais informações ou consulte um monitor."
    )
    exit(1)
from colors import *
from codes import *

# Inicializa o Pygame
pygame.init()

# Dimensões da tela
WIDTH, HEIGHT = 300, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advinihação de Cores")


def draw_guesses():
    """
    Desenha os palpites e os resultados na tela, sempre mantendo o
    último palpite na parte inferior.
    """
    for i, (guess, (correct_colors, correct_positions)) in enumerate(
        zip(HIST[::-1], RES[::-1])
    ):
        for j, color in enumerate(guess):
            pygame.draw.rect(
                SCREEN,
                color.rgb,
                # 40 x 40 square with a 10 pixel margin
                pygame.Rect(
                    j * 50 + 10,
                    HEIGHT - (i + 1) * 50,
                    40,
                    40,
                ),
            )
        pygame.font.init()
        font = pygame.font.SysFont("Arial", 20)
        text = font.render(f"{correct_colors}/{correct_positions}", True, BLACK.rgb)
        SCREEN.blit(text, (210, HEIGHT - (i + 1) * 50 + 10))


def main(max_guesses=10, speed=0.5, interactive=False):
    """
    Função principal do jogo.

    Esta função é responsável por desenhar o jogo na tela e chamar a função `player` do arquivo `player.py`.

    Parâmetros:
    - max_guesses: número máximo de palpites
    - speed: velocidade de cada palpite
    """
    if interactive:
        from interactive import player
    else:
        from player import player

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        SCREEN.fill(GRAY.rgb)
        draw_guesses()

        # Guess a random code
        if len(RES) < max_guesses and not (len(RES) > 0 and RES[-1] == (4, 4)):
            guess_code(player(HIST, RES))

        pygame.display.flip()
        pygame.time.wait(int(speed * 1000))

    if len(RES) == max_guesses and RES[-1] != (4, 4):
        print("You lost!\nCorrect:", *CODE)
    else:
        print("You won! With only", len(RES), "guesses!")

    pygame.quit()


if __name__ == "__main__":
    main()
