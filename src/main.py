"""
The Game 
"""

import random
import logging as log
from table import Deck, DiscardPile
from player import Player
random.seed(1)


class Game:
    def __init__(self, players):
        self.num_players = players
        self.Players = None
        self.deck = Deck()
        print(f'The deck initially has {len(self.deck)} cards')
        self.pile1 = DiscardPile('inc')
        self.pile2 = DiscardPile('inc')
        self.pile3 = DiscardPile('dec')
        self.pile4 = DiscardPile('dec')
        self.Piles=[self.pile1, self.pile2, self.pile3, self.pile4]
        idx_pile = [i for i in range(len(self.Piles))]
        self.Piles_dict = dict(zip(idx_pile, self.Piles)) 
        self.give_init_cards()
            
    def give_init_cards(self):
        if self.num_players == 2:
            self.cards_in_hand = 7
            self.Players = [Player(self.deck, cards = self.cards_in_hand, idx = i) for i in range(self.num_players)]            
        elif self.num_players == 3:
            self.cards_in_hand = 5
            self.Players = [Player(self.deck, cards = self.cards_in_hand, idx = i) for i in range(self.num_players)]
        else:
            log.error("Invalid number of players")

    def show_table(self):
        for p in self.Piles:
            print(p)

    def run(self):
        idx_player = 0
        print(f'Starts player {self.Players[idx_player]}')
        while len(self.deck) > 0:
            print(f'{len(self.deck)} cards still in deck')
            player = self.Players[idx_player]
            valid_play = False
            if not valid_play:
                print('\n\n_________\n')
                print(f'Play player {player.idx}')
                print(f'hand {player.hand}')
                self.show_table()
                idx_card = int(input('which card you want to play? select as 0-index start \n'))
                selected_card = player.hand[idx_card]
                print(f'selected card: {selected_card}')
                idx_pile = int(input('on which pile you want to play it? select as 0-index start \n'))
                selected_pile = self.Piles_dict[idx_pile]
                print(f'selected pile: {selected_pile}')
                valid_play = selected_pile.insert(selected_card)
                if valid_play:
                    player.play_card(idx_card)
                else:
                    continue
                print(player.hand)
                new_card = int(input('want to play another card? 0- yes; 1- no;\n'))
                if new_card == 0:
                    valid_play = False 
                if new_card == 1:
                    valid_play = True

                if valid_play:
                    player.fill_hand()
                    idx_player += 1
                    idx_player = idx_player%len(self.Players)

        if len(self.deck) == 0:
            print(f'Congratulations! you finished the deck, you won The Game!\n')



if __name__ == "__main__":
    # players = int(input('select number of players: \n'))
    players = 2
    game = Game(players)
    game.run()