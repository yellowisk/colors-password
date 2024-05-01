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
from random import sample,randrange

# Cores disponíveis para o palpite
colors = [RED, GREEN, BLUE, YELLOW, ORANGE, BLACK, WHITE]
c_dict =  {
    1: RED,
    2: GREEN,
    3: BLUE,
    4: YELLOW,
    5: ORANGE,
    6: BLACK,
    7: WHITE
}

def convertColorToInt(guess):
    global numGuessHist
    block = []
    for el in guess:
        for color in c_dict.items():
            if color[1].__str__() == el.__str__():
                block.append(color[0])
        numGuessHist.append(block)
    return numGuessHist
            
def convertIntToColor(guess):
    block = []
    for k in range(len(guess)):
        for cor in c_dict.items():
            if cor[0] == guess[k]:
                block.append(cor[1])
    return block

## Deletes all lists that contain the guess' numbers, regardless of any order
def delGeneral(numGuessHist,resHist):
    guess=numGuessHist[-1]
    if resHist[-1][0]!=4:
        1234
        global possibilities
        copia = possibilities.copy()
        for i in copia:
            if guess[0] in i and guess[1] in i and guess[2] in i and guess[3] in i:
                listaPesos.remove(listaPesos[possibilities.index(i)])
                possibilities.remove(i)
        
        return possibilities   
    
def delIfFour(numGuessHist,res_hist):
    guess=numGuessHist[-1]
    global possibilities
    copia=possibilities.copy()
    if res_hist[-1][0]==4:
        for i in copia:
            if guess[0] not in i or guess[1] not in i or guess[2] not in i  or guess[3] not in i:
                listaPesos.remove(listaPesos[possibilities.index(i)])
                possibilities.remove(i)

def delIfZero(numGuessHist,resHist):
    global possibilities
    guess=numGuessHist[-1]
    copia=possibilities.copy()
    a=len(possibilities)
    if resHist[-1][1]==0:
        for i in copia:
            if i[0]==guess[0] or i[1]==guess[1] or i[2]==guess[2] or i[3]==guess[3]:
                listaPesos.remove(listaPesos[possibilities.index(i)])
                possibilities.remove(i)

def delLastGuess(numGuessHist):
    global possibilities
    try:
        listaPesos.remove(listaPesos[possibilities.index(numGuessHist[-1])])
        possibilities.remove(numGuessHist[-1])
    except:
        pass

def delCerteza(numGuessHist,res_hist):
    global possibilities
    global listaPesos
    copia=possibilities.copy()
    guess=numGuessHist[-1]
    if(res_hist[-1][1]!=0):
        for i in copia:
            cont=0
            if i[0]==guess[0]:
                cont+=1
            if i[1]==guess[1]:
                cont+=1
            if i[2]==guess[2]:
                cont+=1
            if i[3]==guess[3]:
                cont+=1
            if cont!=res_hist[-1][1]:
                del listaPesos[possibilities.index(i)]
                possibilities.remove(i)


def addPesoPos(numGuessHist,res_hist):
    global possibilities
    global listaPesos
    copia=possibilities.copy()
    guess=numGuessHist[-1]
    if(res_hist[-1][1]!=0):
        for i in copia:
            cont=0
            if i[0]==guess[0]:
                cont+=1
            if i[1]==guess[1]:
                cont+=1
            if i[2]==guess[2]:
                cont+=1
            if i[3]==guess[3]:
                cont+=1
            if cont==res_hist[-1][1]:
                listaPesos[possibilities.index(i)]+=1

def addPesoEx(numGuessHist,res_hist):
    guess=numGuessHist[-1]
    global possibilities
    global listaPesos
    copia=possibilities.copy()
    for i in copia:
        cont=0
        if i[0] in guess:
            cont+=1
        if i[1] in guess:
            cont+=1
        if i[2] in guess:
            cont+=1
        if i[3] in guess:
            cont+=1
        if cont==res_hist[-1][0]:
            listaPesos[possibilities.index(i)]+=1

def zerarPesos():
    global listaPesos
    global possibilities
    listaPesos = [0]*len(possibilities)

def todosCasos():
    global possibilities
    try:
        possibilities[0]
    except:
        possibilities=[]
        for i in range(1,8):
            for j in range(1,8):
                for k in range(1,8):
                    for l in range(1,8):
                        if i!=j!=k!=l and j!=i!=k!=l and k!=j!=i!=l and l!=j!=k!=i:
                            possibilities.append([i,j,k,l])

def getRandom(pesos: list, possibilities: list):
    higher = max(pesos)
    nextGuess = None
    if pesos.count(higher) > 1:
        while nextGuess == None:
                index = randrange(len(pesos))
                if pesos[index] == higher:
                    nextGuess = possibilities[index]
                    return nextGuess
    else:
        return possibilities[pesos.index(higher)]
    
def reset():
    global possibilities
    global listaPesos
    global cont
    global numGuessHist
    numGuessHist=[]
    possibilities=[]
    listaPesos=[0]*840

def player(guess_hist, res_hist):
    global cont
    if guess_hist==[]:
        reset()
        todosCasos()
    else:
        convertColorToInt(guess_hist[-1])
        delGeneral(numGuessHist,res_hist)
        delIfZero(numGuessHist,res_hist)
        delIfFour(numGuessHist, res_hist)
        delLastGuess(numGuessHist)
        delCerteza(numGuessHist,res_hist)
        #zerarPesos()
        addPesoEx(numGuessHist,res_hist)
        addPesoPos(numGuessHist,res_hist)

    return convertIntToColor(getRandom(listaPesos,possibilities))
