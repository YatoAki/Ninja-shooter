import pygame
from demon import Demon

class Generator:
    margin = 30
    width = 50
    def __init__(self,game):
        margin = 30
        width = 50
        for x in range(margin,game.width - margin, width):
            for y in range(margin, int(game.height / 2), width):
                game.demons.append(Demon(game, x, y))
