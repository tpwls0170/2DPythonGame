from pico2d import*
import game_framework
import title_state
import random

class BackGrand1:
    def __init__(self):
        self.x = 400
        self.image = load_image('bg.png')
        self.bgm = load_music('Circus Charlie.mp3')
        self.bgm.set_volume(60)
        self.bgm.repeat_play()

    def draw(self):
        self.image.draw(self.x,300)

    def bg_move(self):
        self.x -=5
        if(self.x == 0):
            self.x = 400;

class BackGrand2:
    def __init__(self):
        self.x = 800
        self.image = load_image('bg.png')

    def draw(self):
        self.image.draw(self.x,300)
    def bg_move(self):
        self.x -=5
        if (self.x == 400):
            self.x = 800;

class BackGrand3:
    def __init__(self):
        self.x = 1200
        self.image = load_image('bg.png')

    def draw(self):
        self.image.draw(self.x,300)
    def bg_move(self):
        self.x -=5
        if (self.x == 800):
            self.x = 1200;
class Trap:
    def __init__(self):
        self.x, self.y = random.randint(800,1200),250
        self.frame = random.randint(0,4)
        self.image = load_image('Circus Charlie2.png')

    def draw(self):
        self.image.clip_draw(self.frame*100, 400, 80, 150, self.x, self.y,80,200)
        # self.image.clip_draw(self,left,bottom,width,high,x,y,w,h)

    def Trap_move(self):
        self.x -= 2
        self.frame = 4
        #self.x +=2

class Lion:
    def __init__(self):
        self.x, self.y = 200,100
        self.frame = 0
        self.image = load_image('Circus Charlie Lion.png')
        self.jump = False

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 160, 60, self.x, self.y)

    def Lion_move(self):
        self.frame = (self.frame + 2) % 4
        #self.x +=2
        delay(0.03)
        if(self.jump):
            self.y += 10
            if(self.y > 300):
                self.jump = False
        else:
            self.y = max(100, self.y - 10)

    def updatejump(self):
        self.frame = (self.frame + 1) % 4
        self.y += 20

class Boy:
    def __init__(self):
        self.x, self.y = 200, 160
        self.frame = 0
        self.image = load_image('Circus Charlie.png')

    def update(self):
        self.frame = (self.frame + 1) % 2
        #self.x += 2
        delay(0.03)

    def updatejump(self):
        self.frame = (self.frame + 1) % 4
        self.y += 20

    def updatedown(self):
        self.frame = (self.frame + 1) % 4


    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 65, 80, self.x, self.y)
        #self.image.clip_draw(self,left,bottom,width,high,x,y,w,h)
        #self.image.clip_draw_to_origin(self.frame*100, 920, 45, 70, self.x, self.y,70,70)

def enter():
    global boy, backgrand1, backgrand2, backgrand3, lion, trap
    boy = Boy()
    backgrand1 = BackGrand1()
    backgrand2 = BackGrand2()
    backgrand3 = BackGrand3()
    lion = Lion()
    trap = [Trap() for i in range(4)]

def exit():
    global boy
    del(boy)

def handle_events():
    global running
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            #boy.updatejump()
            #Lion.updatejump()
            lion.jump = True
        elif event.key == SDLK_ESCAPE:
            backgrand1.bgm.stop()
            game_framework.change_state(title_state)

def update():
    boy.update()
    backgrand1.bg_move()
    backgrand2.bg_move()
    backgrand3.bg_move()
    lion.Lion_move()

def draw():
    clear_canvas()
    backgrand1.draw()
    backgrand2.draw()
    backgrand3.draw()
    boy.draw()
    lion.draw()
    for TTrap in trap:
        TTrap.draw()
        TTrap.Trap_move()
    update_canvas()
    handle_events()

