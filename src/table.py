import random
from tutorial.scenes import SceneBase

class Deck(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        deck = [i for i in range(2,100)]
        self.maindeck = deck
        self.maindeck.sort(reverse=True)
        # random.shuffle(self.maindeck)
        
    def draw_card(self):
        return self.Update()
    
    @property
    def is_empty(self):
        return True if len(self) == 0 else False

    def shuffle_deck(self):
        random.shuffle(self.maindeck)
        
    def Update(self):
        if len(self.maindeck) == 0:
            return 0
        else:
            return self.maindeck.pop()
    def __str__(self):
        return str(self.maindeck)

    def __len__(self):
        return len(self.maindeck)


class PileDeck(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.maindeck =  [1, 1, 100, 100]
        self.maindeck.sort(reverse=True)
        # random.shuffle(self.maindeck)
        
    def draw_card(self):
        return self.Update()
    
    @property
    def is_empty(self):
        return True if len(self) == 0 else False

    def shuffle_deck(self):
        random.shuffle(self.maindeck)
        
    def Update(self):
        if len(self.maindeck) == 0:
            return 0
        else:
            return self.maindeck.pop()
    def __str__(self):
        return str(self.maindeck)

    def __len__(self):
        return len(self.maindeck)


MARGIN = 80

class DiscardPile(SceneBase):
    def __init__(self, rule):
        SceneBase.__init__(self)
        self.pile = []
        self.rule = rule
        self.img = None
        self.pos = []
        if rule == 'inc':
            self.pile = [1]
            self.num = 1
        elif rule == 'dec':
            self.pile = [100]
            self.num = 100

    def draw(self, piles, screen):
        x, y = piles[0].pos
        card = self.img.get_rect().move(x + MARGIN, y)
        screen.blit(self.img, (x + MARGIN, y))
        pos = [x + MARGIN, y]
        return card


    def ProcessInput(self, events, pressed_keys):
        """
        how to process an input event
        """

    def Update(self, val):
        if self.rule == 'inc':
            if val > self.pile[-1] or val == self.pile[-1] - 10:
                self.pile.append(val)
            else:
                print(f'Accept card = {self.pile[-1]-10} or higher then {self.pile[-1]} \n')
                return False
        elif self.rule == 'dec':
            if val < self.pile[-1] or val == self.pile[-1] + 10:
                self.pile.append(val)
            else:
                print(f'Accept card = {self.pile[-1]+10} or lower then {self.pile[-1]} \n')
                return False
        print(f'insert value {val} in pile')
        return True


    def __str__(self):
        return f'rule: {self.rule}, last card: {self.pile[-1]}'
