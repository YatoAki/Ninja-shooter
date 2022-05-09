import pygame, sys
from ninja import Ninja
from weapon import Weapon
from generator import Generator

class Game:
    screen = None
    weapons = []
    demons = []
    lost = False

    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width,height))
        self.clock = pygame.time.Clock()
        done = False

        ninja = Ninja(self,width/2, height - 30)
        generator = Generator(self)
        background = pygame.image.load("./images/back.jpg")
        background = pygame.transform.scale(background,(self.width,self.height))

        while not done:
            self.screen.blit(background,(0,0))
            if len(self.demons) == 0:
                self.displayText("VICTORY ACHIEVED")

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:  # sipka doleva
                ninja.x -= 2 if ninja.x > 20 else 0  # leva hranice plochy
            elif pressed[pygame.K_RIGHT]:  # sipka dopravac
                ninja.x += 2 if ninja.x < width - 20 else 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.weapons.append(Weapon(self, ninja.x, ninja.y))

            if not self.lost: ninja.draw()
            for demon in self.demons:
                demon.draw()
                demon.checkCollision(self)
                if (demon.y > height):
                    self.lost = True
                    self.displayText("YOU DIED")
            for weapon in self.weapons:
                weapon.draw()
                if weapon.y < 0:
                    self.weapons.remove(weapon)
            pygame.display.update()
            self.clock.tick(60)

    def displayText(self,text):
        pygame.font.init()
        font = pygame.font.SysFont('Arial',50)
        textsurface = font.render(text, False, (44, 0, 62))
        self.screen.blit(textsurface, (110, 160))


if __name__ == '__main__':
    game = Game(600,400)
