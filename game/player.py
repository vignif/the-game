import pygame
import random


class Card:
    """
    Describes Card entity
    - load image from folder if requested
    - store description 
    - identify by number (num)
    """
    
    card_size = (50, 70)

    def __init__(self, num: int):
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

    def __repr__(self):
        return '{0}'.format(self.num)



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
        self.first_pos = [MARGIN, HEIGHT - Card.card_size[1] - 20]
    
    def clicked_on(self, card):        
        [i.click() for i in self.cards if i.active==True]
        card.click()
        self.active_card = [i for i in self.cards if i.active == True][0]     
        
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
        self.cards[0].set_pos(self.first_pos)
        for i in range(self.num-1):
            self.cards[i+1].set_pos([self.cards[i].x + MARGIN, self.cards[i].y])

    def show(self):
        self.set_positions()
        for card in self.cards:
            card.draw()
    
    def replace(self):
        idx = self.cards.index(self.active_card)
        old_pos = self.cards[idx].pos
        self.cards[idx] = self.deck.draw_card()
        self.cards[idx].set_pos(old_pos)
        return self

    def __str__(self):
        for card in self.cards:
            print( f'{card}')
        return ''


class Pile(Card):
    def __init__(self, rule: str):
        self.active = False
        if rule == 'inc':
            self.num = 1
        elif rule == 'dec':
            self.num = 100
        else:
            print(f'Error')

        self.rule = rule
        self.cards = []
        self.value = self.num

    def insert(self, card):
        self.cards.append(card)
        self.value = card.num

    def draw(self):
        Card.draw(self)
        if self.cards:
            self.cards[-1].set_pos([self.x, self.y + Card.card_size[1] + 20])
            self.cards[-1].draw()

    def __str__(self):
        return f'Pile {self.num} contains {self.cards}'


class Piles(Hand):
    def __init__(self, deck):
        rules = ['inc','inc','dec','dec']
        self.num = len(rules)
        self.deck = deck
        self.cards = []
        for rule in rules:
            self.cards.append(Pile(rule))
        self.first_pos = [MARGIN, 20]


def check_pile_1(pile, card_hand):
    if card_hand.num > pile.value or card_hand.num == pile.value - 10:
        return True
    else:
        return False


def check_pile_100(pile, card_hand):
    if card_hand.num < pile.value or card_hand.num == pile.value + 10:
        return True
    else:
        return False


def check_available_moves(piles, hand):
    pass


def logic(pile, hand_card, insert: bool):
    valid = False
    if pile.num == 1:
        # logic for pile 1
        if check_pile_1(pile, hand_card):
            if insert == True:
                pile.insert(hand_card)   
            valid = True
    elif pile.num == 100:
        # logic for pile 100
        if check_pile_100(pile, hand_card):
            if insert == True:
                pile.insert(hand_card)  
            valid = True    
        
    # insert card in choosen pile
    # draw from the deck a new card in the hand
    if valid:
        hand.replace()
    return pile, hand


if __name__ == "__main__":
    import time
    import random
    import sys
    sys.path.insert(1, '.')
    folder = './images/'


    random.seed(2)

    WIDTH=600
    HEIGHT=600
    MARGIN = 60

    pygame.init()


    screen = pygame.display.set_mode( (WIDTH, HEIGHT ) )
    pygame.display.set_caption('The Game')
    background = pygame.Color("darkgreen")
    screen.fill(background)
    myfont = pygame.font.SysFont('Comic Sans MS', 30)


    deck = Deck(randomize=False)
    hand = Hand(deck, 8)
    hand.show()

    piles = Piles(deck)
    piles.show()

    clock = pygame.time.Clock()
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for card in hand.cards:
                    if card.collidepoint(x,y):
                        # select a card from the hand
                        hand.clicked_on(card)

                for pile in piles.cards:
                    if pile.collidepoint(x, y):
                        # select a card from the piles
                        piles.clicked_on(pile)
                        if hand.active_card:
                            # valid game
                            logic(pile, hand.active_card, insert=True)
                # print(piles)
                # update graphic
                print('')
                piles.show()
                hand.show()
                pygame.display.update()
                clock.tick(60)


    pygame.quit()
