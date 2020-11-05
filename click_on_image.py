import pygame
from pygame.locals import *
from pygame.color import THECOLORS as color
import random

class Deck():
    def __init__(self):
        deck = [i for i in range(2,100)]
        self.maindeck = deck 
        random.shuffle(self.maindeck)
        
    def draw_card(self):
        if len(self.maindeck) == 0:
            return 0
        else:
            return self.maindeck.pop()
        
    def shuffle_deck(self):
        random.shuffle(self.maindeck)
        
    def __str__(self):
        return str(self.maindeck)

    def __len__(self):
        return len(self.maindeck)


deck = Deck()
random.seed(1)

pygame.init()
WIDTH=500
HEIGHT=600
MARGINS = 120

card_size = (50, 70)

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
        self.card = self.draw(self.x, self.y)

    def draw(self, x, y):
        card = self.img.get_rect().move(x, y)
        screen.blit(self.img, (x, y))
        return card

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def show_cards():
    c8 = Card((WIDTH*(8/9),HEIGHT-MARGINS), 34)
    c7 = Card((WIDTH*(7/9),HEIGHT-MARGINS), 81)
    c6 = Card((WIDTH*(6/9),HEIGHT-MARGINS), 23)
    c5 = Card((WIDTH*(5/9),HEIGHT-MARGINS), 2)
    c4 = Card((WIDTH*(4/9),HEIGHT-MARGINS), 99)
    c3 = Card((WIDTH*(3/9),HEIGHT-MARGINS), 19)
    c2 = Card((WIDTH*(2/9),HEIGHT-MARGINS), 15)
    c1 = Card((WIDTH*(1/9),HEIGHT-MARGINS), 45)

    cards = [c1, c2, c3, c4, c5, c6, c7, c8]

    p1 = Card((WIDTH*(4/5),MARGINS/2), 1)
    p2 = Card((WIDTH*(3/5),MARGINS/2), 1)
    p3 = Card((WIDTH*(2/5),MARGINS/2), 100)
    p4 = Card((WIDTH*(1/5),MARGINS/2), 100)
    piles = [p1, p2, p3, p4]
    return cards, piles


cards, piles = show_cards()
pygame.display.update()
pygame.display.flip() # paint screen one time

running = True
card_selected = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y positions of the mouse click
            x, y = event.pos
            for card in cards:
                if card.card.collidepoint(x, y):
                    card_selected = card
                    screen.fill(background)
                    cards, piles = show_cards()
                    draw_text(f'clicked on card {card.num}', myfont, (255, 255, 255), screen, 20, HEIGHT * 0.6) 
                    deck.draw_card()  
                    print(f'clicked on card {card.num}')
                    break

            for pile in piles:
                if pile.card.collidepoint(x,y) and card_selected.num:
                    screen.fill(background)
                    cards, piles = show_cards()
                    card_selected.draw(pile.x, pile.y+pile.height + 10)
                    draw_text(f'clicked on pile {pile.num}, selected card {card_selected.num}', myfont, (255, 255, 255), screen, 20, HEIGHT * 0.6)
                    print(f'clicked on pile {pile.num}')
                    card_selected = False

            
            draw_text(f'cards in deck {len(deck)}', myfont, (255, 255, 255), screen, 20, HEIGHT/2)
            
            pygame.display.update()


            
#loop over, quite pygame
pygame.quit()