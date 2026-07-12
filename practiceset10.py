import pygame
import random

# Initialize pygame
pygame.init()

# Screen
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Snake settings
BLOCK = 20
speed = 10

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

def draw_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

def game():
    x = WIDTH // 2
    y = HEIGHT // 2

    dx = BLOCK
    dy = 0

    snake = []
    length = 1

    food_x = random.randrange(0, WIDTH - BLOCK, BLOCK)
    food_y = random.randrange(0, HEIGHT - BLOCK, BLOCK)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -BLOCK
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = BLOCK
                    dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx = 0
                    dy = -BLOCK
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx = 0
                    dy = BLOCK

        x += dx
        y += dy

        # Wall collision
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            running = False

        head = [x, y]
        snake.append(head)

        if len(snake) > length:
            del snake[0]

        # Self collision
        if head in snake[:-1]:
            running = False

        # Food collision
        if x == food_x and y == food_y:
            food_x = random.randrange(0, WIDTH - BLOCK, BLOCK)
            food_y = random.randrange(0, HEIGHT - BLOCK, BLOCK)
            length += 1

        # Draw
        screen.fill(BLACK)

        pygame.draw.rect(screen, RED, (food_x, food_y, BLOCK, BLOCK))

        for part in snake:
            pygame.draw.rect(screen, GREEN, (part[0], part[1], BLOCK, BLOCK))

        draw_score(length - 1)

        pygame.display.update()
        clock.tick(speed)

    # Game Over
    screen.fill(BLACK)
    text = font.render(f"Game Over! Score: {length-1}", True, RED)
    screen.blit(text, (130, 170))
    pygame.display.update()
    pygame.time.wait(3000)

game()
pygame.quit()