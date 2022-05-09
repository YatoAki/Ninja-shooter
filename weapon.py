import pygame

class Weapon:

    def __init__(self,game,x,y):
        self.x = x
        self.y = y
        self.game = game
        self.character = pygame.image.load('./images/star.png')

    def draw(self):
        self.game.screen.blit(self.character,(self.x,self.y))
        self.y -= 2
