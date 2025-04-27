import pygame
import random
import sys

pygame.init()
width, height = 800, 600
sk_size = 20
vel = 20
highscore_file = 'snake_highscore.txt'

sk_x = sk_y = 0
sk_direction = None
snake_body = []
snake_length = 1
apple_x = apple_y = 0
score = 0
highscore = 0
game_over = False

clock = pygame.time.Clock()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

font_small = pygame.font.SysFont("comicsans", 30, bold=True)
font_large = pygame.font.SysFont("comicsans", 50, bold=True)

def read_highscore():
    global highscore
    try:
        with open(highscore_file, 'r') as f:
            highscore = int(f.read().strip())
    except (FileNotFoundError, ValueError):
        highscore = 0

def write_highscore():
    with open(highscore_file, 'w') as f:
        f.write(str(highscore))

def restart():
    global sk_x, sk_y, sk_direction, snake_body, snake_length, apple_x, apple_y, score, game_over
    sk_x = width // 2
    sk_y = height // 2
    sk_direction = None
    snake_body = [(sk_x, sk_y)]
    snake_length = 1
    apple_x = random.randint(0, (width - sk_size) // sk_size) * sk_size
    apple_y = random.randint(0, (height - sk_size) // sk_size) * sk_size
    score = 0
    game_over = False

def check_boundaries():
    global game_over
    if sk_x < 0 or sk_x + sk_size > width or sk_y < 0 or sk_y + sk_size > height:
        game_over = True

def check_self_collision():
    global game_over
    if (sk_x, sk_y) in snake_body[:-1]:
        game_over = True

def draw_snake():
    for seg in snake_body:
        pygame.draw.rect(win, (128, 128, 0), (seg[0], seg[1], sk_size, sk_size))

def draw_apple():
    pygame.draw.rect(win, (255, 0, 0), (apple_x, apple_y, sk_size, sk_size))

def draw_score():
    txt_score = font_small.render(f"Score : {score}", True, (0, 0, 0))
    txt_high = font_small.render(f"Highscore : {highscore}", True, (0, 0, 0))
    win.blit(txt_score, (10, 10))
    win.blit(txt_high, (10, 40))

def draw_game_over():
    txt_over = font_large.render("GAME OVER", True, (255, 0, 0))
    txt_restart = font_small.render("Press R to restart", True, (0, 0, 0))
    txt_quit = font_small.render("Press Q to quit", True, (0, 0, 0))
    win.blit(txt_over, txt_over.get_rect(center=(width//2, height//2 - 50)))
    win.blit(txt_restart, txt_restart.get_rect(center=(width//2, height//2)))
    win.blit(txt_quit, txt_quit.get_rect(center=(width//2, height//2 + 40)))
    pygame.display.update()

def draw_frame():
    win.fill((124, 252, 0))
    draw_snake()
    draw_apple()
    draw_score()
    pygame.display.update()

def main():
    global sk_x, sk_y, sk_direction, snake_body, snake_length
    global apple_x, apple_y, score, highscore, game_over

    read_highscore()
    restart()
    running = True
    while running:
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and game_over:
                    running = False
                elif event.key == pygame.K_r and game_over:
                    restart()
                elif not game_over:
                    if sk_direction is None:
                        if event.key == pygame.K_a:
                            sk_direction = 'LEFT'
                        elif event.key == pygame.K_d:
                            sk_direction = 'RIGHT'
                        elif event.key == pygame.K_w:
                            sk_direction = 'UP'
                        elif event.key == pygame.K_s:
                            sk_direction = 'DOWN'
                    else:
                        if event.key == pygame.K_a and sk_direction != 'RIGHT':
                            sk_direction = 'LEFT'
                        elif event.key == pygame.K_d and sk_direction != 'LEFT':
                            sk_direction = 'RIGHT'
                        elif event.key == pygame.K_w and sk_direction != 'DOWN':
                            sk_direction = 'UP'
                        elif event.key == pygame.K_s and sk_direction != 'UP':
                            sk_direction = 'DOWN'
        if not game_over:
            if sk_direction is not None:
                if sk_direction == 'LEFT':
                    sk_x -= vel
                elif sk_direction == 'RIGHT':
                    sk_x += vel
                elif sk_direction == 'UP':
                    sk_y -= vel
                elif sk_direction == 'DOWN':
                    sk_y += vel
                if sk_x == apple_x and sk_y == apple_y:
                    snake_length += 1
                    score += 1
                    apple_x = random.randint(0, (width - sk_size) // sk_size) * sk_size
                    apple_y = random.randint(0, (height - sk_size) // sk_size) * sk_size
                    if score > highscore:
                        highscore = score
                        write_highscore()
                snake_body.append((sk_x, sk_y))
                if len(snake_body) > snake_length:
                    del snake_body[0]
                check_boundaries()
                check_self_collision()
            draw_frame()
        else:
            draw_game_over()
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
