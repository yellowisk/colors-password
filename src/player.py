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
from random import sample,randrange,choice
import time

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

#Cria lista com todas as possibilidades de chute
saved = []
for i in range(1,8):
            for j in range(1,8):
                for k in range(1,8):
                    for l in range(1,8):
                        if i!=j!=k!=l and j!=i!=k!=l and k!=j!=i!=l and l!=j!=k!=i:
                            saved.append([i,j,k,l])

#Transforma as cores de um chute para int
def convertColorToInt(guess):
    global numGuessHist
    block = []
    for el in guess:
        for color in c_dict.items():
            if color[1].__str__() == el.__str__():
                block.append(color[0])
    numGuessHist.append(block)
    return numGuessHist

#Transforma os ints de um chute para color      
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
        global possibilities
        copia = possibilities.copy()
        for i in copia:
            if guess[0] in i and guess[1] in i and guess[2] in i and guess[3] in i:
                listaPesos.remove(listaPesos[possibilities.index(i)])
                possibilities.remove(i)

#Se as quatro cores de um chute estiverem corretas, remove todos que não têm todas estas cores
def delIfFour(numGuessHist,res_hist):
    guess=numGuessHist[-1]
    global possibilities
    copia=possibilities.copy()
    if res_hist[-1][0]==4:
        for i in copia:
            if guess[0] not in i or guess[1] not in i or guess[2] not in i  or guess[3] not in i:
                listaPesos.remove(listaPesos[possibilities.index(i)])
                possibilities.remove(i)

#Se nenhuma cor de um chute estiver na posição correta, remove todos os chutes que têm alguma dessas cores na mesma posição do chute
def delIfZero(numGuessHist,resHist):
    global possibilities
    guess=numGuessHist[-1]
    copia=possibilities.copy()
    if resHist[-1][1]==0:
        for i in copia:
            if i[0]==guess[0] or i[1]==guess[1] or i[2]==guess[2] or i[3]==guess[3]:
                listaPesos.remove(listaPesos[possibilities.index(i)])
                possibilities.remove(i)

#Remove o último chute dado se ele estiver incorreto
def delLastGuess(numGuessHist):
    global possibilities
    try:
        listaPesos.remove(listaPesos[possibilities.index(numGuessHist[-1])])
        possibilities.remove(numGuessHist[-1])
    except:
        pass

#Remove todos os chutes que tem um número diferente de cores na mesma posição do último chute, caso eles tenham o mesmo número de cores na posição correta
def delCertezaPos(numGuessHist,res_hist):
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

#Valorizamos mais todos os chutes que tem elementos na mesma posição do último chute dado, caso eles tenham o mesmo número de cores na posição correta
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

#Remove todos os chutes que tem um número diferente de cores em qualquer posição do último chute, caso eles tenham o mesmo número de cores corretas
def delCertezaEx(numGuessHist,res_hist):
    global maximo
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
        if cont!=res_hist[-1][0]:                
            del listaPesos[possibilities.index(i)]
            possibilities.remove(i)

#Valorizamos mais todos os chutes que tem os mesmos elementos do último chute dado, caso eles tenham o mesmo número de cores corretas
def addPesoEx(numGuessHist,res_hist):
    global maximo
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

#Caso a lista de chutes não exista é atribuída a ela todos os chutes possíveis
def todosCasos(saved):
    global possibilities
    try:
        possibilities[0]
    except:
        possibilities=saved.copy()

#Dentre os chutes com maior peso, escolhemos um deles aleatoriamente
def getRandom(pesos: list, possibilities: list):
    higher = max(pesos)
    nextGuess = None
    if pesos.count(higher) > 1:
        index = randrange(len(pesos))
        nextGuess = possibilities[index]
        return nextGuess
    else:
        return possibilities[pesos.index(higher)]

#Dentre os chutes disponíveis, escolhemos um deles aleatoriamente    
def getRandomWithoutWeights(possibilities):
    return choice(possibilities)

#Reseta as variáveis para cada jogo novo
def reset():
    global possibilities
    global listaPesos
    global numGuessHist
    numGuessHist=[]
    possibilities=[]
    listaPesos=[0]*840

#Junção das funções dos casos gerais
def removalSpree(numGuessHist,resHist):
    delLastGuess(numGuessHist)
    delGeneral(numGuessHist,resHist)
    delIfZero(numGuessHist,resHist)
    delIfFour(numGuessHist,resHist)
    delCertezaPos(numGuessHist,resHist)
    delCertezaEx(numGuessHist,resHist)
    # addPesoEx(numGuessHist,resHist)
    # addPesoPos(numGuessHist,resHist)

#Joga =)
def player(guess_hist, res_hist):
    if guess_hist==[]:
        reset()
        todosCasos(saved)
        return convertIntToColor([1,2,3,4])
    if len(guess_hist)==1:
        if res_hist[-1][0]==1:
            convertColorToInt(guess_hist[-1])
            removalSpree(numGuessHist,res_hist)
            return convertIntToColor([1,5,6,7])
        else:
            convertColorToInt(guess_hist[-1])
            removalSpree(numGuessHist,res_hist)
            return convertIntToColor(getRandomWithoutWeights(possibilities))
    else:
        convertColorToInt(guess_hist[-1])
        removalSpree(numGuessHist,res_hist)
        return convertIntToColor(getRandomWithoutWeights(possibilities))