from Images import *
from copy import copy,deepcopy
def InGrid(i,j):
    return (i<0 or i>7 or j<0 or j>7)

def Reverse(L,i,j):
    for elmt in L:
        if elmt.pos==(i,j):
            return elmt
    return None

def Occupied(L,i,j):
    if InGrid(i,j) or Reverse(L,i,j)!=None:
            return True
    return False

def unpack(L):
    res= []
    for elmt in L:
        for k in range(len(elmt)):
            res.append(elmt[k])
    return res


class Piece():
    def __init__(self,i,j,name,piece,color):
        self.pos=(i,j)
        self.White=color
        self.name=name
        self.image=piece[0]
        self.zoom=piece[1]
        self.origin=self.pos
    def Allowed(self,L):
        return [self.pos]
    def Eat(self,L):
        return[]
    def Swap(self,pos):
        *a,i,j=pos
        #print("Mani",self.pos,pos)
        if self.name=="White Pawn" and self.pos[1]-j==2:
            #print("Manipd")
            8
        self.pos=pos
    def Opponement(self,L,target,result):
        if self.White:
            if Reverse(L,*target)!=None and not(Reverse(L,*target).White):
                result.append(target)
        else:
            if Reverse(L,*target)!=None and (Reverse(L,*target).White):
                result.append(target)
        return result
    def Test(self,L):
        return []

    def Row(self,L):
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
    def Roweat(self,L):
        result=[]
        for i in range(1,8):
            target=self.pos[0]+i,self.pos[1]
            if Occupied(L,*target):
                result=self.Opponement(L,target,result)
                break
        for i in range(1,8):
            target=self.pos[0]-i,self.pos[1]
            if Occupied(L,*target):
                result=self.Opponement(L,target,result)
                break
        for i in range(1,8):
            target=self.pos[0],self.pos[1]+i
            if Occupied(L,*target):
                result=self.Opponement(L,target,result)
                break
        for i in range(1,8):
            target=self.pos[0],self.pos[1]-i
            if Occupied(L,*target):
                result=self.Opponement(L,target,result)
                break
        return result


class Pawn(Piece):
    
    def Cases(self,L):
        return(self.Allowed(L),self.Eat(L))
    """ def Movements(self):
        if self.White:
            return[(self.pos[0],self.pos[1]-(k+1)) for k in range (2)]
        return[(self.pos[0],self.pos[1]+(k+1)) for k in range (2)] """

    def Allowed(self,L):
        result=[]
        if self.White:
            if (self.pos==self.origin):
                for k in range(2):
                    if not(Occupied(L,self.pos[0],self.pos[1]-(k+1))):
                        result.append((self.pos[0],self.pos[1]-(k+1)))
                    else:
                        break
            else:
                if not(Occupied(L,self.pos[0],self.pos[1]-1)):
                    result.append((self.pos[0],self.pos[1]-1))
    
        else:
            if (self.pos==self.origin):
                for k in range(2):
                    if not(Occupied(L,self.pos[0],self.pos[1]+(k+1))):
                        result.append((self.pos[0],self.pos[1]+(k+1)))
                    else:
                        break
            else:
                if not(Occupied(L,self.pos[0],self.pos[1]+1)):
                    result.append((self.pos[0],self.pos[1]+1))
        return(result)

    def Eat(self,L):
        result=[]
        if self.White:
            for k in range(-1,2,2):
                target=(self.pos[0]+k,self.pos[1]-1)
                if Occupied(L,*target) and Reverse(L,*target)!=None and not(Reverse(L,*target).White):
                    result.append(target)
        else:
            for k in range(-1,2,2):
                target=(self.pos[0]+k,self.pos[1]+1)
                if Occupied(L,*target) and Reverse(L,*target)!=None and (Reverse(L,*target).White):
                    result.append(target)
        return result

class King(Piece):
    
    def Cases(self,L):
        return(self.Allowed(L),self.Eat(L))
    """ def Movements(self):
        return[(self.pos[0]+i,self.pos[1]+j) for i in range(-1,2) for j in range(-1,2) if i!=0 or j!=0]   """ 

    def Allowed(self,L):
        result=[]
        for i in range(-1,2):
            for j in range(-1,2):
                if (j!=0 or i!=0) and not(Occupied(L,self.pos[0]+i,self.pos[1]+j)):
                    result.append((self.pos[0]+i,self.pos[1]+j))
        return result

    def Eat(self,L):
        result=[]
        for i in range(-1,2):
            for j in range(-1,2):
                target=self.pos[0]+i,self.pos[1]+j
                if (j!=0 or i!=0) and (Occupied(L,*target)):
                    result=self.Opponement(L,target,result)
        return result
    def Test(self,L):
        return [elmt.name for elmt in L]

    def Echec(self,L):
        if self.White:
            #print("White King",self.pos in unpack([elmt.Eat(L) for elmt in L if not(elmt.White)]),unpack([elmt.Eat(L) for elmt in L if not(elmt.White)]),self.pos )
            return self.pos in unpack([elmt.Eat(L) for elmt in L if not(elmt.White)])
        else:
            #print("Black King",self.pos in unpack([elmt.Eat(L) for elmt in L if (elmt.White)]),unpack([elmt.Eat(L) for elmt in L if (elmt.White)]),self.pos)
            return self.pos in unpack([elmt.Eat(L) for elmt in L if (elmt.White)])

class Queen(Piece):
    
    def Cases(self,L):
        return(self.Allowed(L),self.Eat(L))
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

    def Eat(self,L):
        result=[]
        for i in range(1,8):
            target=self.pos[0]+i,self.pos[1]
            if Occupied(L,*target):
                result=self.Opponement(L,target,result)
                break
        for i in range(1,8):
            target=self.pos[0]-i,self.pos[1]
            if Occupied(L,*target):
                result=self.Opponement(L,target,result)
                break
        for i in range(1,8):
            target=self.pos[0],self.pos[1]+i
            if Occupied(L,*target):
                result=self.Opponement(L,target,result)
                break
        for i in range(1,8):
            target=self.pos[0],self.pos[1]-i
            if Occupied(L,*target):
                result=self.Opponement(L,target,result)
                break
        for i in range(1,8):
            target=self.pos[0]+i,self.pos[1]+i
            if Occupied(L,*target):
                result=self.Opponement(L,target,result)
                break
        for i in range(1,8):
            target=self.pos[0]+i,self.pos[1]-i
            if Occupied(L,*target):
                result=self.Opponement(L,target,result)
                break
        for i in range(1,8):
            target=self.pos[0]-i,self.pos[1]+i
            if Occupied(L,*target):
                result=self.Opponement(L,target,result)
                break
        for i in range(1,8):
            target=self.pos[0]-i,self.pos[1]-i
            if Occupied(L,*target):
                result=self.Opponement(L,target,result)
                break
        return result

class Rook(Piece):

    def Cases(self,L):
        return (self.Row(L),self.Roweat(L))

    def Allowed(self,L):
        return self.Row(L)

    def Eat(self,L):
        return self.Roweat(L)


class Bishop(Piece):
    def Cases(self,L):
        return(self.Allowed(L),self.Eat(L))

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

    def Eat(self,L):
        result=[]
        for i in range(1,8):
            target=self.pos[0]+i,self.pos[1]+i
            if Occupied(L,*target):
                result=self.Opponement(L,target,result)
                break
        for i in range(1,8):
            target=self.pos[0]+i,self.pos[1]-i
            if Occupied(L,*target):
                result=self.Opponement(L,target,result)
                break
        for i in range(1,8):
            target=self.pos[0]-i,self.pos[1]+i
            if Occupied(L,*target):
                result=self.Opponement(L,target,result)
                break
        for i in range(1,8):
            target=self.pos[0]-i,self.pos[1]-i
            if Occupied(L,*target):
                result=self.Opponement(L,target,result)
                break
        return result


class Knight(Piece):
    
    def Cases(self,L):
        return(self.Allowed(L),self.Eat(L))
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

    def Eat(self,L):
        result=[]
        i=-2
        for j in range(-1,2,2):
            target=self.pos[0]+i,self.pos[1]+j
            if Occupied(L,*target):
                result=self.Opponement(L,target,result)

            target=self.pos[0]+j,self.pos[1]+i
            if Occupied(L,*target):
                result=self.Opponement(L,target,result)

            target=self.pos[0]-i,self.pos[1]+j
            if Occupied(L,*target):
                result=self.Opponement(L,target,result)

            target=self.pos[0]+j,self.pos[1]-i
            if Occupied(L,*target):
                result=self.Opponement(L,target,result)
        return result


class chess():
    def __init__(self):
        self.L=[]
        self.L.append(Rook(0,0,"Black Rook",Tn,False))
        self.L.append(Knight(1,0,"Black Knight",Cn,False))
        self.L.append(Bishop(2,0,"Black Bishop",Fn,False))
        self.L.append(Queen(3,0,"Black Queen",Dn,False))
        self.L.append(King(4,0,"Black King",Rn,False))
        self.L.append(Bishop(5,0,"Black Bishop",Fn,False))
        self.L.append(Knight(6,0,"Black Knight",Cn,False))
        self.L.append(Rook(7,0,"Black Rook",Tn,False))
        for k in range(8):
            self.L.append(Pawn(k,1,"Black Pawn",Pn,False))
            self.L.append(Pawn(k,6,"White Pawn",Pb,True))

        self.L.append(Rook(0,7,"White Rook",Tb,True))
        self.L.append(Knight(1,7,"White Knight",Cb,True))
        self.L.append(Bishop(2,7,"White Bishop",Fb,True))
        self.L.append(Queen(3,7,"White Queen",Db,True))
        self.L.append(King(4,7,"White King",Rb,True))
        self.L.append(Bishop(5,7,"White Bishop",Fb,True))
        self.L.append(Knight(6,7,"White Knight",Cb,True))
        self.L.append(Rook(7,7,"White Rook",Tb,True))

            
        

