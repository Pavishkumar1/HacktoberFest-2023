import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Treasure Island Adventure")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Load assets (You need to provide your own images)
player_image = pygame.image.load('player.png')  # Replace with your player image
treasure_image = pygame.image.load('treasure.png')  # Replace with your treasure image
bg_image = pygame.image.load('background.jpg')  # Replace with your background image

# Game variables
player_pos = [WIDTH // 2, HEIGHT // 2]
treasure_pos = [random.randint(0, WIDTH - 50), random.randint(0, HEIGHT - 50)]
level = 1
score = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5
    if keys[pygame.K_UP]:
        player_pos[1] -= 5
    if keys[pygame.K_DOWN]:
        player_pos[1] += 5

    # Check for treasure collection
    player_rect = pygame.Rect(player_pos[0], player_pos[1], 50, 50)
    treasure_rect = pygame.Rect(treasure_pos[0], treasure_pos[1], 50, 50)
    
    if player_rect.colliderect(treasure_rect):
        score += 1
        level += 1
        treasure_pos = [random.randint(0, WIDTH - 50), random.randint(0, HEIGHT - 50)]  # Respawn treasure

    # Fill the background
    screen.blit(bg_image, (0, 0))

    # Draw player and treasure
    screen.blit(player_image, (player_pos[0], player_pos[1]))
    screen.blit(treasure_image, (treasure_pos[0], treasure_pos[1]))

    # Draw score and level
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f'Score: {score} Level: {level}', True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()
    pygame.time.Clock().tick(30)  # Limit the frame rate to 30 FPS

# Quit Pygame
pygame.quit()
