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

Tb= load(pieces_folder,'tb',piecescale)
Cb= load(pieces_folder,'cb',piecescale)
Fb= load(pieces_folder,'fb',piecescale)
Db= load(pieces_folder,'db',piecescale)
Rb= load(pieces_folder,'rb',piecescale)

Pb= load(pieces_folder,'pb',piecescale)

Tn= load(pieces_folder,'tn',piecescale)
Cn= load(pieces_folder,'cn',piecescale)
Fn= load(pieces_folder,'fn',piecescale)
Dn= load(pieces_folder,'dn',piecescale)
Rn= load(pieces_folder,'rn',piecescale)

Pn= load(pieces_folder,'pn',piecescale)


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