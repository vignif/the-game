import time
import random
import sys
import pygame
from game.player import Deck, Hand, Piles, logic, copyright, cards_in_deck, check_available_moves
from game.constants import *
sys.path.insert(1, '.')



class Game:
    deck = Deck(randomize=True)
    hand = Hand(deck, 8)
    piles = Piles(deck)

    copyright()
    clock = pygame.time.Clock()
    pygame.display.update()
    moves = len(hand.cards) * len(piles.cards)

    def __init__(self):
        self.win = False
        self.run_main = True
        self.running = True
        self.start = True

    def init_page(self):
        if self.start:
            textsurface = title.render("Press Enter to start the game", True, (255, 255, 255))
            screen.blit(textsurface,(40,HEIGHT/2))
            pygame.display.update()
            self.start = False        

        for event in pygame.event.get():
            if event.type == pygame.K_RETURN:
                return
    
    def in_game(self):
        if self.moves == 0 and len(self.deck) > 0:
            self.win = False
            self.run_main = False

        elif self.moves == 0 and len(self.deck) == 0:
            self.win = True
            self.run_main = False

    def end_page(self):
        screen.fill(background)
        if self.win:
            textsurface1 = title.render("You Won!!", True, (255, 255, 255))
        else:
            textsurface1 = title.render("You Lost!!", True, (255, 255, 255))
            textsurfacePoints = title.render("With points {0}".format(len(self.deck)), True, (255, 255, 255))
            screen.blit(textsurfacePoints,(20,HEIGHT/2 + 40))

        screen.blit(textsurface1,(40,HEIGHT/2))
        pygame.display.update()
        self.clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


 

    def run(self):
        self.piles.show()
        self.hand.show()
        while self.run_main:
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

                    self.in_game()
                    # update graphic
                    screen.fill(background)
                    cards_in_deck(self.deck)
                    self.piles.show()
                    self.hand.show()
                    copyright()
                    self.moves = check_available_moves(self.piles, self.hand)
                    pygame.display.update()
                    self.clock.tick(60)
                if event.type == pygame.QUIT:
                    self.running = False
