# # maps = [1,2,3
# #         4,5,6,
# #         7,8,9]

# # victories = [0,1,2],
# # [3,4,5],

# import pygame as pg, sys
# from pygame.locals import *
# import time, random

# width = 400
# height = 400
# white = (255, 255, 255)
# RED = (255, 0, 0)
# BLACK = (0, 0, 0)
# line_color = (10, 10, 10)

# # initializing pygame window
# pg.init()
# fps = 30
# CLOCK = pg.time.Clock()
# screen = pg.display.set_mode((width, height + 100), 0, 32)
# pg.display.set_caption("Tic Tac Toe")

# # loading the images
# opening = pg.image.load("tic tac opening.png")
# x_img = pg.image.load("x.png")
# o_img = pg.image.load("o.png")

# # resizing images
# x_img = pg.transform.scale(x_img, (80, 80))
# o_img = pg.transform.scale(o_img, (80, 80))
# opening = pg.transform.scale(opening, (width, height + 100))


def display_board():
    print("Welcome to Tic Tac Toe")
    print("Tic Tac Toe")
    print("**************************")
    print(f"*      |       |        *")
    print("*-------|-------|--------*")
    print("*  {x}  |       |        *")
    print("*-------|-------|--------*")
    print("*       |       |        *")
    print("**************************")


display_board()
row = 1
column = 1
# board = ' '

# for i in range(1,10):
#     if i % 3 != 0:
#         board += '  '
