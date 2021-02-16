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
def redraw_window(x,y,select):
    
    Background()
    DrawPieces()
    Indicator(x,y,select)

    
def Background():
    screen.fill(DARKGREY)
    for i in range(8):
        for j in range(8):
            if (i+j)%2==0:
                pygame.draw.rect(screen,WHITE,(xshift+i*squarelen,j*squarelen,squarelen,squarelen))
            else:
                pygame.draw.rect(screen,BROWN,(xshift+i*squarelen,j*squarelen,squarelen,squarelen))
    

def Indicator(x,y,select):
    if select!=None:
        ShowMovements(select,(255,0,0))
    else:
        ShowMovements(Indexer(L,x,y),DARKGREY)


def DrawPieces():        
    for elmt in L:
        screen.blit(elmt.image,PiecetoPix(*elmt.pos))


def ShowMovements(pointed,color):
    if pointed!=None:
        for elmts in pointed.Allowed(L):
            pygame.draw.circle(screen,color,Center(*elmts),squarelen/8)
        
        for elmts in pointed.Eat(L):
            pygame.draw.circle(screen,(0,0,255),Center(*elmts),squarelen/8)


def SwapPiece(source,destination):
    if destination in source.Allowed(L):
        print("Swaped",source.name,source.pos,"to",destination)
        source.Swap(destination)
    elif source.pos==destination:
        print("got currented")
        return source
    elif destination in source.Eat(L):
        print(source.name,"eat ",Reverse(L,*destination).name)
        L.remove(Reverse(L,*destination))
        source.Swap(destination)
    elif Indexer(L,*PiecetoPix(*destination))!=None:
        print(Indexer(L,*PiecetoPix(*destination)).name)
        return Indexer(L,*PiecetoPix(*destination))
    else:
        print("out of range")
    return None
    
def __Game__():
    
    select=None
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
                select = SwapPiece(select,pointed(x,y))
            else:
                select=Indexer(L,x,y)
            pygame.time.delay(100)
      
        redraw_window(x,y,select)

        pygame.display.update()



if __name__ == "__main__":
    __Game__()


