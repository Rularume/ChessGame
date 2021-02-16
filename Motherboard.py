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