import pygame
import sys
from Motherboard import *

pygame.init()

clock = pygame.time.Clock()
pygame.display.set_icon(logo)
pygame.display.set_caption('Sacochade')
screen=pygame.display.set_mode(size)

#screen=pygame.display.set_mode((1920, 1080))

#any_font = pygame.font.SysFont("Blue Eyes.otf",25)
L=chess().L
def redraw_window(x,y,select,turn):
    
    Background()
    Indicator(x,y,select,turn)
    
    DrawPieces()

    
def Background():
    screen.fill(DARKGREY)
    for i in range(8):
        for j in range(8):
            if (i+j)%2==0:
                pygame.draw.rect(screen,WHITE,(xshift+i*squarelen,j*squarelen,squarelen,squarelen))
            else:
                pygame.draw.rect(screen,BROWN,(xshift+i*squarelen,j*squarelen,squarelen,squarelen))
    

def Indicator(x,y,select,turn):
    if select!=None:
        ShowMovements(select,DARKGREY,turn)
    else:
        ShowMovements(Indexer(L,x,y),MEDIUMGREY,turn)


def DrawPieces():        
    for elmt in L:
        screen.blit(elmt.image,PiecetoPix(*elmt.pos))


def ShowMovements(pointed,color,turn):
    if pointed!=None:
        
        if pointed.White and turn%2==0:
            for elmts in pointed.Allowed(L):
                if NextWorld(L,pointed,elmts):
                    pygame.draw.circle(screen,color,Center(*elmts),squarelen/8)
            
            for elmts in pointed.Eat(L):
                if NextWorld(L,pointed,elmts,True):
                    pygame.draw.circle(screen,color,Center(*elmts),squarelen*0.45,3)
        elif not(pointed.White) and turn%2==1:
            for elmts in pointed.Allowed(L):
                if NextWorld(L,pointed,elmts):
                    pygame.draw.circle(screen,color,Center(*elmts),squarelen/8)
            
            for elmts in pointed.Eat(L):
                if NextWorld(L,pointed,elmts,True):
                    pygame.draw.circle(screen,color,Center(*elmts),squarelen*0.45,3)
        


def SwapPiece(source,destination,turn):
    if destination==None:
        return None,turn
    elif destination in source.Allowed(L):
        #print("Swaped",source.name,source.pos,"to",destination)
        source.Swap(destination)
        return None,turn+1
    elif source.pos==destination:
        #print("got currented")
        return source,turn
    elif destination in source.Eat(L):
        #print(source.name,"eat",Reverse(L,*destination).name)
        L.remove(Reverse(L,*destination))
        source.Swap(destination)
        return None,turn+1
    elif Indexer(L,*PiecetoPix(*destination))!=None:
        #print(Indexer(L,*PiecetoPix(*destination)).name)
        return Indexer(L,*PiecetoPix(*destination)),turn
    else:
        #print("out of range")
        return None,turn
    
    
def __Game__():
    
    select=None
    turn=0
    clock.tick(FPS)
    while 1:
        for elmt in pygame.event.get():
            if elmt.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        x,y=pygame.mouse.get_pos()

        if mouse[0]:
            if select!=None:
                if (select.White and turn%2==1) or (not(select.White) and turn%2==0):
                    select=None
                else:
                    select,turn = SwapPiece(select,pointed(x,y),turn)
                    WK=WhiteKing(L)
                    BK=BlackKing(L)
                    #print(unpack([Anyone(L,elmt)for elmt in L if not(elmt.White)]))
                    #print("test mat",turn%2==0, WK.Echec(L), [not(any([Anyone(L,elmt) for elmt in L if elmt.White]))][0])
                    #print("test mat Black",turn%2==1, BK.Echec(L), not(any(unpack([Anyone(L,elmt)for elmt in L if not(elmt.White)]))))
                    if turn%2==1 and not(any(unpack([Anyone(L,elmt)for elmt in L if (elmt.White)]))):
                        if WK.Echec(L):
                            print("Mat Blanc")
                        else:
                            print("Pat")
                    if turn%2==1 and not(any(unpack([Anyone(L,elmt)for elmt in L if not(elmt.White)]))):
                        if BK.Echec(L):
                            print("Mat Noir")
                        else:
                            print("Pat")
            else:
                select=Indexer(L,x,y)
                if select!=None:
                    if (select.White and turn%2==1) or (not(select.White) and turn%2==0):
                        select=None
            pygame.time.delay(100)
      
        redraw_window(x,y,select,turn)

        pygame.display.update()



if __name__ == "__main__":
    __Game__()


