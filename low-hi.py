import pygame
import random

folder_images = "./images/"

# Card class definition
class Card:
    def __init__(self, value):
        self.value = value


if __name__ == '__main__':

    # Margins
    MARGIN_LEFT = 230
    MARGIN_TOP = 150

    # WINDOW SIZE
    WIDTH = 800
    HEIGHT = 600

    # COLORS
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (110, 110, 110)
    GREEN = (0, 255, 0)
    LIGHT_GREEN = (0, 120, 0)
    RED = (255, 0, 0)
    LIGHT_RED = (120, 0, 0)


    # The type of card
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    # The card value
    cards_values = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10}

    # The deck of cards - List of Objects
    deck = []


    # Loop for every type of card in a suit
    for num in numbers:
        # Adding the card to the deck
        deck.append(Card(num))

    # Initializing PyGame
    pygame.init()

    # Setting up the screen and background
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(GRAY)

    # Setting up caption
    pygame.display.set_caption("The Game")

    # Loading image for the icon
    icon = pygame.image.load(folder_images + 'icon.png')

    # Setting the game icon
    pygame.display.set_icon(icon)

    # Types of fonts to be used
    small_font = pygame.font.Font(None, 32)
    large_font = pygame.font.Font(None, 50)

    # Hign and Low Game Buttons
    high_button = large_font.render("HIGH", True, WHITE)

    # Gets_rectangular covering of text
    high_button_rect = high_button.get_rect()

    # Places the text
    high_button_rect.center = (280, 400)

    low_button = large_font.render("LOW", True, WHITE)
    low_button_rect = low_button.get_rect()
    low_button_rect.center = (520, 400)

    # Load the card image
    prev_card = pygame.image.load(folder_images + r'1.png')

    # Scale the loaded image
    prev_card = pygame.transform.scale(prev_card, (100, 160))

    # Choose the starting card from the deck
    current_card = random.choice(deck)

    # Load the card image
    cur_card = pygame.image.load(folder_images + current_card.value + '.png')

    # Scale the loaded card image
    cur_card = pygame.transform.scale(cur_card, (100, 160))

    # Remove the card from the deck
    deck.remove(current_card)

    # Loading the card image
    next_card = pygame.image.load(folder_images + r'100.png')

    # Scaling the loaded image
    next_card = pygame.transform.scale(next_card, (100, 160))

    # Number of chances left
    chances = 3

    # The current score
    score = 0

    # User's choice initialized
    choice = -1

    # Used to stop game functioning, if True
    over = False

    # The GAME LOOP
    while True:

        # Tracking the mouse movements
        mouse = pygame.mouse.get_pos()

        # Loop events occuring inside the game window
        for event in pygame.event.get():

            # Qutting event
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Left-mouse clicked event
            if not over and event.type == pygame.MOUSEBUTTONDOWN:

                # Clicked on the High Button
                if 220 <= mouse[0] <= 220 + 125 and 370 <= mouse[1] <= 370 + 60:
                    choice = 1

                # Clicked on the Low Button
                if 460 <= mouse[0] <= 460 + 120 and 370 <= mouse[1] <= 370 + 60:
                    choice = 0

                # Finish the game if the deck is finished
                if len(deck) == 1:
                    over = True

                # If a valid choice, the game logic
                if choice != -1:

                    # Change current card to previous
                    previous_card = current_card
                    prev_card = pygame.image.load(
                        folder_images + previous_card.value + '.png')
                    prev_card = pygame.transform.scale(prev_card, (100, 160))

                    # Set up the current card
                    current_card = random.choice(deck)
                    deck.remove(current_card)

                    cur_card = pygame.image.load(folder_images + current_card.value + '.png')
                    cur_card = pygame.transform.scale(cur_card, (100, 160))

                    # Check the result, that is, High or Low
                    if cards_values[current_card.value] > cards_values[previous_card.value]:
                        result = 1
                    elif cards_values[current_card.value] < cards_values[previous_card.value]:
                        result = 0
                    else:
                        result = -1

                        # Manage the game variables
                    if result == -1:
                        continue
                    elif result == choice:
                        score = score + 1
                    else:
                        chances = chances - 1

                        # End the game if chances are finished
                    if chances == 0:
                        over = True

                    # Reset the choice
                    choice = -1

        # Manage the button hovering animation
        if 220 <= mouse[0] <= 220 + 125 and 370 <= mouse[1] <= 370 + 60:
            pygame.draw.rect(screen, LIGHT_GREEN, [220, 370, 125, 60])
        else:
            pygame.draw.rect(screen, GREEN, [220, 370, 125, 60])

        if 460 <= mouse[0] <= 460 + 120 and 370 <= mouse[1] <= 370 + 60:
            pygame.draw.rect(screen, LIGHT_RED, [460, 370, 120, 60])
        else:
            pygame.draw.rect(screen, RED, [460, 370, 120, 60])

            # Displaying scoreboard
        pygame.draw.rect(screen, WHITE, [270, 40, 255, 90])
        score_text = small_font.render("Score = " + str(score), True, BLACK)
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (WIDTH // 2, 70)

        chances_text = small_font.render("Chances = " + str(chances), True, BLACK)
        chances_text_rect = chances_text.get_rect()
        chances_text_rect.center = (WIDTH // 2, 100)

        # Setting up all the buttons, images and texts on the screen
        screen.blit(high_button, high_button_rect)
        screen.blit(low_button, low_button_rect)
        screen.blit(score_text, score_text_rect)
        screen.blit(chances_text, chances_text_rect)
        screen.blit(prev_card, (MARGIN_LEFT, MARGIN_TOP))
        screen.blit(cur_card, (MARGIN_LEFT + 120, MARGIN_TOP))
        screen.blit(next_card, (MARGIN_LEFT + 240, MARGIN_TOP))

        # If the game is finished, display the final score
        if over == True:
            pygame.draw.rect(screen, WHITE, [270, 40, 255, 90])
            score_text = small_font.render("Final Score = " + str(score), True, BLACK)
            score_text_rect = score_text.get_rect()
            score_text_rect.center = (WIDTH // 2, 85)
            screen.blit(score_text, score_text_rect)

        # Update the display after each game loop
        pygame.display.update()