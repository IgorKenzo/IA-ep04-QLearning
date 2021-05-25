
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

menu = Menu(QLearn(alfa, gama, epsilon, epsilonDecay, epsilonMin, rewards))

menu.start()
#a.train()
#a.printBestDirections()
#a.giveDirectionsFromPosition(0, 4)
