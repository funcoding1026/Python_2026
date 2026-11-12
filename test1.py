import importlib
import random
import sys

try:
    pygame = importlib.import_module("pygame")
except ModuleNotFoundError:
    print("Pygame is not installed. Install it with: python -m pip install pygame")
    sys.exit(1)

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Coin!")

# Colors (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 150, 255)
YELLOW = (255, 215, 0)

# Clock to control frame rate
clock = pygame.time.Clock()

# Player settings
player_width = 50
player_height = 50
player_x = (SCREEN_WIDTH // 2) - (player_width // 2)
player_y = SCREEN_HEIGHT - player_height - 20
player_speed = 8

# Coin settings
coin_radius = 15
coin_x = random.randint(coin_radius, SCREEN_WIDTH - coin_radius)
coin_y = 0
coin_speed = 4

# Game variables
score = 0
font = pygame.font.SysFont("Arial", 36)

# Main game loop
running = True
while running:
    # 1. Handle Events (Inputs)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check keyboard inputs for continuous movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += player_speed

    # 2. Game Logic / Updates
    # Move the coin downward
    coin_y += coin_speed

    # Create bounding boxes (rectangles) for collision checking
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    coin_rect = pygame.Rect(coin_x - coin_radius, coin_y - coin_radius, coin_radius * 2, coin_radius * 2)

    # Check if player catches the coin
    if player_rect.colliderect(coin_rect):
        score += 1
        coin_speed += 0.5  # Make it slightly harder
        # Reset coin to the top
        coin_x = random.randint(coin_radius, SCREEN_WIDTH - coin_radius)
        coin_y = 0

    # Check if coin misses and hits the bottom
    if coin_y > SCREEN_HEIGHT:
        score = 0  # Reset score
        coin_speed = 5  # Reset speed
        # Reset coin to the top
        coin_x = random.randint(coin_radius, SCREEN_WIDTH - coin_radius)
        coin_y = 0

    # 3. Drawing / Rendering
    screen.fill(BLACK)  # Clear screen with black background

    # Draw Player (Blue Square)
    pygame.draw.rect(screen, BLUE, player_rect)

    # Draw Coin (Yellow Circle)
    pygame.draw.circle(screen, YELLOW, (coin_x, coin_y), coin_radius)

    # Draw Score Text
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

# Quit Pygame clean up
pygame.quit()
sys.exit()
