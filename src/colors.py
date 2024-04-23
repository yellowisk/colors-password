#!/usr/bin/env python3

import sys


# Cores disponíveis
class color_name:
    WHITE = (255, 255, 255)
    BLACK = (40, 40, 40)
    RED = (255, 205, 210)
    GREEN = (200, 255, 201)
    BLUE = (187, 222, 251)
    YELLOW = (255, 249, 196)
    ORANGE = (218, 133, 72)
    GRAY = (224, 224, 224)  # Não pode estar na senha, mas é usada para o display


# Verifica se o terminal suporta emojis
UNICODE_SUPPORT = sys.stdout.encoding.lower().startswith("utf")


class color:
    """
    Classe para representar uma cor.

    Atributos:
    - rgb: tupla com os valores RGB da cor
    - emoji: se True, a impressão retorna um emoji da cor, caso contrário, retorna o nome da cor

    Métodos:
    - __repr__: retorna a representação da cor
    - __str__: retorna a representação da cor
    - __eq__: compara duas cores
    """

    def __init__(self, rgb) -> None:
        """
        Inicializa a cor com o valor RGB passado.

        Parâmetros:
        - rgb: tupla com os valores RGB da cor

        Exemplo:
        RED = color(color_name.RED)

        NOTE: Você não precisa criar objetos dessa classe, pois as cores já estão definidas no final do arquivo.
        """
        self.rgb = rgb
        # Caso seu terminal não suporte emojis, mude para False
        self.emoji = UNICODE_SUPPORT

    def _text(self) -> str:
        """
        Retorna o nome da cor.
        """

        match self.rgb:
            case color_name.RED:
                return "Red"
            case color_name.GREEN:
                return "Green"
            case color_name.BLUE:
                return "Blue"
            case color_name.YELLOW:
                return "Yellow"
            case color_name.ORANGE:
                return "Orange"
            case color_name.BLACK:
                return "Black"
            case color_name.WHITE:
                return "White"
            case _:
                return "Unknown"

    def _emoji(self) -> str:
        """
        Retorna um emoji da cor.
        """
        match self.rgb:
            case color_name.RED:
                return "🟥"
            case color_name.GREEN:
                return "🟩"
            case color_name.BLUE:
                return "🟦"
            case color_name.YELLOW:
                return "🟨"
            case color_name.ORANGE:
                return "🟧"
            case color_name.BLACK:
                return "⬛"
            case color_name.WHITE:
                return "⬜"
            case _:
                return "❓"

    def __repr__(self) -> str:
        """
        Retorna a representação da cor.
        """
        return self._emoji() if self.emoji else self._text()

    def __str__(self) -> str:
        """
        Retorna a representação da cor.
        """
        return self._emoji() if self.emoji else self._text()

    def __eq__(self, other) -> bool:
        """
        Compara duas cores.
        """
        return self.rgb == other.rgb

    def __hash__(self) -> int:
        """
        Retorna o hash da cor.
        """
        return hash(self.rgb)


# Cores disponíveis
# Você pode usá-las após:
# from colors import *
WHITE = color(color_name.WHITE)
BLACK = color(color_name.BLACK)
RED = color(color_name.RED)
GREEN = color(color_name.GREEN)
BLUE = color(color_name.BLUE)
YELLOW = color(color_name.YELLOW)
ORANGE = color(color_name.ORANGE)
GRAY = color(color_name.GRAY)
