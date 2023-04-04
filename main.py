import pygame
import pygame.freetype
import filesaving
from setting import *
from sprite import *
pygame.init()


def cletlist():
    a = []
    for tymp in range(0, CLETCOUNTY):
        b = []
        for txmp in range(0, CLETCOUNTX):
            c = pygame.Rect((CLETX + CLETVOID) * txmp, (CLETY + CLETVOID) * tymp, CLETX, CLETY)
            b.append(c)
        a.append(b)
    return a
def eat():
    if snakehead.rect.colliderect(tomat.rect):
        snakehead.food += 1
        tomat.setcords(clets)

def cletdraw():
    for tymp in clets:
        for txmp in tymp:
            pygame.draw.rect(window, CLETCOLOR, txmp)


def update():
    snakehead.update()
    tomat.update(clets)
    eat()


def draw():
    cletdraw()
    snakehead.draw(window)
    tomat.draw(window)
    text.render_to(window, (5, 2), F"rec: {PLAYSCORE} score: {snakehead.food}")


def menu():
    mewhil = False
    text = pygame.freetype.Font("kenvector_future_thin.ttf", 32)
    rectbut = pygame.rect.Rect((490, 170), (120, 45))
    butchose = 0
    ytop = 180
    toplist = filesaving.top(FNAME, 3)
    while mewhil is False:
        do = pygame.event.get()
        for temp in do:
            if temp.type == pygame.QUIT:
                return 1
            if temp.type == pygame.KEYDOWN:
                if temp.key == pygame.K_s:
                    rectbut.y = 260
                    butchose = 1
                if temp.key == pygame.K_w:
                    rectbut.y = 170
                    butchose = 0
                if temp.key == pygame.K_RETURN:
                    return butchose
                    
        window.fill(MENUCOLOR)
        text.render_to(window, (130, 80), "EPIC SNAKE")
        text.render_to(window, (100, 120), F"Hello! {PLAYNAME}")
        for temp in toplist:
            text.render_to(window, (100, ytop), F"{temp[1]} - {temp[0]}")
            ytop += 30
        pygame.draw.rect(window, BUTTONCOLOR, rectbut)
        text.render_to(window, (500, 180), "start")
        text.render_to(window, (500, 270), "exit")
        ytop = 180
        pygame.display.update()
        clock.tick(FPS)






window = pygame.display.set_mode((SCREENX, SCREENY))
clock = pygame.time.Clock()
whil = menu()
gamemode = 1
clets = cletlist()
snakehead = Head(CLETX + CLETVOID, clets[7][5].topleft)
tomat = Food(clets[0][0].center)
tomat.setcords(clets)
text = pygame.freetype.Font("kenvector_future_thin.ttf", 12)
while whil != 1:
    do = pygame.event.get()
    for temp in do:
        if temp.type == pygame.QUIT:
            whil = 1
    window.fill(BGCOLOR)
    update()
    draw()
    if snakehead.collidebody() is True:
        whil = menu()
        snakehead.food = 0
        snakehead.body.clear()
    if snakehead.food > PLAYSCORE:
        filesaving.filesave("player_list.txt", PLAYNAME, snakehead.food)
        PLAYSCORE = snakehead.food
    pygame.display.update()
    clock.tick(FPS)