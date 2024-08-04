# # import time
# #
# # import pygame
# # import sys
# #
# # def run():
# #     pygame.init()
# #     screen = pygame.display.set_mode((800, 400))
# #
# #     character_image = pygame.image.load('image/character_staying.png')
# #     character_rect = character_image.get_rect()
# #     character_rect.bottom = 370
# #
# #     background_image = pygame.image.load('image/bg_img-py.jpg')
# #     background_rect = background_image.get_rect()
# #
# #     while True:
# #         for event in pygame.event.get():
# #             if event.type == pygame.QUIT:
# #                 sys.exit()
# #
# #         keys = pygame.key.get_pressed()
# #
# #         if keys[pygame.K_LEFT]:
# #             character_rect.x -= 1
# #         if keys[pygame.K_RIGHT]:
# #             character_rect.x += 1
# #         if keys[pygame.K_UP]:
# #             character_rect.y -= 1
# #         if keys[pygame.K_DOWN]:
# #             character_rect.y += 1
# #
# #         if character_rect.left < 0:
# #             character_rect.left = 0
# #         if character_rect.right > screen.get_width():
# #             character_rect.right = screen.get_width()
# #         if character_rect.top < 0:
# #             character_rect.top = 0
# #         if character_rect.bottom > screen.get_height():
# #             character_rect.bottom = screen.get_height()
# #
# #         screen.blit(background_image, background_rect)
# #         screen.blit(character_image, character_rect)
# #         pygame.display.flip()
# #
# # run()
#
#
#
#
#
#
#
# import pygame
# import time
# import random
#
# pygame.init()
#
# white = (255, 255, 255)
# yellow = (255, 255, 102)
# black = (0, 0, 0)
# red = (213, 50, 80)
# green = (0, 255, 0)
# blue = (50, 153, 213)
#
# dis_width = 800
# dis_height = 600
#
# dis = pygame.display.set_mode((dis_width, dis_height))
# pygame.display.set_caption('Snake Game')
#
# clock = pygame.time.Clock()
#
# snake_block = 10
# snake_speed = 30
#
# font_style = pygame.font.SysFont(None, 50)
# score_font = pygame.font.SysFont(None, 35)
#
#
# def our_snake(snake_block, snake_list):
#     for x in snake_list:
#         pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
#
#
# def message(msg, color):
#     mesg = font_style.render(msg, True, color)
#     dis.blit(mesg, [dis_width / 6, dis_height / 3])
#
#
# def game_loop():
#     game_over = False
#     game_close = False
#
#     x1 = dis_width / 2
#     y1 = dis_height / 2
#
#     x1_change = 0
#     y1_change = 0
#
#     snake_List = []
#     Length_of_snake = 1
#
#     foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#     foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
#
#     while not game_over:
#
#         while game_close == True:
#             dis.fill(blue)
#             message("You lost! Press Q-Quit or C-Play Again", red)
#             pygame.display.update()
#
#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_q:
#                         game_over = True
#                         game_close = False
#                     if event.key == pygame.K_c:
#                         game_loop()
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_over = True
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     x1_change = -snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_RIGHT:
#                     x1_change = snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_UP:
#                     y1_change = -snake_block
#                     x1_change = 0
#                 elif event.key == pygame.K_DOWN:
#                     y1_change = snake_block
#                     x1_change = 0
#
#         if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
#             game_close = True
#         x1 += x1_change
#         y1 += y1_change
#         dis.fill(blue)
#         pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
#         snake_Head = []
#         snake_Head.append(x1)
#         snake_Head.append(y1)
#         snake_List.append(snake_Head)
#         if len(snake_List) > Length_of_snake:
#             del snake_List[0]
#
#         for x in snake_List[:-1]:
#             if x == snake_Head:
#                 game_close = True
#
#         our_snake(snake_block, snake_List)
#
#         pygame.display.update()
#
#         if x1 == foodx and y1 == foody:
#             foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#             foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
#             Length_of_snake += 1
#
#         clock.tick(snake_speed)
#
#     pygame.quit()
#     quit()
#
#
# game_loop()


import math
import time
import os
import random
from colorama import init, Fore, Style

init(autoreset=True)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def rotate_point(x, y, z, angle_x, angle_y, angle_z):
    new_y = y * math.cos(angle_x) - z * math.sin(angle_x)
    new_z = y * math.sin(angle_x) + z * math.cos(angle_x)
    y, z = new_y, new_z

    new_x = x * math.cos(angle_y) + z * math.sin(angle_y)
    new_z = -x * math.sin(angle_y) + z * math.cos(angle_y)
    x, z = new_x, new_z

    new_x = x * math.cos(angle_z) - y * math.sin(angle_z)
    new_y = x * math.sin(angle_z) + y * math.cos(angle_z)
    x, y = new_x, new_y

    return x, y, z


def main():
    cube = [
        [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
        [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
    ]

    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]

    angle_x, angle_y, angle_z = 0, 0, 0
    pulse = 0
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

    while True:
        clear_screen()

        rotated_cube = [rotate_point(x, y, z, angle_x, angle_y, angle_z) for x, y, z in cube]

        screen = [[' ' for _ in range(60)] for _ in range(30)]

        for edge in edges:
            x1, y1, _ = rotated_cube[edge[0]]
            x2, y2, _ = rotated_cube[edge[1]]
            x1, y1 = int(x1 * 15 + 30), int(y1 * 7 + 15)
            x2, y2 = int(x2 * 15 + 30), int(y2 * 7 + 15)

            color = random.choice(colors)
            char = random.choice(['*', '+', 'o', '•', '×'])

            dx, dy = abs(x2 - x1), abs(y2 - y1)
            sx = 1 if x1 < x2 else -1
            sy = 1 if y1 < y2 else -1
            err = dx - dy

            while True:
                if 0 <= x1 < 60 and 0 <= y1 < 30:
                    screen[y1][x1] = color + char
                if x1 == x2 and y1 == y2:
                    break
                e2 = 2 * err
                if e2 > -dy:
                    err -= dy
                    x1 += sx
                if e2 < dx:
                    err += dx
                    y1 += sy

        pulse_char = '•' if pulse < 5 else '○'
        pulse = (pulse + 1) % 10

        for x, y, _ in rotated_cube:
            x, y = int(x * 15 + 30), int(y * 7 + 15)
            if 0 <= x < 60 and 0 <= y < 30:
                screen[y][x] = Style.BRIGHT + Fore.WHITE + pulse_char

        print('\n'.join(''.join(cell for cell in row) for row in screen))

        angle_x += 0.05
        angle_y += 0.07
        angle_z += 0.03

        time.sleep(0.1)


if __name__ == "__main__":
    main()
