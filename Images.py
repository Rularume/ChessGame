import pygame
from os import path
from Settings import *
pygame.init()

WINDOWSIZE = pygame.display.list_modes()[PYSIZE]
SHIFT=0.8
size = (int(WINDOWSIZE[0]*SHIFT),int(WINDOWSIZE[1]*SHIFT))
squarelen=int(size[1]/8)
xshift=(size[0]-size[1])/2

a,b=WINDOWSIZE
a,b=int(a*0.8),int(b*0.8)

def load(folderpath,letter,scale):
    normal=pygame.transform.scale(pygame.image.load(path.join(folderpath,letter+'.png')),(squarelen,squarelen))
    scaled=pygame.transform.scale(pygame.image.load(path.join(folderpath,letter+'.png')),scale)
    return [scaled,normal]
piecescale=(int(squarelen*SHIFT),int(squarelen*SHIFT))


logo= load(pieces_folder,'cn',piecescale)[0]

Cb= load(pieces_folder,'cb',piecescale)
Pn= load(pieces_folder,'pn',piecescale)
Pb= load(pieces_folder,'pb',piecescale)


###Archer###

""" PlayerScale = (60,60)
Archersprite = loadJerem(False,hunter_folder,'B',1,PlayerScale,2)[0]
"""
###Skeleton###
"""
SkeletonScale=(64,64)
skeleton_attack = path.join(skeleton_folder, 'sk_attack')

Skeletonsprite=load(False,skeleton_folder,1,SkeletonScale,1)[0]
SkeletonAttack=load(False,skeleton_attack,2,SkeletonScale,36) """