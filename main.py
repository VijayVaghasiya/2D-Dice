import pygame
from dice import Dice

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((200,250))
    dice = Dice(screen, 30, 30)
    dice.roll()