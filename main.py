
# Hiperparametros

from QLearn import Direcoes, QLearn

alfa = 0.2
gama = 0.8
epsilon = 0.9
epsilonDecay = 0.7
epsilonMin = 0.2

c = 'c'
b = 'b'
p = 'p'
a = 'a'
t = 't'


rewards = {
    b : 100,
    p : -1000,
    c : -100,
    t : 500
}

a = QLearn(alfa, gama, epsilon, epsilonDecay, epsilonMin, rewards)
# a.initializeQStates()
# print(a.previousQState)

a.train()

a.giveDirectionsFromPosition(0, 4)
