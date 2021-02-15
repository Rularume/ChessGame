from os import path

FPS=60
PYSIZE=11

#Color
DARKGREY=(100,100,100)
BLACK=(0,0,0)
WHITE=(255,255,255)

#Folder
game_folder = path.dirname('.')
assets_folder = path.join(game_folder, 'assets')
pieces_folder = path.join(assets_folder, 'pieces')

""" 0 (1920, 1080)
1 (1680, 1050)
2 (1600, 900)
3 (1440, 900)
4 (1400, 1050)
5 (1366, 768)
6 (1360, 768)
7 (1280, 1024)
8 (1280, 960)
9 (1280, 800)
10 (1280, 768)
11 (1280, 720)
12 (1280, 600)
13 (1152, 864)
14 (1024, 768)
15 (800, 600)
16 (640, 480)
17 (640, 400)
18 (512, 384)
19 (400, 300)
20 (320, 240)
21 (320, 200) """