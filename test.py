import pygame
import sys
import random

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Thiết lập màn hình
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Square Jump Game")

# Đồng hồ để điều khiển tốc độ khung hình
clock = pygame.time.Clock()
FPS = 60

# Thuộc tính người chơi
player_size = 50
player_x = 100
player_y = SCREEN_HEIGHT - player_size
player_y_velocity = 0
player_gravity = 1
player_is_jumping = False

# Thuộc tính chướng ngại vật
obstacle_width = 30
obstacle_x = SCREEN_WIDTH
obstacle_y = SCREEN_HEIGHT - obstacle_width
obstacle_speed = 5
obstacle_type = "ground"
obstacle_shapes = ["triangle", "rectangle", "circle"]

# Biến cho vòng lặp chính của trò chơi
running = True
score = 0
font = pygame.font.Font(None, 36)

def reset_game():
    global player_y, player_y_velocity, player_is_jumping, obstacle_x, obstacle_speed, score, obstacle_type
    player_y = SCREEN_HEIGHT - player_size
    player_y_velocity = 0
    player_is_jumping = False
    obstacle_x = SCREEN_WIDTH
    obstacle_speed = 5
    score = 0
    obstacle_type = "ground"

while running:
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not player_is_jumping:
                player_y_velocity = -15
                player_is_jumping = True
            if event.key == pygame.K_r and not running:
                reset_game()
                running = True

    # Cập nhật vị trí người chơi
    player_y += player_y_velocity
    player_y_velocity += player_gravity

    # Ngăn người chơi rơi xuống dưới mặt đất
    if player_y >= SCREEN_HEIGHT - player_size:
        player_y = SCREEN_HEIGHT - player_size
        player_is_jumping = False

    # Cập nhật vị trí và tốc độ chướng ngại vật
    obstacle_x -= obstacle_speed
    if obstacle_x < -obstacle_width:
        obstacle_x = SCREEN_WIDTH
        obstacle_type = random.choice(obstacle_shapes)
        obstacle_speed += 0.5
        score += 1
        if obstacle_type == "ground":
            obstacle_y = SCREEN_HEIGHT - random.randint(30, 70)
        elif obstacle_type == "air":
            obstacle_y = SCREEN_HEIGHT - player_size - random.randint(20, 50)

    # Phát hiện va chạm
    if (player_x < obstacle_x + obstacle_width and
        player_x + player_size > obstacle_x and
        player_y < obstacle_y + obstacle_width and
        player_y + player_size > obstacle_y):
        running = False

    # Vẽ các thành phần
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_size, player_size))
    if obstacle_type == "triangle":
        pygame.draw.polygon(screen, RED, [(obstacle_x, obstacle_y + obstacle_width),
                                           (obstacle_x + obstacle_width // 2, obstacle_y),
                                           (obstacle_x + obstacle_width, obstacle_y + obstacle_width)])
    elif obstacle_type == "rectangle":
        pygame.draw.rect(screen, BLUE, (obstacle_x, obstacle_y, obstacle_width, obstacle_width))
    elif obstacle_type == "circle":
        pygame.draw.circle(screen, GREEN, (obstacle_x + obstacle_width // 2, obstacle_y + obstacle_width // 2), obstacle_width // 2)

    # Hiển thị điểm số
    score_text = font.render(f"Điểm: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Nếu chết, hiển thị nút chơi lại
    if not running:
        game_over_text = font.render("Game Over! Nhấn R để chơi lại", True, WHITE)
        screen.blit(game_over_text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))

    # Cập nhật màn hình
    pygame.display.flip()

    # Điều chỉnh tốc độ khung hình
    clock.tick(FPS)

# Thoát Pygame
pygame.quit()
sys.exit()
