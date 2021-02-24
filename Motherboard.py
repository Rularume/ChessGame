from Rules import *

def pointed(x,y):
    x-=xshift
    for i in range(8):
        for j in range(8):
            #print(x,i*squarelen,(i+1)*squarelen,"\n",y,j*squarelen,(j+1)*squarelen)
            if x>i*squarelen and x<(i+1)*squarelen and y>j*squarelen and y<(j+1)*squarelen:
                return(i,j)
    return None


def Indexer(L,x,y):
    for elmt in L:
        if elmt.pos==pointed(x,y):
            return elmt
    return None

def PiecetoPix(i,j):
    return((i+0.1)*squarelen+xshift,(j+0.1)*squarelen)


def Center(i,j):
    return((i+0.5)*squarelen+xshift,(j+0.5)*squarelen)

def Corner(i,j):
    return(i*squarelen+xshift,j*squarelen)

def BlackKing(L):
    return [elmt for elmt in L if elmt.name=="Black King"][0]

def WhiteKing(L):
    return [elmt for elmt in L if elmt.name=="White King"][0]


def NextWorld(L,piece,dest,eat=False):
    if piece!=None:
        eatable=Indexer(L,*PiecetoPix(*dest))
        if eat and eatable!=None:
            eatable.White= not(eatable.White)
        Temp=copy(piece.pos)
        piece.Swap(dest)
        #print(Temp,piece.pos)
        if piece.White:
            res= WhiteKing(L).Echec(L)
        else:
            res= BlackKing(L).Echec(L)
        piece.Swap(Temp)
        if eat:
            eatable.White= not(eatable.White)
        return not(res)
    return True


def Anyone(L,piece):
    return [NextWorld(L,piece,elmts) for elmts in (piece.Allowed(L)+piece.Eat(L))]