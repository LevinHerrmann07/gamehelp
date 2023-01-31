import pygame
import random

# Initialize pygame
pygame.init()

# Set the window size
size = (900, 700)
screen = pygame.display.set_mode(size)

# Set the window title
pygame.display.set_caption("Two-Player Game")

# Set the color of the players
red = (255, 0, 0)

# set player2 color
green = (0, 255, 0)

# Set the color of the collectible
blue = (0, 0, 255)

# Set the initial positions for the player squares
player1_x, player1_y = size[0]//2, size[1]//2
player2_x, player2_y = size[0]//2, size[1]//2
item_x, item_y = size[0]//2, size[1]//2

# Set the initial position of the collectible
x, y = random.randint(0, size[0]), random.randint(0, size[1])


# Set the initial scores
player1_score = 0
player2_score = 0
score = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Clear the screen
screen.fill((255, 255, 255))


    # Get player 1's movement
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
        player1_x -= 5
if keys[pygame.K_RIGHT]:
       player1_x += 5
if keys[pygame.K_UP]:
        player1_y -= 5
if keys[pygame.K_DOWN]:
       player1_y += 5

    # Get player 2's movement
if keys[pygame.K_a]:
        player2_x -= 5
if keys[pygame.K_d]:
        player2_x += 5
if keys[pygame.K_w]:
        player2_y -= 5
if keys[pygame.K_s]:
        player2_y += 5
        
if player1_x < item_x + 50 and player1_x + 50 > item_x and player1_y < item_y + 50 and player1_y + 50 > item_y:
    player1_score += 1
    item_x, item_y = random.randint(0, size[0]), random.randint(0, size[1])

if player1_x < 0:
    player1_x = 650
elif player1_x > 650:
    player1_x = 0
if player1_y < 0:
    player1_y = 450
elif player1_y > 450:
    player1_y = 0

if player2_x < 0:
    player2_x = 650
elif player2_x > 650:
    player2_x = 0
if player2_y < 0:
    player2_y = 450
elif player2_y > 450:
    player2_y = 0



    # Check if either player goes out of the screen
if x < 0:
        player1_x = 650
elif x > 650:
        player1_x = 0
if y < 0:
        player1_y = 450
elif y > 450:
        player1_y = 0

if x < 0:
        player2_x = 650
elif x > 650:
        player2_x = 0
if y < 0:
        player2_y = 450
elif y > 450:
        player2_y = 0


    # Draw the player1 square at the new position
pygame.draw.rect(screen, (red), (player1_x, player1_y, 50, 50))


# Draw the player2 square at the new position
pygame.draw.rect(screen, (0, 255, 0), (player2_x, player2_y, 50, 50))
    
    # Draw the collectible at the new position
pygame.draw.rect(screen,(blue), (item_x, item_y, 50, 50))

    
    
    
     # Draw the score
font = pygame.font.Font(None, 30)
text = font.render("Score: " + str(score), True, (255, 255, 255))
screen.blit(text, (10, 10))
    
    
    # Update the display
pygame.display.update()

    # Pause for a moment
pygame.time.delay(10)

# Exit the game
pygame.quit()