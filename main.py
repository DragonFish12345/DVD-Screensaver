from random import randint
from time import sleep
from sys import exit

import pygame as pg


pg.init()

screen = pg.display.set_mode((800, 500))
pg.display.set_caption('DVD Screensaver')
icon = pg.image.load('dvd-32.png')
pg.display.set_icon(icon)
background = (0, 0, 0)

dvd_image = pg.image.load('dvdlogo-03.png')
starting_x, starting_y = randint(0, 613), randint(0, 417)
speed_x = speed_y = 1


def put_image_up(x, y):
    screen.blit(dvd_image, (x, y))


def set_color(img, color):
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            color.a = img.get_at((x, y)).a  # Preserve the alpha value.
            img.set_at((x, y), color)  # Set the color of the pixel.


random_r, random_g, random_b = randint(0, 255), randint(0, 255), randint(0, 255)
set_color(dvd_image, pg.Color(random_r, random_g, random_b))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    random_r, random_g, random_b = randint(0, 255), randint(0, 255), randint(0, 255)

    # UP
    if starting_y == 0:
        speed_y = 1
        set_color(dvd_image, pg.Color(random_r, random_g, random_b))

    # DOWN
    if starting_y == 417:
        speed_y = -1
        set_color(dvd_image, pg.Color(random_r, random_g, random_b))

    # LEFT
    if starting_x == 0:
        speed_x = 1
        set_color(dvd_image, pg.Color(random_r, random_g, random_b))

    # RIGHT
    if starting_x == 613:
        speed_x = -1
        set_color(dvd_image, pg.Color(random_r, random_g, random_b))

    starting_x += speed_x
    starting_y += speed_y
    screen.fill(background)
    put_image_up(starting_x, starting_y)
    pg.display.flip()
    sleep(0.005)
