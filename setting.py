import vsmain
import pygame
import filesaving as fs
CLETX = 30
CLETY = 30
CLETCOUNTY = int(vsmain.secivent["clety"])
CLETCOUNTX = int(vsmain.secivent["cletx"])
CLETVOID = 5
SCREENX = (CLETX + CLETVOID) * CLETCOUNTX
SCREENY = (CLETY + CLETVOID) * CLETCOUNTY
SNAKESHAPE = pygame.draw.ellipse if vsmain.secivent["circl"] else pygame.draw.rect
FPS = 60
if vsmain.secivent["color"] == "red":
    SNAKECOLOR = (189, 0, 0)
    BODYCOLOR = (221, 45, 45)
elif vsmain.secivent["color"] == "purple":
    SNAKECOLOR = (157, 3, 163)
    BODYCOLOR = (202, 48, 208)
else:
    SNAKECOLOR = (0, 86, 208)
    BODYCOLOR = (42, 111, 208)
BGCOLOR = (15, 207, 57)
CLETCOLOR = (25, 217, 67)
APPLE = vsmain.secivent["apcolor"]

MENUCOLOR = (211, 227, 30)
BUTTONCOLOR = (181, 197, 0)

PLAYNAME = vsmain.secivent["iname"]
PLAYSCORE = fs.fileread("player_list.txt", PLAYNAME)
FNAME = "player_list.txt"