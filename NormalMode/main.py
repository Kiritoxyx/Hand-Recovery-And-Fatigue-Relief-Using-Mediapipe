# Setup Python ----------------------------------------------- #
import sys
import os

from NormalMode import ui
from NormalMode.settings import *
from lane import Lane
from enemy import EnemyHandle
from game import *
from NormalMode.ball import BallHandle
from hexagon import *

# from game import Game
# from menu import Menu
# Setup pygame/window --------------------------------------------- #
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 32)  # windows position
pygame.init()
pygame.display.set_caption(WINDOW_NAME)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

mainClock = pygame.time.Clock()
# Fonts ----------------------------------------------------------- #
fps_font = pygame.font.SysFont("Silver.ttf", 22)

# Music ----------------------------------------------------------- #
pygame.mixer.music.load("Assets/Sounds/background.mp3")
pygame.mixer.music.set_volume(MUSIC_VOLUME)
pygame.mixer.music.play(-1)


def user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


def update():
    pygame.display.update()
    mainClock.tick(FPS)


lane = [Lane(LANE_X, LANE_Y),
        Lane(LANE_X, LANE_Y + LANE_VEL),
        Lane(LANE_X, LANE_Y + LANE_VEL * 2)]

# TODO 新增
hexagon1 = Hexagon(LANE_X + 30, LANE_Y)
hexagon2 = Hexagon(LANE_X + 30, LANE_Y + LANE_VEL)
hexagon3 = Hexagon(LANE_X + 30, LANE_Y + LANE_VEL * 2)

scroll_bar = ScrollBar()
ball_handle = BallHandle()
enemy_handle = EnemyHandle()
game = Game(SCREEN, ball_handle, enemy_handle, scroll_bar)

# Loop ------------------------------------------------------------ #
while True:
    user_events()
    SCREEN.fill((255, 255, 255))
    SCREEN.blit(background, background_rect)

    hexagon1.draw_hexagon(SCREEN)
    hexagon2.draw_hexagon(SCREEN)
    hexagon3.draw_hexagon(SCREEN)
    # lane[0].draw_lane(SCREEN)
    # lane[1].draw_lane(SCREEN)
    # lane[2].draw_lane(SCREEN)
    game.update(ball_handle, SCREEN, lane, enemy_handle, scroll_bar)
    game.draw_score()
    # 更新滚动条
    update()

    # 添加重新开始按钮
    if ui.button(SCREEN, 10, 10, "Restart"):
        game.reset()  # 假设你有一个重置游戏状态的方法

    # 更新屏幕显示
    pygame.display.flip()
    # FPS
    if DRAW_FPS:
        fps_label = fps_font.render(f"FPS: {int(mainClock.get_fps())}", 1, (255, 200, 20))
        SCREEN.blit(fps_label, (5, 5))
