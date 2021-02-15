from Images import *

def Occupied(L,i,j):
    for elmt in L:
        if i<0 or i>7 or j<0 or j>7 or elmt.pos==(i,j):
            return True
    return False

class Piece():
    def __init__(self,i,j,name,piece,color):
        self.pos=(i,j)
        self.White=color
        self.name=name
        self.image=piece[0]
        self.zoom=piece[1]
    def Allowed(self,L):
        return [self.pos]


class Pawn(Piece):
    """ def Movements(self):
        if self.White:
            return[(self.pos[0],self.pos[1]-(k+1)) for k in range (2)]
        return[(self.pos[0],self.pos[1]+(k+1)) for k in range (2)] """

    def Allowed(self,L):
        result=[]
        if self.White:
            if self.pos[1]==6:
                for k in range(2):
                    if not(Occupied(L,self.pos[0],self.pos[1]-(k+1))):
                        result.append((self.pos[0],self.pos[1]-(k+1)))
                    else:
                        break
            else:
                if not(Occupied(L,self.pos[0],self.pos[1]-1)):
                    result.append((self.pos[0],self.pos[1]-1))
    
        else:
            if self.pos[1]==1:
                for k in range(2):
                    if not(Occupied(L,self.pos[0],self.pos[1]+(k+1))):
                        result.append((self.pos[0],self.pos[1]+(k+1)))
                    else:
                        break
            else:
                if not(Occupied(L,self.pos[0],self.pos[1]+1)):
                    result.append((self.pos[0],self.pos[1]+1))
        return(result)

class King(Piece):
    """ def Movements(self):
        return[(self.pos[0]+i,self.pos[1]+j) for i in range(-1,2) for j in range(-1,2) if i!=0 or j!=0]   """ 

    def Allowed(self,L):
        result=[]
        for i in range(-1,2):
            for j in range(-1,2):
                if (j!=0 or i!=0) and not(Occupied(L,self.pos[0]+i,self.pos[1]+j)):
                    result.append((self.pos[0]+i,self.pos[1]+j))
        return result

class Queen(Piece):
    """ def Movements(self):
        return([(self.pos[0]+i,self.pos[1]+j) for i in range(-7,8) for j in range(-7,8) if (i==0 and j!=0) or (j==0 and i!=0) or (abs(i)-abs(j))==0])
    """

    def Allowed(self,L):
        result=[]
        for i in range(1,8):
            if not(Occupied(L,self.pos[0]+i,self.pos[1])):
                result.append((self.pos[0]+i,self.pos[1]))
            else:
                break
        for i in range(1,8):
            if not(Occupied(L,self.pos[0]-i,self.pos[1])):
                result.append((self.pos[0]-i,self.pos[1]))
            else:
                break
        for j in range(1,8):
            if not(Occupied(L,self.pos[0],self.pos[1]+j)):
                result.append((self.pos[0],self.pos[1]+j))
            else:
                break
        for j in range(1,8):
            if not(Occupied(L,self.pos[0],self.pos[1]-j)):
                result.append((self.pos[0],self.pos[1]-j))
            else:
                break
        for i in range(1,8):
            if not(Occupied(L,self.pos[0]+i,self.pos[1]+i)):
                result.append((self.pos[0]+i,self.pos[1]+i))
            else:
                break
        for i in range(1,8):
            if not(Occupied(L,self.pos[0]+i,self.pos[1]-i)):
                result.append((self.pos[0]+i,self.pos[1]-i))
            else:
                break
        for i in range(1,8):
            if not(Occupied(L,self.pos[0]-i,self.pos[1]+i)):
                result.append((self.pos[0]-i,self.pos[1]+i))
            else:
                break
        for i in range(1,8):
            if not(Occupied(L,self.pos[0]-i,self.pos[1]-i)):
                result.append((self.pos[0]-i,self.pos[1]-i))
            else:
                break
        return result

class Rook(Piece):
    def Allowed(self,L):
        result=[]
        for i in range(1,8):
            if not(Occupied(L,self.pos[0]+i,self.pos[1])):
                result.append((self.pos[0]+i,self.pos[1]))
            else:
                break
        for i in range(1,8):
            if not(Occupied(L,self.pos[0]-i,self.pos[1])):
                result.append((self.pos[0]-i,self.pos[1]))
            else:
                break
        for j in range(1,8):
            if not(Occupied(L,self.pos[0],self.pos[1]+j)):
                result.append((self.pos[0],self.pos[1]+j))
            else:
                break
        for j in range(1,8):
            if not(Occupied(L,self.pos[0],self.pos[1]-j)):
                result.append((self.pos[0],self.pos[1]-j))
            else:
                break
        return result


class Bishop(Piece):
    def Allowed(self,L):
        result=[]
        for i in range(1,8):
            if not(Occupied(L,self.pos[0]+i,self.pos[1]+i)):
                result.append((self.pos[0]+i,self.pos[1]+i))
            else:
                break
        for i in range(1,8):
            if not(Occupied(L,self.pos[0]+i,self.pos[1]-i)):
                result.append((self.pos[0]+i,self.pos[1]-i))
            else:
                break
        for i in range(1,8):
            if not(Occupied(L,self.pos[0]-i,self.pos[1]+i)):
                result.append((self.pos[0]-i,self.pos[1]+i))
            else:
                break
        for i in range(1,8):
            if not(Occupied(L,self.pos[0]-i,self.pos[1]-i)):
                result.append((self.pos[0]-i,self.pos[1]-i))
            else:
                break
        return result


class Knight(Piece):
    def Allowed(self,L):
        result=[]
        i=-2
        for j in range(-1,2,2):
            if not(Occupied(L,self.pos[0]+i,self.pos[1]+j)):
                result.append((self.pos[0]+i,self.pos[1]+j))

            if not(Occupied(L,self.pos[0]+j,self.pos[1]+i)):
                result.append((self.pos[0]+j,self.pos[1]+i))

            if not(Occupied(L,self.pos[0]-i,self.pos[1]+j)):
                result.append((self.pos[0]-i,self.pos[1]+j))

            if not(Occupied(L,self.pos[0]+j,self.pos[1]-i)):
                result.append((self.pos[0]+j,self.pos[1]-i))
        return result



class chess():
    def __init__(self):
        self.L=[]
        for k in range(8):
            self.L.append(Rook(0,0,"Black Rook",Tn,False))
            self.L.append(Knight(1,0,"Black Knight",Cn,False))
            self.L.append(Bishop(2,0,"Black Bishop",Fn,False))
            self.L.append(Queen(3,0,"Black Queen",Dn,False))
            self.L.append(King(4,0,"Black King",Rn,False))
            self.L.append(Bishop(5,0,"Black Bishop",Fn,False))
            self.L.append(Knight(6,0,"Black Knight",Cn,False))
            self.L.append(Rook(7,0,"Black Rook",Tn,False))
            self.L.append(Pawn(k,1,"Black Pawn",Pn,False))

            self.L.append(Rook(0,7,"White Rook",Tb,True))
            self.L.append(Knight(1,7,"White Knight",Cb,True))
            self.L.append(Bishop(2,7,"White Bishop",Fb,True))
            self.L.append(Queen(3,7,"White Queen",Db,True))
            self.L.append(King(4,7,"White King",Rb,True))
            self.L.append(Bishop(5,7,"White Bishop",Fb,True))
            self.L.append(Knight(6,7,"White Knight",Cb,True))
            self.L.append(Rook(7,7,"White Rook",Tb,True))
            self.L.append(Pawn(k,6,"White Pawn",Pb,True))
            
        

