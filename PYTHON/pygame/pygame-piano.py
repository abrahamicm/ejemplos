import pygame

# Define the black and white keys
WHITE_KEY_WIDTH = 50
WHITE_KEY_HEIGHT = 200
BLACK_KEY_WIDTH = 30
BLACK_KEY_HEIGHT = 120

# Initialize Pygame
pygame.init()

# Create the window
screen = pygame.display.set_mode((WHITE_KEY_WIDTH * 7, WHITE_KEY_HEIGHT))

# Create the white keys
white_keys = []
for i in range(7):
    white_key = pygame.Surface((WHITE_KEY_WIDTH, WHITE_KEY_HEIGHT))
    white_key.fill((240, 240, 240))
    white_keys.append(white_key)

# Create the black keys
black_keys = []
black_keys.append(pygame.Surface((BLACK_KEY_WIDTH, BLACK_KEY_HEIGHT)))
black_keys[-1].fill((0, 0, 0))
black_keys.append(pygame.Surface((BLACK_KEY_WIDTH, BLACK_KEY_HEIGHT)))
black_keys[-1].fill((0, 0, 0))
black_keys.append(pygame.Surface((BLACK_KEY_WIDTH, BLACK_KEY_HEIGHT)))
black_keys[-1].fill((0, 0, 0))

# Draw the keys
x = 0
for i, white_key in enumerate(white_keys):
    screen.blit(white_key, (x, 0))
    x += WHITE_KEY_WIDTH
    if i in [1, 3, 6]:
        screen.blit(black_keys[0], (x - BLACK_KEY_WIDTH / 2, 0))
    if i == 4:
        screen.blit(black_keys[1], (x - BLACK_KEY_WIDTH / 2, 0))
    if i == 11:
        screen.blit(black_keys[2], (x - BLACK_KEY_WIDTH / 2, 0))

# Update the display
pygame.display.update()

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
