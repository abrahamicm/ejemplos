import pygame

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the cell size
CELL_SIZE = 100

# Initialize Pygame
pygame.init()

# Create the window
screen = pygame.display.set_mode((CELL_SIZE * 3, CELL_SIZE * 3))

# Initialize the game board
board = [[None for _ in range(3)] for _ in range(3)]

# Initialize the turn
turn = "X"

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            # Get the row and column of the clicked cell
            column = event.pos[0] // CELL_SIZE
            row = event.pos[1] // CELL_SIZE
            # Check if the cell is empty
            if board[row][column] is None:
                # Fill the cell with the current player's symbol
                board[row][column] = turn
                # Switch the turn
                if turn == "X":
                    turn = "O"
                else:
                    turn = "X"
    # Clear the screen
    screen.fill(WHITE)
    # Draw the grid
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (CELL_SIZE * 3, i * CELL_SIZE), 5)
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, CELL_SIZE * 3), 5)
    # Draw the symbols
    for row in range(3):
        for column in range(3):
            if board[row][column] is not None:
                symbol = board[row][column]
                font = pygame.font.Font(None, CELL_SIZE)
                text = font.render(symbol, True, BLACK)
                text_rect = text.get_rect()
                text_rect.center = (column * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2)
                screen.blit(text, text_rect)
    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
