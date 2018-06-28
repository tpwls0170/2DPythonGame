from pico2d import*
import game_framework
import stage_title



name = "TitleState"
image = None
title_time = 0

def enter():
    global image
    open_canvas()
    image = load_image('circustitle1.png')

def exit():
    global image
    del(image)

def handle_events():

        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                #game_framework.quit()
                game_framework.change_state(stage_title)
            else:
                if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                    game_framework.quit()
                elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                    game_framework.change_state(stage_title)



def update():
    global title_time
    if (title_time > 1.0):
        title_time = 0
        #game_framework.quit()
        game_framework.change_state(stage_title)


def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
