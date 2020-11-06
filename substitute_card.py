import pygame
from pygame.locals import *
from pygame.color import THECOLORS as color
import random
from src.table import Deck, DiscardPile


deck = Deck()
random.seed(1)

pygame.init()
WIDTH=500
HEIGHT=600
MARGINS = 120

card_size = (100, 150)

screen = pygame.display.set_mode( (WIDTH, HEIGHT ) )
pygame.display.set_caption('The Game')
background = pygame.Color("darkgreen")
screen.fill(background)
myfont = pygame.font.SysFont('Comic Sans MS', 30)


folder = './images/'
class Card(Deck):
    def __init__(self, pos: [], num: int):
        self.x, self.y = pos
        self.pos = pos
        self.num = num
        self.img = pygame.image.load(folder+str(num)+".png")
        self.img = pygame.transform.scale(self.img, card_size)
        self.height = card_size[1]
        self.width = card_size[0]
        self.card = self.draw()

    def draw(self, *args):
        if args:
            self.x, self.y = args
        card = self.img.get_rect().move(self.x, self.y)
        screen.blit(self.img, (self.x, self.y))
        return card
    
    def remove(self):
        self.img = None


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def init_cards():
    c1 = Card((WIDTH/2,HEIGHT/2), deck.draw_card())
    c2 = Card((WIDTH/2+ 110,HEIGHT/2), deck.draw_card())
    c3 = Card((WIDTH/2- 110,HEIGHT/2), deck.draw_card())

    cards = [c1, c2, c3]

    return cards

cards = init_cards()
pygame.display.update()
pygame.display.flip() # paint screen one time

running = True
card_selected = False
valid_play = False

while running:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        for card in cards:
            if card.card.collidepoint(mouse):
                #mouse hovering card
                pass            
            else:
                #mouse not hovering card
                pass
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill(background)
            # Set the x, y positions of the mouse click
            x, y = event.pos
            for card in cards:
                if card.card.collidepoint(x, y):
                    card_selected = card
                    pos_old = card.pos
                    draw_text(f'clicked on card {card.num}', myfont, (255, 255, 255), screen, 20, HEIGHT * 0.2)
                    idx = cards.index(card)
                    print(f'clicked on card {card.num} at index {idx}')
                    valid_play = True
                    break

            if valid_play:
                card_selected.remove()
                cards.pop(idx)
                cards.append(Card(pos_old, deck.draw_card()))  
            
            # render
            
            draw_text(f'cards in deck {len(deck)}', myfont, (255, 255, 255), screen, 20, HEIGHT*0.4)
            [card.draw() for card in cards]
            valid_play = False
            pygame.display.update()


            
#loop over, quite pygame
pygame.quit()