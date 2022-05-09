import pygame

class Demon:

    def __init__(self,game,x,y):
        self.x = x
        self.game = game
        self.y = y
        self.size = 24
        self.character = pygame.image.load('./images/oni.png')

    def draw(self):
        self.game.screen.blit(self.character,(self.x,self.y))
        self.y += 0.05

    def checkCollision(self,game):
        for weapon in game.weapons:
            if (weapon.x < self.x + self.size and
                    weapon.x > self.x - self.size and
                    weapon.y < self.y + self.size and
                    weapon.y > self.y - self.size):
                game.weapons.remove(weapon)
                game.demons.remove(self)
