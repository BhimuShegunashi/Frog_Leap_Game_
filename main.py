# Bhimanna Shegunashi
import pygame
#import random

# Initialize Pygame
pygame.init()

# Game Constants
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
FROG_WIDTH = 30
FROG_HEIGHT = 30
OBSTACLE_WIDTH = 10
OBSTACLE_HEIGHT = 15
OBSTACLE_COLOR = (240, 18, 18)
BACKGROUND_COLOR = (134, 238, 242)
GRAVITY = 1
JUMP_STRENGTH = 15
GAME_SPEED = 5

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Frog and Leap")

# Font for displaying text
font = pygame.font.Font(None, 36)

# Load frog image
frog_image = pygame.image.load("frog.png")
frog_image = pygame.transform.scale(frog_image, (FROG_WIDTH, FROG_HEIGHT))
'''background_image = pygame.image.load("backgroundLake.jpg")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
obstacle_image = pygame.image.load("/mnt/data/obstacle.jpeg")
obstacle_image = pygame.transform.scale(obstacle_image, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))   '''


# Frog class
class Frog:
    def __init__(self):
        self.x = 100
        self.y = SCREEN_HEIGHT - FROG_HEIGHT
        self.vel_y = 0
        self.jumping = False

    def draw(self):
        # Draw the frog image
        screen.blit(frog_image, (self.x, self.y))

    def jump(self):
        if not self.jumping:
            self.jumping = True
            self.vel_y = -JUMP_STRENGTH

    def update(self):
        if self.jumping:
            self.vel_y += GRAVITY
            self.y += self.vel_y
            if self.y >= SCREEN_HEIGHT - FROG_HEIGHT:
                self.y = SCREEN_HEIGHT - FROG_HEIGHT
                self.jumping = False


# Obstacle class
class Obstacle:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.y = SCREEN_HEIGHT - OBSTACLE_HEIGHT
        self.width = OBSTACLE_WIDTH
        self.height = OBSTACLE_HEIGHT

    def draw(self):
        pygame.draw.rect(screen, OBSTACLE_COLOR, (self.x, self.y, self.width, self.height))
        # Draw the obstacle image
        # screen.blit(obstacle_image, (self.x, self.y))

    def update(self):
        self.x -= GAME_SPEED


# Game Over function
def game_over():
    screen.fill(BACKGROUND_COLOR)
    text = font.render("Game Over! Press R to Restart", True, (250, 0, 125))
    screen.blit(text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
    pygame.display.update()


# Main game loop
def main():
    clock = pygame.time.Clock()
    frog = Frog()
    obstacles = [Obstacle()]

    game_active = True

    while True:
        # for closing the game window/quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            # press space to jump the frog
            if event.type == pygame.KEYDOWN:
                if game_active:
                    if event.key == pygame.K_SPACE:
                        frog.jump()
                if not game_active and event.key == pygame.K_r:
                    main()

        if game_active:
            # Background
            screen.fill(BACKGROUND_COLOR)
            # Draw the background
            # screen.blit(background_image, (0, 0))

            # Update frog
            frog.update()
            frog.draw()

            # Update and draw obstacles
            if len(obstacles) == 0 or obstacles[-1].x < SCREEN_WIDTH - 200:
                obstacles.append(Obstacle())
            for obstacle in obstacles:
                obstacle.update()
                obstacle.draw()

            # Remove off-screen obstacles
            obstacles = [obs for obs in obstacles if obs.x + OBSTACLE_WIDTH > 0]

            # Check for collisions
            for obstacle in obstacles:
                if (frog.x + FROG_WIDTH > obstacle.x and
                        frog.x < obstacle.x + OBSTACLE_WIDTH and
                        frog.y + FROG_HEIGHT > obstacle.y):
                    game_active = False
                    game_over()

            # Refresh the screen
            pygame.display.update()

            # Set the frame rate
            clock.tick(60)


# Start the game
main()
