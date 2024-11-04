import pygame
import sys

from RPSGame import RPSGame

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Rock Paper Scissors')

# Initialize clock
clock = pygame.time.Clock()

# Load images
rock_image = pygame.image.load('rock.png')
paper_image = pygame.image.load('paper.png')
scissors_image = pygame.image.load('scissors.png')
winning_image = pygame.image.load('winning.png')
losing_image = pygame.image.load('losing.png')

# Scale images if necessary
rock_image = pygame.transform.scale(rock_image, (150, 150))
paper_image = pygame.transform.scale(paper_image, (150, 150))
scissors_image = pygame.transform.scale(scissors_image, (150, 150))
winning_image = pygame.transform.scale(winning_image, (WIDTH, HEIGHT))
losing_image = pygame.transform.scale(losing_image, (WIDTH, HEIGHT))

# Function to ask for final score
def ask_for_final_score():
    font = pygame.font.Font(None, 36)
    final_score = 0
    input_active = True
    input_text = ""

    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Enter key
                    if input_text.isdigit() and 1 <= int(input_text) <= 5:
                        final_score = int(input_text)
                        input_active = False
                    else:
                        input_text = ""  # Reset if invalid input
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        # Clear the screen
        screen.fill((255, 255, 255))

        # Render text asking for final score
        prompt = font.render("Choose final score (1-5):", True, (0, 0, 0))
        screen.blit(prompt, (20, HEIGHT // 4))

        # Render user input
        score_input = font.render(input_text, True, (0, 0, 0))
        screen.blit(score_input, (20, HEIGHT // 2))

        # Update the display
        pygame.display.flip()
        clock.tick(FPS)

    return final_score

# Initialize the game logic
game = RPSGame()
final_score = ask_for_final_score()

def show_end_screen(image, message):
    """Display the end screen with the given image and message."""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                # Check if clicked on reload or exit buttons
                if reload_button.collidepoint((mouse_x, mouse_y)):
                    return True  # Reload game
                elif exit_button.collidepoint((mouse_x, mouse_y)):
                    pygame.quit()
                    sys.exit()

        screen.blit(image, (0, 0))

        # Render message higher on the screen
        font = pygame.font.Font(None, 48)
        text_surface = font.render(message, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 3))  # Higher position
        screen.blit(text_surface, text_rect)

        # Draw buttons with a border
        pygame.draw.rect(screen, (0, 128, 0), reload_button)  # Reload button
        pygame.draw.rect(screen, (255, 0, 0), exit_button)  # Exit button
        pygame.draw.rect(screen, (0, 0, 0), reload_button, 3)  # Border for reload button
        pygame.draw.rect(screen, (0, 0, 0), exit_button, 3)  # Border for exit button

        # Render button text
        reload_text = font.render("Reload Game", True, (255, 255, 255))
        exit_text = font.render("Exit Game", True, (255, 255, 255))
        screen.blit(reload_text, reload_text.get_rect(center=reload_button.center))
        screen.blit(exit_text, exit_text.get_rect(center=exit_button.center))

        pygame.display.flip()
        clock.tick(FPS)

def main():
    global final_score  # Declare final_score as global
    result = ""
    computer_choice = ""
    player_choice = ""

    global reload_button, exit_button
    reload_button = pygame.Rect(250, 450, 300, 60)  # Increased button size
    exit_button = pygame.Rect(250, 520, 300, 60)  # Increased button size with space

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if rock_image.get_rect(topleft=(50, 450)).collidepoint((mouse_x, mouse_y)):
                    player_choice = 'rock'
                    result, computer_choice = game.play_round(player_choice)
                elif paper_image.get_rect(topleft=(275, 450)).collidepoint((mouse_x, mouse_y)):
                    player_choice = 'paper'
                    result, computer_choice = game.play_round(player_choice)
                elif scissors_image.get_rect(topleft=(500, 450)).collidepoint((mouse_x, mouse_y)):
                    player_choice = 'scissors'
                    result, computer_choice = game.play_round(player_choice)

        # Clear the screen
        screen.fill((255, 255, 255))

        # Display images
        screen.blit(rock_image, (50, 450))
        screen.blit(paper_image, (275, 450))
        screen.blit(scissors_image, (500, 450))

        # Display scores
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Your Score: {game.user_score} | Computer Score: {game.computer_score}", True, (0, 0, 0))
        screen.blit(score_text, (20, 20))

        # Display results
        if player_choice and computer_choice:
            player_image = rock_image if player_choice == 'rock' else paper_image if player_choice == 'paper' else scissors_image
            computer_image = rock_image if computer_choice == 'rock' else paper_image if computer_choice == 'paper' else scissors_image

            # Show player and computer choices
            screen.blit(player_image, (50, 200))
            screen.blit(computer_image, (500, 200))

            # Labels for choices
            player_label = font.render("Your Choice", True, (0, 0, 0))
            computer_label = font.render("Computer's Choice", True, (0, 0, 0))
            screen.blit(player_label, (50, 175))
            screen.blit(computer_label, (500, 175))

            # Result text positioned higher
            result_text = font.render(f"{result}", True, (0, 0, 0))
            screen.blit(result_text, (WIDTH // 2 - font.size(result)[0] // 2, 130))  # Adjusted position

        # Check for win condition
        if game.user_score >= final_score:
            show_end_screen(winning_image, "Congratulations!")
            game.reset_scores()
            final_score = ask_for_final_score()

        elif game.computer_score >= final_score:
            show_end_screen(losing_image, "Unlucky, Try Again")
            game.reset_scores()
            final_score = ask_for_final_score()

        # Update the display
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
