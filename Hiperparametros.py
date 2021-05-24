
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

# print("Em cima vanessa")
# for i in range(4):
#     print(f"{Direcoes(i)}")
#     print(a.QState[f'86{i}'])

# print()
# print("Esquerda vanessa")
# for i in range(4):
#     print(f"{Direcoes(i)}")
#     print(a.QState[f'95{i}'])

# print()
# print("Direita vanessa")
# for i in range(4):
#     print(f"{Direcoes(i)}")
#     print(a.QState[f'97{i}'])
a.giveDirectionsFromPosition(5, 5)

# initialState = [
#     [b, c, c, c, b, c, b, b, c, b],
#     [b, p, b, b, b, b, b, p, b, p],
#     [b, c, c, b, c, c, b, b, b, c],
#     [b, b, b, b, b, b, c, c, b, c],
#     [c, p, p, c, b, p, a, b, b, b],
#     [b, b, b, c, b, b, c, c, c, b],
#     [b, c, c, c, p, c, c, c, p, b],
#     [b, b, b, p, c, b, p, b, b, b],
#     [c, p, b, b, b, b, b, b, b, c],
#     [p, c, b, c, c, t, b, c, b, p],
# ]