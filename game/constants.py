import pygame

WIDTH = 600
HEIGHT = 600
MARGIN = 60
folder = './images/'

pygame.init()


screen = pygame.display.set_mode( (WIDTH, HEIGHT ) )
pygame.display.set_caption('The Game')
background = pygame.Color("darkgreen")
screen.fill(background)
myfont = pygame.font.SysFont('Comic Sans MS', 30)
