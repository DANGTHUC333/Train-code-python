import pygame
import sys
import random

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()

# tạo cửa sổ
screen = pygame.display.set_mode((432, 768))
pygame.display.set_caption("Chú Chim Béo")

# set fps
clock = pygame.time.Clock()


# background
bg = pygame.image.load('background-night.png').convert()  # convert giúp load hình ảnh nhanh hơn
bg = pygame.transform.scale2x(bg)

# chèn âm thanh
flap_sound = pygame.mixer.Sound('sfx_wing.wav')
hit_sound = pygame.mixer.Sound('sfx_hit.wav')
score_sound = pygame.mixer.Sound('sfx_point.wav')
score_sound_countdown = 99
die_sound = pygame.mixer.Sound('sfx_die.wav')

# Màn hình kết thúc
game_over_surface = pygame.transform.scale2x(pygame.image.load('message.png').convert_alpha())
game_over_rect = game_over_surface.get_rect(center=(216, 384))

# biến
gravity = 0.3  # gravity (trọng lực)
game_active = True
game_font = pygame.font.Font('04B_19.ttf', 40)
score = 0
high_score = 0

# xét điểm
def score_display(game_state):
    if game_state == 'main game':
        score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(216, 100))
        screen.blit(score_surface, score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(f'Score: {int(score)}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(216, 100))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f'High score: {int(high_score)}', True, (255, 255, 255))
        high_score_rect = high_score_surface.get_rect(center=(216, 620))
        screen.blit(high_score_surface, high_score_rect)

def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score

# floor
floor = pygame.image.load('floor.png').convert()
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0
def draw_floor():
    screen.blit(floor, (floor_x_pos, 650))
    screen.blit(floor, (floor_x_pos+432, 650))

# Bird
bird_down = pygame.transform.scale2x(pygame.image.load('yellowbird-downflap.png').convert_alpha())
bird_mid = pygame.transform.scale2x(pygame.image.load('yellowbird-midflap.png').convert_alpha())
bird_up = pygame.transform.scale2x(pygame.image.load('yellowbird-upflap.png').convert_alpha())
bird_list = [bird_down, bird_mid, bird_up]  # 0,1,2
bird_index = 0
bird = bird_list[bird_index]
# bird = pygame.image.load('yellowbird-midflap.png').convert_alpha()
# bird = pygame.transform.scale2x(bird)
bird_rect = bird.get_rect(center=(100, 384))
bird_move = 0
def rotate_bird(bird1):
    new_bird = pygame.transform.rotozoom(bird1, -bird_move*3, 1)
    return new_bird
def bird_animation():
    new_bird = bird_list[bird_index]
    new_bird_rect = new_bird.get_rect(center=(100, bird_rect.centery))
    return new_bird, new_bird_rect

# Tạo ống
pipe_surface = pygame.image.load('pipe-green.png').convert_alpha()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_height = [200, 300, 400]
pipe_list = []
def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bot_pipe = pipe_surface.get_rect(midtop=(500, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midtop=(500, random_pipe_pos - 700))
    return bot_pipe, top_pipe



def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes
def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >= 600:
         screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)
# tạo va chạm
def check_collison(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            hit_sound.play()
            return False
    if bird_rect.top <= -75 or bird_rect.bottom >= 650:
            die_sound.play()
            return False
    return True
# Tạo timer
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 1200)

birdflap = pygame.USEREVENT + 1
pygame.time.set_timer(birdflap, 200)


# tạo vòng lặp
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_move = -8
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100, 384)
                bird_move = 0
                score = 0
        if event.type == spawnpipe:
            pipe_list.extend(create_pipe())
        if event.type == birdflap:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0
            bird, bird_rect = bird_animation()
    screen.blit(bg, (0, 0))
    if game_active:
        # bird
        bird_move += gravity
        rotated_bird = rotate_bird(bird)
        bird_rect.centery += bird_move
        screen.blit(rotated_bird, bird_rect)
        game_active = check_collison(pipe_list)
        # pipe
        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)
        # điểm
        score += 0.1
        score_display('main game')
        score_sound_countdown -= 0.1
        if score_sound_countdown <= 0:
            score_sound.play()
            score_sound_countdown = 99
    else:
        screen.blit(game_over_surface,game_over_rect)
        high_score = update_score(score, high_score)
        score_sound_countdown = 99
        score_display('game_over')
    # floor
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -432:
        floor_x_pos = 0
    pygame.display.update()
    clock.tick(60)
