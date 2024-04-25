from Tablero import Tablero
from copy import deepcopy

class Nodo:
    def __init__(self, father=None, nums=[], dir='l'):
        self.father = father
        if self.father == None:
            self.Tablero = Tablero(nums)
        else:
            self.Tablero = Tablero(deepcopy(self.father.Tablero.nums))
            self.Tablero.makeMove(dir)

    def setChilds(self):
        self.childs = []
        for _dir in self.Tablero.moves():
            auxN = Nodo(father=self, dir=_dir)
            self.childs.append(auxN)
