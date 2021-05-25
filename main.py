
# Hiperparametros
from QLearn import QLearn
from menu import Menu

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

config =[
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

menu = Menu(QLearn(alfa, gama, epsilon, epsilonDecay, epsilonMin, rewards, config))

menu.start()
#a.train()
#a.printBestDirections()
#a.giveDirectionsFromPosition(0, 4)
