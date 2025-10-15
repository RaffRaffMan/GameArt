import pygame

# Initialize window.
pygame.init()

# screen is a Surface (to render game onto).
# set_mode returns a Surface.
screen = pygame.display.set_mode((800, 600))
screen_rect = pygame.Rect(0, 0, 800, 600)

clock = pygame.time.Clock()

running = True

# Create hitboxes for paddles.
left_pad = pygame.Rect(50, 255, 8, 90)
right_pad = pygame.Rect(750, 255, 8, 90)

# Create ball hitbox (as rectangle) and set it to center of the screen.
ball = pygame.Rect(0, 0, 16, 16)
ball.center = (400, 300)

# Set ball velocity.
ball_vx = 7
ball_vy = 7

# Main game loop. Runs 60 times per second.
while running:
    # Poll for events. Iterate through every event in the queue.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with color to clear previous frame.
    screen.fill("black")

    # -------------- UPDATE THE GAME HERE -----------------
    # Get state of keys.
    keys = pygame.key.get_pressed()

    # Move left pad.
    if keys[pygame.K_w]:
        left_pad.move_ip(0, -10)
    if keys[pygame.K_s]:
        left_pad.move_ip(0, 10)

    # Move right pad.
    if keys[pygame.K_UP]:
        right_pad.move_ip(0, -10)
    if keys[pygame.K_DOWN]:
        right_pad.move_ip(0, 10)

    # Clamp paddles.
    left_pad.clamp_ip(screen_rect)
    right_pad.clamp_ip(screen_rect)

    # Move ball each frame.
    ball.move_ip(ball_vx, ball_vy)

    # EXECUTE BALL COLLISIONS
    # 1. If ball hits top or bottom edges, bounce vertically.
    if ball.top <= screen_rect.top or ball.bottom >= screen_rect.bottom:
        ball_vy = -ball_vy

    # 2. If ball hits paddles, bounce horizontally.
    if ball.colliderect(left_pad) or ball.colliderect(right_pad):
        ball_vx = -ball_vx

    # 3. If ball hits left or right edges, respawn at center.
    if ball.left <= screen_rect.left or ball.right >= screen_rect.right:
        ball.center = (400, 300)

    # Draw left pad.
    pygame.draw.rect(screen, "white", left_pad)

    # Draw right pad.
    pygame.draw.rect(screen, "white", right_pad)

    # Draw ball.
    pygame.draw.circle(screen, "white", ball.center, 8)
    # -----------------------------------------------------
    
    # Flip display to render the new frame.
    pygame.display.flip()

    # Limit framerate to 60 FPS.
    clock.tick(60)

pygame.quit()