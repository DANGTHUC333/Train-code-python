import pygame
import sys
import random

pygame.init()
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
# hàm
def draw_floor():
    screen.blit(floor, (floor_x_pos, 340))
    screen.blit(floor, (floor_x_pos + 335, 340))
    screen.blit(floor, (floor_x_pos + 670, 340))
    screen.blit(floor, (floor_x_pos + 1005, 340))

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    new_pipe = pipe_surface.get_rect(midtop=(1000, random_pipe_pos))
    return new_pipe
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes
def draw_pipe(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface, pipe)

def create_coin():
    random_coin_pos = random.choice(coin_height)
    new_coin = coin_surface.get_rect(midtop=(1000, random_coin_pos))
    return new_coin
def move_coin(coins):
    for coin in coins:
        coin.centerx -= 5
    return coins
def draw_coin(coins):
    for coin in coins:
        screen.blit(coin_surface, coin)

def check_collistion(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            hit_sound.play()
            return False


    return True

def rotate_bird(bird1):
    new_bird = pygame.transform.rotozoom(bird1, -bird_move*3, 1)
    return new_bird

def bird_animation():
    new_bird = bird_list[bird_index]
    new_bird_rect = new_bird.get_rect(center=(100,bird_rect.centery))
    return new_bird, new_bird_rect

def score_display(game_state):
    if game_state == 'main game':
        score_surface = game_font.render(f'Score: {int(score)}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(110, 40))
        screen.blit(score_surface, score_rect)
    if game_state == 'game over':
        score_surface = game_font.render(f'Score: {int(score)}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(370, 50))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f'High score: {int(high_score)}', True, (255, 255, 255))
        high_score_rect = high_score_surface.get_rect(center=(370, 300))
        screen.blit(high_score_surface, high_score_rect)


def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score

def kiem_tra_va_cham_coin(coins):
    global score
    for coin in coins[:]:  # Duyệt qua bản sao của danh sách để có thể xóa đồng xu khi lặp
        if bird_rect.colliderect(coin):
            coins.remove(coin)  # Xóa đồng xu khỏi danh sách
            point_sound.play()
            score += 100  # Tăng điểm

def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= pipe_speed
    return pipes

def move_coin(coins):
    for coin in coins:
        coin.centerx -= coin_speed
    return coins


# tạo cửa sổ
screen = pygame.display.set_mode((736, 368))
pygame.display.set_caption("The forest")

#font chữ
game_font = pygame.font.Font('04B_19.TTF', 40)

# Màn hình kết thúc
game_over_surface = pygame.transform.scale2x(pygame.image.load('yellowbird-upflap.png').convert_alpha())
game_over_rect = game_over_surface.get_rect(center=(370, 180))

# set fps
clock = pygame.time.Clock()

# background
bg = pygame.image.load('bg.jpg').convert()  # convert giúp load hình ảnh nhanh hơn

# Sàn
floor = pygame.image.load('floor.png').convert()
floor_x_pos = 0

# biến
gravity = 0.5  # gravity (trọng lực)
bird_move = 0
jump_count = 0  # Biến để theo dõi số lần nhảy
game_active = False
score = 0
high_score = 0
pipe_speed = 0.001  # Tốc độ ban đầu của ống
coin_speed = 0.001  # Tốc độ ban đầu của đồng tiền

# Chim
bird_down = pygame.image.load('yellowbird-downflap.png').convert_alpha()
bird_mid = pygame.image.load('yellowbird-midflap.png').convert_alpha()
bird_up = pygame.image.load('yellowbird-upflap.png').convert_alpha()
bird_list = [bird_down, bird_mid, bird_up]  # 0,1,2
bird_index = 0
bird = bird_list[bird_index]
# bird = pygame.image.load('yellowbird-downflap.png').convert_alpha()
bird_rect = bird.get_rect(center=(120, 328))

# ống
pipe_surface = pygame.image.load('tree.png').convert_alpha()
pipe_surface = pygame.transform.scale(pipe_surface, (60, 180))
pipe_height = [180, 200, 220, 240]
pipe_list = []

# tiền
coin_surface = pygame.image.load('coin.png').convert_alpha()
coin_surface = pygame.transform.scale(coin_surface, (50, 50))
coin_height = [200, 180, 160, 100]
coin_list = []

# tạo timer
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 1200)

spawncoin = pygame.USEREVENT + 1
pygame.time.set_timer(spawncoin, 4000)

birdflap = pygame.USEREVENT + 2
pygame.time.set_timer(birdflap, 200)

# chèm âm thanh
flap_sound = pygame.mixer.Sound('sfx_wing.wav')
hit_sound = pygame.mixer.Sound('sfx_hit.wav')
point_sound = pygame.mixer.Sound('sfx_point.wav')

# Âm nhạc nền
pygame.mixer.music.load('pixel-dreams-259187.mp3')  # Thay bằng tên file nhạc của bạn
pygame.mixer.music.set_volume(0.5)  # Đặt âm lượng (0.0 đến 1.0)
pygame.mixer.music.play(-1)  # Phát nhạc lặp vô hạn

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and jump_count < 2 and game_active:
                bird_move = -11
                jump_count += 1  # Tăng số lần nhảy
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                coin_list.clear()
                bird_move = 0
                bird_rect.center = (120, 328)
                score = 0
                pipe_speed = 5
                coin_speed = 5
        if event.type == spawnpipe:
            pipe_list.append(create_pipe())

        if event.type == spawncoin:
            coin_list.append(create_coin())

        if event.type == birdflap:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0
            bird, bird_rect = bird_animation()

    screen.blit(bg, (0, 0))
    if game_active:
        # chim
        bird_move += gravity
        rotated_bird = rotate_bird(bird)
        bird_rect.centery += bird_move
        game_active = check_collistion(pipe_list)
        # Kiểm tra nếu chim chạm sàn
        if bird_rect.bottom >= 340:  # 340 là vị trí của sàn
            bird_rect.bottom = 340
            bird_move = 0  # Dừng chim khi chạm đất
            jump_count = 0  # Đặt lại số lần nhảy khi chạm sàn

        screen.blit(rotated_bird, bird_rect)
        # ống
        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)
        # tiền
        coin_list = move_coin(coin_list)
        kiem_tra_va_cham_coin(coin_list)
        draw_coin(coin_list)
        # điểm
        score += 0.1
        score_display('main game')
        # tăng tốc game
        if int(score) % 100 == 0 and score > 0:  # Tăng tốc mỗi 10 điểm
            pipe_speed += 0.05
            coin_speed += 0.05
    else:
        # thêm text
        space_text_surface = game_font.render("'Space         Play'", True, (255, 255, 255))
        space_text_rect = space_text_surface.get_rect(center=(350, 180))
        screen.blit(space_text_surface, space_text_rect)

        screen.blit(game_over_surface, game_over_rect)
        high_score = update_score(score, high_score)
        score_display('game over')
    # sàn
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= - 335:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(60)
