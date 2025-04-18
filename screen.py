import pygame
import sys
import gomoku_logic as gomoku
import time


# Initialize Pygame
pygame.init()

# Set up the display
width, height = 600, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Go Chess Board")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 128)
line_color = (0, 0, 0)
invalid_color = (255, 0, 0)  # Define invalid_color

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('GeeksForGeeks', True, green, blue)
textRect = text.get_rect()

# Set up the board
board_size = 19
fixed_board_size = 600
top_left_x = 20
top_left_y = 20
cell_size = fixed_board_size // board_size

# Set up the radius for the circles
circle_radius = 10

# Create an empty list to store the placed circles
placed_circles = []

# Create a 2-dimensional list to represent the board
board = [[" " for _ in range(board_size)] for _ in range(board_size)]

# Variable to keep track of the current player's turn (1 for black, -1 for white)
current_player = 1

# Flag to indicate whether the color selection menu is active
color_selection = True

# Flag to indicate whether it's an invalid move
invalid_move = False

# Colors for menu buttons
button_color = (100, 100, 100)
button_hover_color = (150, 150, 150)

# Player color choices
player_colors = {
    1: black,
    -1: white, 
    0: "6"
}
player_number = 1

# Clock to control the frame rate
clock = pygame.time.Clock()

game_end = False
calculating = False
player_color = 1

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check for mouse click events
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and not game_end:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if not calculating:
                # Check if the click is within the board area
                if top_left_x - 5 <= mouse_x <= top_left_x + fixed_board_size - cell_size + 5 and \
                        top_left_y - 5 <= mouse_y <= top_left_y + fixed_board_size - cell_size + 5:

                    # Calculate the grid position of the click
                    x = (mouse_x - top_left_x) / cell_size
                    grid_x = int(abs(x)) if x % 1 < 0.5 else int(abs(x) + 1)
                    y = (mouse_y - top_left_y) / cell_size
                    grid_y = int(abs(y)) if y % 1 < 0.5 else int(abs(y) + 1)

                    # Check if the position is unplayed
                    if board[grid_y][grid_x] == " ":
                        # Update the board with the current player's stone
                        board[grid_y][grid_x] = "b" if current_player == 1 else "w"

                        # Calculate the exact position to place the circle at the intersection
                        circle_x = top_left_x + grid_x * cell_size
                        circle_y = top_left_y + grid_y * cell_size

                        # Add the circle position to the list with the appropriate color
                        placed_circles.append((circle_x, circle_y, player_color))

                        # Switch the player's turn
                        current_player *= -1

                        # Reset the invalid move flag
                        invalid_move = False

    # Fill the screen with a white color
    screen.fill(white)


    
    # Draw horizontal lines
    for i in range(board_size):
        pygame.draw.line(screen, line_color, (top_left_x, top_left_y + i * cell_size),
                             (top_left_x + fixed_board_size - cell_size - 10, top_left_y + i * cell_size), 1)

    # Draw vertical lines
    for i in range(board_size):
        pygame.draw.line(screen, line_color, (top_left_x + i * cell_size, top_left_y),
                             (top_left_x + i * cell_size, top_left_y + fixed_board_size - cell_size - 10), 1)

        # Draw placed circles with border for white stones
    for circle_pos in placed_circles:
        pygame.draw.circle(screen, circle_pos[2], circle_pos[:2], circle_radius)

            # Add a black border to white circles
        if circle_pos[2] == white:
            pygame.draw.circle(screen, black, circle_pos[:2], circle_radius, 2)

        if circle_pos == placed_circles[-1]:
            pygame.draw.circle(screen, green, circle_pos[:2], 5, 2)
    
    
    calculating = False

    # Display invalid move indicator
    if invalid_move:
        font = pygame.font.Font(None, 36)
        text_invalid = font.render("Invalid Move", True, invalid_color)
        screen.blit(text_invalid, (width // 2 - text_invalid.get_width() // 2,
                                   height // 2 - text_invalid.get_height() // 2))
        

    if gomoku.check_winner(board, "b"):
        game_end = True
        screen.blit(font.render('Black Won', False, green, blue), (0, 600))
        

    if gomoku.check_winner(board, "w"):
        game_end = True
        screen.blit(font.render('White Won', True, green, blue), (0, 600))


    # Update the display
    pygame.display.flip()

    if current_player != player_number and player_number != 0 and not game_end:
            calculating = True
            dct = {
                1: "b",
                -1: "w"
            }
            grid_y, grid_x = gomoku.get_move(board, dct[current_player])
            board[grid_y][grid_x] = "b" if current_player == 1 else "w"

            # Calculate the exact position to place the circle at the intersection
            circle_x = top_left_x + grid_x * cell_size
            circle_y = top_left_y + grid_y * cell_size

            # Add the circle position to the list with the appropriate color
            placed_circles.append((circle_x, circle_y, player_colors[current_player]))

            # Switch the player's turn
            current_player *= -1

    
    if game_end:
        color_selection = True
        placed_circles.clear()
        board = [[" " for _ in range(board_size)] for _ in range(board_size)]
        player_number = 1
        current_player = 1
        time.sleep(3)
        game_end = False


    # Cap the frame rate
    clock.tick(60)
