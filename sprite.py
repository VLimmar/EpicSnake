import pygame
import random
from setting import *
class Head:
    def __init__(self, speed, spawn) -> None:
        self.speedx = speed
        self.speedy = 0
        self.speed = speed
        self.spawn = spawn
        self.food = 0
        self.body = []
        self.rect = pygame.rect.Rect(spawn, (CLETX, CLETY))
        self.tick = 0
    def draw(self, face):
        for temp in self.body:
            temp.draw(face)
        SNAKESHAPE(face, SNAKECOLOR, self.rect)
    def update(self):
        wond = pygame.key.get_pressed()
        if wond[pygame.K_s] is True and self.speedy != -self.speed:
            self.speedx = 0 
            self.speedy = self.speed
        if wond[pygame.K_w] is True and self.speedy != self.speed:
            self.speedx = 0
            self.speedy = -(self.speed)
        if wond[pygame.K_d] is True and self.speedx != -self.speed:
            self.speedx = self.speed
            self.speedy = 0
        if wond[pygame.K_a] is True and self.speedx != self.speed:
            self.speedy = 0
            self.speedx = -(self.speed)
        time = pygame.time.get_ticks()
        self.collidewall()
        if time - self.tick >= 300:
            self.bodyplus()
            self.bodyminus()
            self.rect.centerx += self.speedx
            self.rect.centery += self.speedy
            self.tick = time

    def collidewall(self):
        if self.rect.centerx >= SCREENX:
            self.rect.left = 0
        elif self.rect.centerx <= 0:
            self.rect.right = SCREENX - CLETVOID
        elif self.rect.centery >= SCREENY:
            self.rect.top = 0
        elif self.rect.centery <= 0:
            self.rect.bottom = SCREENY - CLETVOID
    def collidebody(self):
        for temp in range(1, len(self.body)):
            if self.rect.colliderect(self.body[temp].rect):
                return True
    def bodyplus(self):
        tail = Body(self.rect.topleft)
        self.body.append(tail)

    def bodyminus(self):
        if len(self.body) > self.food:
            self.body.pop(0)

class Body():
    def __init__(self, spawn) -> None:
        self.spawn = spawn
        self.rect = pygame.rect.Rect(spawn, (CLETX, CLETY))
    def draw(self, face):
        SNAKESHAPE(face, BODYCOLOR, self.rect)
    
class Food():
    def __init__(self,spawn) -> None:
        self.spawn = spawn
        self.rect = pygame.rect.Rect(spawn, (CLETX / 2, CLETY / 2))
        self.lastick = 0
    def draw(self, face):
        pygame.draw.rect(face, APPLE, self.rect)
    def update(self, listik):
        time = pygame.time.get_ticks()
        if time - self.lastick >= 12345:
            self.setcords(listik)
            self.lastick = time
    def setcords(self, clets):
        self.rect.center = clets[random.randint(0, CLETCOUNTY - 1)][random.randint(0, CLETCOUNTX - 1)].center
        