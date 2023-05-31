import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Set the size of the screen
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 800
xy_rand=[[100, 250], [300,250], [500,250], [700,250], [900,250], [1100,250], [100,550], [300,500], [500,550], [700,550], [900,550], [1100,550]]
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Match Game")

# Set the font for the cards
font = pygame.font.SysFont("font_file.ttf", 25)
font2 = pygame.font.SysFont("font_file.ttf", 40)

# Set the colors for the cards
colors = [((0,0,0)), (255,182,193), (64,224,208), (255, 255, 0), (0, 255, 255), (255, 0, 255)]

# Define the dictionary with the questions and answers
qa_dict = {"Mapping Type:": "dict", "class Student(Person):": " Inheritance", "Weekday,full version": "Directive %A", "Creates the specified file": "mode : x", "loads a sound": "pygame.mixer", "Represents an image": "pygame.Surface"}

# Create a list of card dictionaries with the surfaces, rectangles, and original positions
cards = []
for i, (question, answer) in enumerate(qa_dict.items()):
    # Create the surface for the question and answer
    question_surface = font.render(question, True, (0, 0, 0))
    answer_surface = font.render(answer, True, (0, 0, 0))

    # Choose a random color for the card
    # Create the surface for the question and answer
    question_surface = font.render(question, True, (0, 0, 0))
    question_width = max(question_surface.get_width(), question_surface.get_height())
    question_bg_surface = pygame.Surface((question_width, question_width))
    question_bg_surface.fill(colors[2])
    question_bg_surface.blit(question_surface, ((question_width-question_surface.get_width())//2, (question_width-question_surface.get_height())//2))

    answer_surface = font.render(answer, True, (0, 0, 0))
    answer_width = max(answer_surface.get_width(), answer_surface.get_height())
    answer_bg_surface = pygame.Surface((answer_width, answer_width))
    answer_bg_surface.fill(colors[1])
    answer_bg_surface.blit(answer_surface, ((answer_width-answer_surface.get_width())//2, (answer_width-answer_surface.get_height())//2))

    # Create the rectangle for the question card
    a=random.choice(xy_rand)
    question_rect = question_bg_surface.get_rect(center=(a[0], a[1]))
    xy_rand.remove(a)
    # Update the width and height of the rectangle to fit the new surface
    question_rect.width = question_bg_surface.get_width()
    question_rect.height = question_bg_surface.get_height()

    # Create the rectangle for the answer card
    a=random.choice(xy_rand)
    answer_rect = answer_bg_surface.get_rect(center=(a[0], a[1]))
    xy_rand.remove(a)
    # Update the width and height of the rectangle to fit the new surface
    answer_rect.width = answer_bg_surface.get_width()
    answer_rect.height = answer_bg_surface.get_height()

    # Append the question and answer cards to the list
    cards.append({"surface": question_bg_surface, "rect": question_rect, "original_pos": question_rect.topleft, "color": colors[1], "text": question})
    cards.append({"surface": answer_bg_surface, "rect": answer_rect, "original_pos": answer_rect.topleft, "color": colors[2], "text": answer})

# Check if the cards are going beyond the screen border and adjust their position
if question_rect.left < 0:
    question_rect.left = 0
elif question_rect.right > SCREEN_WIDTH:
    question_rect.right = SCREEN_WIDTH
if question_rect.top < 0:
    question_rect.top = 0
elif question_rect.bottom > SCREEN_HEIGHT:
    question_rect.bottom = SCREEN_HEIGHT

if answer_rect.left < 0:
    answer_rect.left = 0
elif answer_rect.right > SCREEN_WIDTH:
    answer_rect.right = SCREEN_WIDTH
if answer_rect.top < 0:
    answer_rect.top = 0
elif answer_rect.bottom > SCREEN_HEIGHT:
    answer_rect.bottom = SCREEN_HEIGHT



# Shuffle the cards
random.shuffle(cards)

# Initialize the score and game over variable
score = 0
game_over = False

# Initialize the index of the card being moved
current_card = None
offset = None

# Create the clock object
clock = pygame.time.Clock()

start_ticks = pygame.time.get_ticks()

# Main loop
# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for card in cards:
                if card["rect"].collidepoint(mouse_pos):
                    current_card = card
                    offset = (current_card["rect"].left - mouse_pos[0], current_card["rect"].top - mouse_pos[1])
                    current_card["mouse_pos"] = mouse_pos  # Add mouse_pos to current_card dictionary
                    break
        elif event.type == pygame.MOUSEBUTTONUP:
            if current_card:
                other_card = None
                for card in cards:
                    if (card["rect"] != current_card["rect"] and card["rect"].colliderect(current_card["rect"]))or (card["rect"] != current_card["rect"] and current_card["rect"].colliderect(card["rect"])):
                        other_card = card
                        break

                if (other_card is not None and current_card["text"] in qa_dict and qa_dict[current_card["text"]] == other_card["text"]) or (other_card is not None and card["text"] in list(qa_dict.keys()) and qa_dict[other_card["text"]] == current_card["text"]):
                    cards.remove(current_card)
                    cards.remove(other_card)
                    score += 1
                else:
                    if card["text"] != current_card["text"]:
                        while True:
                            random_pos = (random.randint(0, SCREEN_WIDTH-150), random.randint(0, SCREEN_HEIGHT-150))
                            random_rect = pygame.Rect(random_pos, current_card["rect"].size)
                            if not any(random_rect.colliderect(card["rect"]) for card in cards):
                                    current_card["rect"].topleft = random_pos
                                    break
                    current_card = None
                    offset = None

        elif event.type == pygame.MOUSEMOTION:
            if current_card:
                mouse_pos = pygame.mouse.get_pos()
                current_card["rect"].topleft = (mouse_pos[0] + offset[0], mouse_pos[1] + offset[1])
                if current_card["rect"].left < 0:
                   current_card["rect"].left = 0
                elif current_card["rect"].right > SCREEN_WIDTH:
                   current_card["rect"].right = SCREEN_WIDTH
                if current_card["rect"].top < 0:
                   current_card["rect"].top = 0
                elif current_card["rect"].bottom > SCREEN_HEIGHT:
                   current_card["rect"].bottom = SCREEN_HEIGHT
    
    screen.fill((255, 255, 255))

    for card in cards:
        pygame.draw.rect(screen, card["color"], card["rect"])
        screen.blit(card["surface"], card["rect"])

    score_surface = font.render("Score: {}".format(score), True, (0, 0, 0))
    screen.blit(score_surface, (10, 10))


    time_surface = font.render("Time: " + str(round((pygame.time.get_ticks() - start_ticks) / 1000, 1)), True, (0, 0, 0))

    screen.blit(time_surface, (SCREEN_WIDTH - time_surface.get_width() - 10, 10))

    if len(cards) == 0:
       game_over_surface = font.render("Game Over", True, (255, 0, 0))
       screen.blit(game_over_surface, (SCREEN_WIDTH/2-game_over_surface.get_width()/2, SCREEN_HEIGHT/2-game_over_surface.get_height()/2))
       pygame.display.update()
       game_over = True
    pygame.display.update()
    a=round((pygame.time.get_ticks() - start_ticks) / 1000, 1)
    if len(cards) == 0 or a>=40:
        end_ticks = pygame.time.get_ticks()
        time_taken = (end_ticks - start_ticks) / 1000
        endgame_word=font2.render(f"OVERALL SEMESTER POINTS:  {round(score*6.667+60)}",True,(102,0,0))
        screen.fill((255,222,173))
        screen.blit(endgame_word,(550,300))
        pygame.display.update()
        ended=True
        while ended:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()