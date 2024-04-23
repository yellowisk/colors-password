#!/usr/bin/env python3
"""
Implemente aqui o seu código para o jogador.

Seu principal objetivo é implementar a função `player`, que deve retornar uma lista de 4 cores, o seu próximo palpite.
Como exemplo, a função abaixo retorna um palpite aleatório.

Dicas:
- Você pode implementar outras funções para auxiliar a função `player`.
- Você pode salvar informações entre os palpites usando variáveis globais (fora de qualquer função).
"""
from colors import *
from random import sample

# Cores disponíveis para o palpite
colors = [RED, GREEN, BLUE, YELLOW, ORANGE, BLACK, WHITE]
c_dict =  {
    1: "🟥",
    2: "🟩",
    3: "🟦",
    4: "🟨",
    5: "🟧",
    6: "⬛",
    7: "⬜"
}
def convertColorToInt(guess_hist):
    global numGuessHist
    numGuessHist = []
    for guess in guess_hist:
        block = []
        for k in range(len(guess)):
            for color in c_dict.items():
                if color[1] == guess[k]:
                    block.append(color[0])
        numGuessHist.append(block)
    return numGuessHist
            


## Deletes all lists that contain the guess' numbers, regardless of any order
def delGeneral(guess,resHist):
    if resHist[-1][0]!=4:
        global possibilities
        valid = []
        for i in possibilities:
            removable = True
            for j in range(len(guess)):
                if guess[j] not in i:
                    removable = False
                    break
            if removable == False:
                valid.append(i)
        possibilities.clear()
        possibilities.extend(valid)
        return possibilities   

def todosCasos():
    global possibilities
    try:
        possibilities[0]
    except:
        casosrepetido=[]
        for i in range(1,8):
            for j in range(1,8):
                for k in range(1,8):
                    for l in range(1,8):
                        casosrepetido.append([i,j,k,l])
        possibilities=casosrepetido.copy()
        for i in casosrepetido:
            for j in i:
                if i.count(j)>1:
                    possibilities.remove(i)
                    break


def player(guess_hist, res_hist):
    todosCasos()

    convertColorToInt([["⬜", "🟩", "⬛", "🟥"],["🟧", "🟩", "⬛", "🟥"]])
    print('++',numGuessHist)
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

    return sample(colors, 4)  # Exemplo: retorna um palpite aleatório
