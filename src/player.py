
from collections import OrderedDict


class Player:
    def __init__(self, deck, cards, idx):
        self.idx = idx
        self.num_cards = cards
        self.maindeck = deck
        self.hand = []
        self.init_hand()
        self.idx_removed = []
    
    def init_hand(self):
        self.hand = [self.maindeck.draw_card() for _ in range(self.num_cards)]        
        self.hand = sorted(self.hand)
        idx_card = [i for i in range(self.num_cards)] 
        self.hand = dict(zip(idx_card, self.hand)) 

    def play_card(self, idx):
        self.idx_removed.append(idx)
        self.hand.pop(idx)
        self.hand = OrderedDict(sorted(self.hand.items()))

    def fill_hand(self):
        for i in self.idx_removed:
            self.hand[i] = self.maindeck.draw_card()
    
    def __str__(self):
        return f'player {self.idx}'
