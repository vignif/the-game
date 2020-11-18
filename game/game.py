import time
import random
import sys
import pygame
from game.player import Deck, Hand, Piles, logic, copyright
from game.constants import *
sys.path.insert(1, '.')


random.seed(2)

class Game:
    deck = Deck(randomize=False)
    hand = Hand(deck, 8)
    hand.show()

    piles = Piles(deck)
    piles.show()

    copyright()
    clock = pygame.time.Clock()
    pygame.display.update()
    def __init__(self):
        self.running = True

    def run(self):
                
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    for card in self.hand.cards:
                        if card.collidepoint(x,y):
                            # select a card from the hand
                            self.hand.clicked_on(card)

                    for pile in self.piles.cards:
                        if pile.collidepoint(x, y):
                            # select a card from the piles
                            self.piles.clicked_on(pile)
                            if self.hand.active_card:
                                # valid game
                                logic(pile, self.hand, insert=True)
                    # update graphic
                    self.piles.show()
                    self.hand.show()
                    copyright()
                    pygame.display.update()
                    self.clock.tick(60)
                if event.type == pygame.QUIT:
                    self.running = False


        pygame.quit()
