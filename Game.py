import pygame
import sys
from Motherboard import *

pygame.init()

clock = pygame.time.Clock()
pygame.display.set_icon(logo)
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
                pygame.draw.rect(screen,BLACK,(xshift+i*squarelen,j*squarelen,squarelen,squarelen))
    

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
        for elmts in pointed.Movements():
            pygame.draw.circle(screen,color,Center(*elmts),squarelen/8)
    
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
        #print(x,y)

        if mouse[0]:
            select=Indexer(L,x,y)
            pygame.time.delay(100)
      
        redraw_window(x,y,select)

        pygame.display.update()



if __name__ == "__main__":
    __Game__()


