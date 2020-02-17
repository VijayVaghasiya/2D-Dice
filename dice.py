"""
Project Name : Roll the Dice
Developed as hobby project by @pyLancing
"""

import pygame
import os
import random

class Dice(object):

    def __init__(self, screen, x , y):
        self.x = x
        self.y = y
        self.number = 0
        self.roll_decision = False
        self.dice_images = []
        self.screen = screen

        for i in range(1,7):
            self.dice_images.append(pygame.image.load(os.path.join("dice_images/", str(i) + ".png")))

        # Button Positions
        self.button_x = self.x + self.dice_images[0].get_width()/2 - 40
        self.button_y = self.y + self.dice_images[0].get_height() + 20


    def rotating_illusion(self):
        """
        Create illusion that dice is rolling.
        :return : none
        """
        self.roll_decision = True

        if self.roll_decision:
            num_of_rotation = 20
            while num_of_rotation != 0:
                pygame.time.wait(30)
                self.number = random.randint(0,5)
                num_of_rotation -= 1
                self.draw()
        
        self.roll_decision = False

    def draw(self):
        """
        Draw all the images on the screen. 
        :return : None
        """
        self.screen.fill((255,255,255))
        self.screen.blit(self.dice_images[self.number], (self.x, self.y))

        # Draw Button and create hovering effect
        roll_text = pygame.font.Font('freesansbold.ttf', 20)
        if self.hovered:
            pygame.draw.rect(self.screen, (0,0,200),(self.button_x, self.button_y, 80, 40))
        else:
            pygame.draw.rect(self.screen, (0,0,0),(self.button_x, self.button_y, 80, 40))

        self.screen.blit(roll_text.render("ROLL", True, (255,255,255)),(self.button_x + 15, self.button_y + 10))

        pygame.display.update()


    def roll(self):
        running = True

        # main Game Loop
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # dice rolling method 1 : presss space
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # Roll dice whenever space key is pressed
                        self.rotating_illusion()

                # dice rolling method 2 : click button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if (self.button_x <= x <= self.button_x + 80) and (self.button_y <= y <= self.button_y + 40):
                        self.rotating_illusion()

            # Enable/Disable mouse hovering effect
            x, y = pygame.mouse.get_pos()
            if self.button_x <= x <= self.button_x + 80 and self.button_y <= y <= self.button_y + 40:
                self.hovered = True
            else:
                self.hovered = False

            self.draw()

    pygame.quit()