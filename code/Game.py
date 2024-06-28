#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame

from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # Check for all events
            # for event in pygame.event.get():
            #    if event.type == pygame.QUIT:
            #        pygame.quit()  # Close Window
            #        quit()  # end pygame

