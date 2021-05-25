import pickle
from QLearn import QLearn

class Menu():
    def __init__(self, agent : QLearn):
        self.agent = agent

    def checkIfTrained(self):
        check = False
        try:
            f = open("qstates.pkl")
            check = True
            f.close()
        except IOError:
            check = False
        finally:
            return check

    def loadQStates(self):
        f = open("qstates.pkl","rb")
        qstates = pickle.load(f)
        f.close()

        self.agent.QState = qstates

    def getCarPos(self):
        x = int(input("Digite a posioção X do carro: "))
        y = int(input("Digite a posioção Y do carro: "))
        self.agent.giveDirectionsFromPosition(x, y)

    def start(self):
        while True:
            print()
            print("Digite uma opção:")
            res = int(input("1 - Treinar o Modelo \n2 - Digitar a posição do carro\n3 - Sair\n"))

            if res == 1 :
                print("Iniciando treinamento...")
                self.agent.train()
            
            elif res == 2:
                if self.checkIfTrained():
                    
                    self.loadQStates()
                    self.getCarPos()        
                else:
                    print("Modelo não treinado ainda. Iniciando treinamento...")
                    self.agent.train()
            elif res == 3:
                break