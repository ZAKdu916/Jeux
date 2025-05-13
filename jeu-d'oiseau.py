import pygame
import random


pygame.init()


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


gravity = 0.25
bird_movement = 0
bird_speed = -7
bird_x = 50
bird_y = 300
bird_width = 40
bird_height = 40

pipe_width = 70
pipe_height = random.randint(150, 400)
pipe_gap = 150
pipe_velocity = 4
pipes = []


clock = pygame.time.Clock()


font = pygame.font.SysFont("Arial", 36)


def draw_text(text, x, y):
    label = font.render(text, True, BLACK)
    screen.blit(label, (x, y))


def draw_bird(y_pos):
    pygame.draw.rect(screen, BLUE, (bird_x, y_pos, bird_width, bird_height))


def create_pipe():
    height = random.randint(150, 400)
    pipe = {'x': SCREEN_WIDTH, 'height': height}
    pipes.append(pipe)

def move_pipes():
    global pipes
    for pipe in pipes:
        pipe['x'] -= pipe_velocity
    pipes = [pipe for pipe in pipes if pipe['x'] + pipe_width > 0]

def draw_pipes():
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, (pipe['x'], 0, pipe_width, pipe['height']))
        pygame.draw.rect(screen, GREEN, (pipe['x'], pipe['height'] + pipe_gap, pipe_width, SCREEN_HEIGHT))


def game_loop():
    global bird_y, bird_movement, pipes
    running = True
    while running:
        screen.fill(WHITE)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_movement = bird_speed

        
        bird_movement += gravity
        bird_y += bird_movement

        
        if len(pipes) == 0 or pipes[-1]['x'] < SCREEN_WIDTH - 200:
            create_pipe()

        move_pipes()
        draw_pipes()

        
        draw_bird(bird_y)

        
        if bird_y > SCREEN_HEIGHT - bird_height or bird_y < 0:
            running = False

        
        for pipe in pipes:
            if bird_x + bird_width > pipe['x'] and bird_x < pipe['x'] + pipe_width:
                if bird_y < pipe['height'] or bird_y + bird_height > pipe['height'] + pipe_gap:
                    running = False

        
        draw_text(f"Score: {len(pipes)}", 10, 10)

       
        pygame.display.update()

        
        clock.tick(60)


game_loop()
pygame.quit()
