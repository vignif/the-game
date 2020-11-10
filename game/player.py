import pygame
import random

random.seed(1)

WIDTH=600
HEIGHT=600
MARGIN = 60

pygame.init()


screen = pygame.display.set_mode( (WIDTH, HEIGHT ) )
pygame.display.set_caption('The Game')
background = pygame.Color("darkgreen")
screen.fill(background)
myfont = pygame.font.SysFont('Comic Sans MS', 30)


folder = './images/'

class Card:
    """
    Describes Card entity
    - load image from folder if requested
    - store description 
    - identify by number (num)
    """
    
    card_size = (50, 70)

    def __init__(self, num):
        self.num = num
        self.active = False
        self.pos = [0, 0]
        
    def load_graphic(self):
        self.img = pygame.image.load(folder+str(self.num)+".png")
        self.img = pygame.transform.scale(self.img, self.card_size)

    def click(self):
        if not self.active:
            self.active = True
        else:
            self.active = False

    def reset(self):
        self.active = False

    def set_pos(self, pos):
        self.pos = pos
        self.x, self.y = self.pos

    def draw(self, *args):
        self.load_graphic()
        if args:
            self.x, self.y = args
        card = self.img.get_rect().move(self.x, self.y)
        screen.blit(self.img, (self.x, self.y))
        self.rect = card

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def __lt__(self, other):
        return self.num < other.num

    def __str__(self):
        return f'Card {self.num}, active {self.active}'




class Deck:
    """
    Describes the main deck of the game
    - create deck
    - store deck info
    - count cards left in deck
    - no graphic is needed
    """
    def __init__(self, randomize = False):      
        self.maindeck = [Card(num = i) for i in range(2,100)]
        
        if randomize:
            self.shuffle_deck()
        else:
            self.maindeck.sort(reverse=True)
    
    @property
    def is_empty(self):
        return True if len(self) == 0 else False

    def shuffle_deck(self):
        return random.shuffle(self.maindeck)
        
    def draw_card(self):
        if len(self.maindeck) == 0:
            return 0
        else:
            return self.maindeck.pop()

    def __str__(self):
        return str(self.maindeck)

    def __len__(self):
        return len(self.maindeck)


class Hand:
    def __init__(self, deck, num_of_cards = 8):
        self.deck = deck
        self.num = num_of_cards
        self.cards = []
        self.active_card = None
        self.give_cards()
    
    def clicked_on(self, card):        
        [i.click() for i in self.cards if i.active==True]
        card.click()        
        

    def give_cards(self):
        for i in range(self.num):
            self.cards.append(self.deck.draw_card())

    def remove(self, card):
        self.active_card.pos = card.pos
        idx = self.cards.index(card)
        self.cards.pop(idx)

    def insert(self):
        self.cards.append(self.deck.draw_card())  

    def set_positions(self):
        self.cards[0].set_pos([MARGIN, HEIGHT - Card.card_size[1] - 20])
        for i in range(self.num-1):
            self.cards[i+1].set_pos([self.cards[i].x + MARGIN, self.cards[i].y])

    def show(self):
        self.set_positions()
        for card in self.cards:
            card.draw()

    def __str__(self):
        for card in self.cards:
            print( f'{card}')
        return ''


if __name__ == "__main__":
    import time

    deck = Deck(randomize=False)
    hand = Hand(deck, 8)
    hand.show()
    pygame.display.update()
    # pygame.display.flip() # paint screen one time

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for card in hand.cards:
                    if card.collidepoint(x,y):
                        # print(f'clicked on card {card.num}')
                        hand.clicked_on(card)
                        # print(card)
                print(hand)


    
    time.sleep(2)
    print('')
    #loop over, quite pygame
    pygame.quit()
