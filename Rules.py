from Images import *

class Piece():
    def __init__(self,i,j,name,piece,color):
        self.pos=(i,j)
        self.White=color
        self.name=name
        self.image=piece[0]
        self.zoom=piece[1]


class Pawn(Piece):
    hasmoved=False
    def Movements(self):
        if self.White:
            return[(self.pos[0],self.pos[1]-(k+1)) for k in range (2)]
        return[(self.pos[0],self.pos[1]+(k+1)) for k in range (2)]


class chess():
    def __init__(self):
        self.L=[]
        for k in range(8):
            self.L.append(Pawn(k,1,"Black Pawn",Pn,False))
            self.L.append(Pawn(k,6,"White Pawn",Pb,True))