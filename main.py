#!/usr/bin/env python3

from game.game import Game

g = Game()

while g.running:
    g.init_page()
    g.run()
    g.end_page()