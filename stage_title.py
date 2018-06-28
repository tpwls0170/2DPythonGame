from pico2d import *
import game_framework
import main_state
import stage_1
#import stage_2
#import stage_3

name = "Stage State"
image = None
title_time = 0


def enter():
    global image
    image = load_image('stage_title1.png')


def exit():

    global image
    del (image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_1):
                game_framework.change_state(stage_1)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_2):
                game_framework.change_state(main_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_3):
                game_framework.change_state(main_state)


def update():
    global title_time
    if (title_time > 1.0):
        title_time = 0
        # game_framework.quit()
        game_framework.change_state(main_state)


def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
