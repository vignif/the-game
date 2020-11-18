#!/usr/bin/env python3

from game.game import Game

g = Game()

while g.running:
    g.run()
