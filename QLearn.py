from random import choice, random
from enum import Enum
import numpy as np
import pickle

c = 'c'
b = 'b'
p = 'p'
a = 'a'
t = 't'

class Direcoes(Enum):
    Cima = 0
    Direita = 1
    Baixo = 2
    Esquerda = 3

directionsIcons = ['↑','→','↓','←']

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class QLearn():

    MAXGEN = 2000

    def __init__(self, alfa, gama, epsilon, epsilonDecay, epsilonMin, rewards):
        self.alfa = alfa
        self.gama = gama
        self.epsilon = epsilon
        self.epsilonDecay = epsilonDecay
        self.epsilonMin = epsilonMin
        self.rewards = rewards
        self.config = [
            [b, c, c, c, b, c, b, b, c, b],
            [b, p, b, b, b, b, b, p, b, p],
            [b, c, c, b, c, c, b, b, b, c],
            [b, b, b, b, b, b, c, c, b, c],
            [c, p, p, c, b, p, b, b, b, b],
            [b, b, b, c, b, b, c, c, c, b],
            [b, c, c, c, p, b, c, c, p, b],
            [b, b, b, p, c, b, p, b, b, b],
            [c, p, b, b, b, b, b, b, b, c],
            [p, c, b, c, c, t, b, c, b, p],
        ]
        #self.currentState = []
        self.previousQState = {}
        self.QState = {}
        
    def initializeQStates(self):
        for i in range(10):
            for j in range(10):
                #if self.config[i][j] != c and self.config[i][j] != p and self.config[i][j] != t:
                    for d in Direcoes:
                        self.previousQState[f"{i}{j}{d.value}"] = 0
                        self.QState[f"{i}{j}{d.value}"] = 0

    def isValidRow(self, i, j):
        return self.config[i][j] != c and self.config[i][j] != p and self.config[i][j] != t

    def checkFuturePosition(self, state, action):
        i, j = int(state[0]) , int(state[1])
        
        if action == Direcoes.Cima:
            if i - 1 < 0 : return state, self.config[i][j]
            return f"{i - 1}{j}", self.config[i-1][j]
        elif action == Direcoes.Direita:
            if j + 1 >= 10 : return state, self.config[i][j]
            return f"{i}{j + 1}", self.config[i][j+1]
        elif action == Direcoes.Baixo:
            if i + 1 >= 10 : return state, self.config[i][j]
            return f"{i + 1}{j}", self.config[i+1][j]
        else: 
            if j - 1 < 0: return state, self.config[i][j]
            return f"{i}{j - 1}", self.config[i][j-1]


    def reward(self, state, action):
        futurePos, symbol = self.checkFuturePosition(state, action)
        if futurePos == state:
            return self.rewards[c]
        else:
            return self.rewards[symbol]

    def Q(self, state, action):
        futurePos, symbol = self.checkFuturePosition(state, action)

        val = []
        if symbol in [c, p, t]:
            val.append(self.rewards[symbol])
        else:
            for d in Direcoes:
                val.append(self.previousQState[f"{futurePos}{d.value}"])

        return self.previousQState[f"{state}{action.value}"] + self.alfa * (self.reward(state, action) + self.gama * np.max(val) - self.previousQState[f"{state}{action.value}"])

    def getRandomBlankPositions(self):
        pos = []
        for i in range(10):
            for j in range(10):
                if self.config[i][j] == b:
                    pos.append((i,j))
        return choice(pos)

    def getAllBlankPositions(self):
        pos = []
        for i in range(10):
            for j in range(10):
                if self.config[i][j] == b:
                    pos.append((i,j))
        return pos

    def train(self):
        self.initializeQStates()

        for gen in range(self.MAXGEN):
            if gen % 100 == 0: print(f"Geração {gen}")
            randomPosAgent = self.getRandomBlankPositions()
            
            state = f"{randomPosAgent[0]}{randomPosAgent[1]}"
            
            for _ in range(200):
                self.QState[f"{state}{ Direcoes.Cima.value}"] = self.Q(state, Direcoes.Cima)
                self.QState[f"{state}{ Direcoes.Direita.value}"] = self.Q(state, Direcoes.Direita)
                self.QState[f"{state}{ Direcoes.Baixo.value}"] = self.Q(state, Direcoes.Baixo)
                self.QState[f"{state}{ Direcoes.Esquerda.value}"] = self.Q(state, Direcoes.Esquerda)
                
                possibleActions =  [ self.QState[f"{state}{ Direcoes.Cima.value}"] ,
                                    self.QState[f"{state}{ Direcoes.Direita.value}"] ,
                                    self.QState[f"{state}{ Direcoes.Baixo.value}"] ,
                                    self.QState[f"{state}{ Direcoes.Esquerda.value}"] ]

                action = None
                if random() < self.epsilon:
                    action = choice(list(Direcoes))
                else: 
                    action = Direcoes(np.argmax(possibleActions))

                state, _ = self.checkFuturePosition(state, action)

                self.previousQState = self.QState.copy()

            self.epsilon *= self.epsilonDecay
            self.epsilon = max(self.epsilon, self.epsilonMin)

        #Salvar os QStates
        f = open("qstates.pkl","wb")
        pickle.dump(self.QState, f)
        f.close()

    def printMatrix(self, matrix):
        for i in range(10):
            print(" | ".join(matrix[i]))

    def giveDirectionsFromPosition(self, i , j):
        starterI = i
        starterJ = j
        state = f"{i}{j}"
        path = []
        
        print("Direções escolhidas:")
        while (self.config[i][j] != t):
            possibleActions =  [ self.QState[f"{state}{ Direcoes.Cima.value}"] ,
                                self.QState[f"{state}{ Direcoes.Direita.value}"] ,
                                self.QState[f"{state}{ Direcoes.Baixo.value}"] ,
                                self.QState[f"{state}{ Direcoes.Esquerda.value}"] ]
            action = Direcoes(np.argmax(possibleActions))
            print(f"Direção: {bcolors.FAIL}{directionsIcons[action.value]}{bcolors.ENDC}", f"QValue {possibleActions[action.value]}")
            state, _ = self.checkFuturePosition(state, action)
            i, j = int(state[0]), int(state[1])
            path.append((i,j))
        print()
        self.printPath(starterI, starterJ, path)

    def printPath(self, i, j, path):
            matrix = self.config.copy()
            for x in range(10):
                for y in range(10):
                    if matrix[x][y] == "b":
                        matrix[x][y] = " "
                    else:
                        matrix[x][y] = f"{bcolors.OKCYAN}{matrix[x][y]}{bcolors.ENDC}"

            matrix[i][j] = f"{bcolors.WARNING}A{bcolors.ENDC}"

            for position in path:
                matrix[position[0]][position[1]] = f"{bcolors.FAIL}.{bcolors.ENDC}"

            matrix[path[-1][0]][path[-1][1]] = f"{bcolors.OKGREEN}T{bcolors.ENDC}"
            
            self.printMatrix(matrix)