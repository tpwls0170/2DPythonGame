from pico2d import*
import game_framework
import title_state
import random



def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


class BackGrand1:
    Right = 2
    Left = 1
    Stop = 0

    def __init__(self):
        self.x = 400
        self.image = load_image('bg2.png')
        self.bgm = load_music('Circus Charlie.mp3')
        self.bgm.set_volume(60)
        self.bgm.repeat_play()
        self.state = self.Stop

    def draw(self):
        self.image.draw(self.x,300)

    def bg_Update(self):
        if self.state == self.Right:
            self.x -=5
            if(self.x == 0):
                self.x = 400;

class BackGrand2:
    Right = 2
    Left = 1
    Stop = 0
    def __init__(self):
        self.x = 800
        self.image = load_image('bg2.png')
        self.state = self.Stop

    def draw(self):
        self.image.draw(self.x,300)

    def bg_Update(self):
        if self.state == self.Right:
            self.x -=5
            if(self.x == 400):
                self.x = 800;

class BackGrand3:
    Right = 2
    Left = 1
    Stop = 0
    def __init__(self):
        self.x = 1200
        self.image = load_image('bg2.png')
        self.state = self.Stop
    def draw(self):
        self.image.draw(self.x,300)

    def bg_Update(self):
        if self.state == self.Right:
            self.x -= 5
            if (self.x == 800):
                self.x = 1200;
class Line:
    def __init__(self):
       # self.x, self.y = 400
        self.image = load_image('line2.png')
    def draw(self):
        self.image.draw(400, 370)


class Monkey_Trap:
    def __init__(self, x,y):
        self.x, self.y = x, y
        self.frame = 0
        self.image = load_image('monkey1.png')
    def get_bb(self):
        return self.x -45, self.y - 45, self.x+45 , self.y+45
    def draw_bb(self):
        draw_rectangle(self.x -45, self.y - 45, self.x+45 , self.y+45)
    def draw(self):
        self.image.clip_draw(self.frame * 75, 0, 75, 75 , self.x, self.y)
        self.draw_bb()
        self.frame = (self.frame + 1) % 4
        # self.image.clip_draw(self,left,bottom,width,high,x,y,w,h)
    def Trap_move(self):
        self.x -= 2

class Blue_Monkey_Trap:

    def __init__(self,x,y):
        self.x, self.y = x,y
        self.frame = 0
        self.image = load_image('bluemonkey.png')

    def get_bb(self):
        return self.x -45, self.y - 45, self.x+45 , self.y+45
    def draw(self):
        self.image.clip_draw(self.frame * 75, 0, 75, 75 , self.x, self.y)
        draw_rectangle(self.x -45, self.y - 45, self.x+45 , self.y+45)
        self.frame = (self.frame + 1) % 4
        # self.image.clip_draw(self,left,bottom,width,high,x,y,w,h)
    def Trap_move(self):
        self.x -= 4






class Charlie:
    Stop, LEFT_RUN, RIGHT_RUN = 0, 1, 2
    bgm = None
    def __init__(self):
        self.x, self.y = 200, 410
        self.frame = 0
        self.image = load_image('Circus Charlie.png')
        self.jump = False
        self.state = self.Stop

        if Charlie.bgm == None:
            Charlie.bgm = load_wav('pickup.wav')
            Charlie.bgm.set_volume(32)

    def get_bb(self):
        return self.x -45, self.y - 45, self.x+45 , self.y+45
    def Charlie_move(self):
        if self.state == self.Stop:
            self.frame = (self.frame + 1) % 1
            delay(0.03)
        elif self.state == self.RIGHT_RUN:
            self.frame = (self.frame + 2) % 4
            self.x += 3
            self.x = min(400, self.x +3)
            delay(0.05 )
        elif self.state == self.LEFT_RUN:
            self.frame = (self.frame + 2) % 4
            self.x =max(0, self.x - 3)
            delay(0.05)

        if (self.jump):
            self.y += 25
            if (self.y > 630):
                self.jump = False
        else:
            self.y = max(410, self.y - 20)

    def jumpbgm(self, number):
        self.bgm.play()

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 70, 80, self.x, self.y)
        draw_rectangle(self.x -45, self.y - 45, self.x+45 , self.y+45)
monkeyList = []
blueMonkeyList = []

def enter():
    global charlie, backgrand1, backgrand2, backgrand3, monkey_trap, line, blue_monkey_trap, monkeyList,blueMonkeyList
    
    charlie = Charlie()
    backgrand1 = BackGrand1()
    backgrand2 = BackGrand2()
    backgrand3 = BackGrand3()

    for i in range(0,10):
        monkeyList.append(Monkey_Trap(i*400,400))
    for i in range(0, 5):
        blueMonkeyList.append(Blue_Monkey_Trap(i*500,400))
    line = Line()

def exit():
    global boy, monkeyList,blueMonkeyList
    monkeyList.clear()
    blueMonkeyList.clear()

def handle_events():
    global charlie
    global backgrand1, backgrand2, backgrand3

    global running
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.key == SDLK_ESCAPE:
            backgrand1.bgm.stop()
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_UP:
                charlie.jump = True
            elif event.key == SDLK_RIGHT:
                backgrand1.state = backgrand1.Right
                backgrand2.state = backgrand2.Right
                backgrand3.state = backgrand3.Right
                charlie.state = charlie.RIGHT_RUN
            elif event.key == SDLK_LEFT:
                backgrand1.state = backgrand1.Left
                backgrand2.state = backgrand2.Left
                backgrand3.state = backgrand3.Left
                charlie.state = charlie.LEFT_RUN
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                backgrand1.state = backgrand1.Stop
                backgrand2.state = backgrand2.Stop
                backgrand3.state = backgrand3.Stop
                charlie.state = charlie.Stop
            elif event.key == SDLK_LEFT:
                backgrand1.state = backgrand1.Stop
                backgrand2.state = backgrand2.Stop
                backgrand3.state = backgrand3.Stop
                charlie.state = charlie.Stop

def update():
    charlie.Charlie_move()


def draw():

    clear_canvas()

    backgrand1.draw()
    backgrand2.draw()
    backgrand3.draw()
    backgrand1.bg_Update()
    backgrand2.bg_Update()
    backgrand3.bg_Update()
   # monkey_trap.draw()
    for monkey in monkeyList:
        monkey.draw()
        monkey.Trap_move()
        if(collide(charlie,monkey)):
            print("test")


    for bluemonkey in blueMonkeyList:
        bluemonkey.draw()
        bluemonkey.Trap_move()
        if (collide(charlie, bluemonkey)):
               print("test")


    #blue_monkey_trap.draw()
    line.draw()
    charlie.draw()
    #monkey_trap.Trap_move()
   #blue_monkey_trap.Trap_move()
    update_canvas()
    handle_events()
