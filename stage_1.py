from pico2d import*
import msvcrt
import game_framework
import title_state
import random
import time
import stage_1
import stage_2

class BackGrand1:
    Right = 2
    Stop = 0

    def __init__(self):
        self.x = 400
        self.image = load_image('bg.png')
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
    Stop = 0
    def __init__(self):
        self.x = 800
        self.image = load_image('bg.png')
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
    Stop = 0
    def __init__(self):
        self.x = 1200
        self.image = load_image('bg.png')
        self.state = self.Stop
    def draw(self):
        self.image.draw(self.x,300)

    def bg_Update(self):
        if self.state == self.Right:
            self.x -= 5
            if (self.x == 800):
                self.x = 1200;
###########################################################################
class Trap:
    def __init__(self, x,y):
        self.x, self.y = x,y
        self.frame = 0
        self.image = load_image('Circus Charlie Trap.png')

    def draw(self):
        self.frame = (self.frame + 2) % 4
        #for i in range(1,10):
        self.image.clip_draw(self.frame*35, 0, 70, 220, self.x , self.y)
        #self.image.clip_draw(self.frame*100, 400, 0, 150, self.x, self.y)
        # self.image.clip_draw(self,left,bottom,width,high,x,y,w,h)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 100, self.x + 20, self.y - 90

    def Trap_move(self):
        self.x -= 8
##########################################################################
class FireTrap:
    Stop = 0
    Right = 1
    def __init__(self):
        self.x, self.y = 700, 100
        self.frame = 0
        self.image = load_image('Circus Charlie Trap.png')
        self.state = self.Stop

    def draw(self):
        self.frame = 3
        #for i in range(1,10):
        self.image.clip_draw(self.frame*70, 0, 70, 100, self.x , self.y)
        #self.image.clip_draw(self.frame*100, 400, 0, 150, self.x, self.y)
        # self.image.clip_draw(self,left,bottom,width,high,x,y,w,h)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 20, self.y + 30

    def Trap_move(self):
        if self.state == self.Right:
            self.x -= 5

class FireTrap1:
        Stop = 0
        Right = 1

        def __init__(self):
            self.x, self.y = 1100, 100
            self.frame = 0
            self.image = load_image('Circus Charlie Trap.png')
            self.state = self.Stop

        def draw(self):
            self.frame = 3
            # for i in range(1,10):
            self.image.clip_draw(self.frame * 70, 0, 70, 100, self.x, self.y)
            # self.image.clip_draw(self.frame*100, 400, 0, 150, self.x, self.y)
            # self.image.clip_draw(self,left,bottom,width,high,x,y,w,h)

        def draw_bb(self):
            draw_rectangle(*self.get_bb())

        def get_bb(self):
            return self.x - 10, self.y - 10, self.x + 20, self.y + 30

        def Trap_move(self):
            if self.state == self.Right:
                self.x -= 5

class FireTrap2:
        Stop = 0
        Right = 1

        def __init__(self):
            self.x, self.y = 1500, 100
            self.frame = 0
            self.image = load_image('Circus Charlie Trap.png')
            self.state = self.Stop

        def draw(self):
            self.frame = 3
             # for i in range(1,10):
            self.image.clip_draw(self.frame * 70, 0, 70, 100, self.x, self.y)
             # self.image.clip_draw(self.frame*100, 400, 0, 150, self.x, self.y)
            # self.image.clip_draw(self,left,bottom,width,high,x,y,w,h)

        def draw_bb(self):
              draw_rectangle(*self.get_bb())

        def get_bb(self):
            return self.x - 10, self.y - 10, self.x + 20, self.y + 30

        def Trap_move(self):
            if self.state == self.Right:
                self.x -= 5

class FireTrap3:
        Stop = 0
        Right = 1

        def __init__(self):
            self.x, self.y = 1900, 100
            self.frame = 0
            self.image = load_image('Circus Charlie Trap.png')
            self.state = self.Stop

        def draw(self):
            self.frame = 3
            # for i in range(1,10):
            self.image.clip_draw(self.frame * 70, 0, 70, 100, self.x, self.y)
            # self.image.clip_draw(self.frame*100, 400, 0, 150, self.x, self.y)
            # self.image.clip_draw(self,left,bottom,width,high,x,y,w,h)

        def draw_bb(self):
            draw_rectangle(*self.get_bb())

        def get_bb(self):
            return self.x - 10, self.y - 10, self.x + 20, self.y + 30

        def Trap_move(self):
            if self.state == self.Right:
                self.x -= 5

class FireTrap4:
        Stop = 0
        Right = 1

        def __init__(self):
            self.x, self.y = 2300, 100
            self.frame = 0
            self.image = load_image('Circus Charlie Trap.png')
            self.state = self.Stop

        def draw(self):
            self.frame = 3
            # for i in range(1,10):
            self.image.clip_draw(self.frame * 70, 0, 70, 100, self.x, self.y)
            # self.image.clip_draw(self.frame*100, 400, 0, 150, self.x, self.y)
            # self.image.clip_draw(self,left,bottom,width,high,x,y,w,h)

        def draw_bb(self):
            draw_rectangle(*self.get_bb())

        def get_bb(self):
            return self.x - 10, self.y - 10, self.x + 20, self.y + 30

        def Trap_move(self):
            if self.state == self.Right:
                self.x -= 5

class FireTrap5:
        Stop = 0
        Right = 1

        def __init__(self):
            self.x, self.y = 2700, 100
            self.frame = 0
            self.image = load_image('Circus Charlie Trap.png')
            self.state = self.Stop

        def draw(self):
            self.frame = 3
            # for i in range(1,10):
            self.image.clip_draw(self.frame * 70, 0, 70, 100, self.x, self.y)
            # self.image.clip_draw(self.frame*100, 400, 0, 150, self.x, self.y)
            # self.image.clip_draw(self,left,bottom,width,high,x,y,w,h)

        def draw_bb(self):
            draw_rectangle(*self.get_bb())

        def get_bb(self):
            return self.x - 10, self.y - 10, self.x + 20, self.y + 30

        def Trap_move(self):
            if self.state == self.Right:
                self.x -= 5
##################################################################################
class Finsh:
    Stop = 0
    Right = 1
    def __init__(self):
        self.x, self.y = 3000, 100
        self.frame = 0
        self.image = load_image('Finsh.png')
        self.state = self.Stop

    def draw(self):
        self.frame = 0
        self.image.clip_draw(self.frame * 70, 0, 150, 100, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def Trap_move(self):
        if self.state == self.Right:
            self.x -= 5
################################################################################
class Lion:
    bgm = None
    Stop, LEFT_RUN, RIGHT_RUN= 0 ,1 ,2
    def __init__(self):
        self.x, self.y = 200, 80
        self.frame = 0
        self.image = load_image('Circus Charlie Lion.png')
        self.jump = False
        self.state = self.Stop

        if Lion.bgm == None:
            Lion.bgm = load_wav('pickup.wav')
            Lion.bgm.set_volume(32)

    def jumpbgm(self, number):
        self.bgm.play()

    def draw(self):
        self.image.clip_draw(self.frame*175, 0, 175, 60, self.x, self.y)

    def Lion_move(self):
        if self.state == self.Stop:
            self.frame = 2
            delay(0.06)
        elif self.state == self.RIGHT_RUN:
            self.frame = (self.frame +2) % 4
            self.x = min(500, self.x + 7)
            delay(0.06)
        elif self.state == self.LEFT_RUN:
            self.frame = (self.frame + 2) % 4
            self.x =max(0, self.x - 7)
            delay(0.06)

        if(self.jump):
            self.frame = (self.frame + 1) % 1
            self.y += 50
            self.x += 20
            delay(0.03)
            if(self.y > 200):
                self.jump = False
        else:
            self.y = max(80, self.y - 8)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 50, self.y - 20, self.x + 80, self.y + 20


class Charlie:
    Stop, LEFT_RUN, RIGHT_RUN = 0, 1, 2
    def __init__(self):
        self.x, self.y = 200, 140
        self.frame = 0
        self.image = load_image('Circus Charlie.png')
        self.jump = False
        self.state = self.Stop

    def Charlie_move(self):
        if self.state == self.Stop:
            self.frame = (self.frame + 1) % 1
        elif self.state == self.RIGHT_RUN:
            #self.frame = (self.frame + 2) % 4
            self.x = min(500, self.x + 7)

        elif self.state == self.LEFT_RUN:
           # self.frame = (self.frame + 2) % 4
            self.x =max(0, self.x - 7)

        if (self.jump):
            self.y += 50
            self.x += 20
            if (self.y > 260):
                self.jump = False
        else:
            self.y = max(140, self.y - 8)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 70, 80, self.x, self.y)
        #self.image.clip_draw(self,left,bottom,width,high,x,y,w,h)

class Gameover:
    Off , On = 0 ,1
    def __init__(self):
        self.x, self.y = 400, 250
        self.frame = 0
        self.image = load_image('Game_Over.png')
        self.state = self.Off

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 500, 400, self.x, self.y)
        return


def collide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def Finshcollide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

TrapList = []
FireTrapList = []
def enter():
    global charlie, backgrand1, backgrand2, backgrand3, lion, go, finsh, fire, fire1, fire2, fire3, fire4, fire5
    charlie = Charlie()
    backgrand1 = BackGrand1()
    backgrand2 = BackGrand2()
    backgrand3 = BackGrand3()
    fire = FireTrap()
    fire1 = FireTrap1()
    fire2 = FireTrap2()
    fire3 = FireTrap3()
    fire4 = FireTrap4()
    fire5 = FireTrap5()
    lion = Lion()
    finsh = Finsh()
    go = Gameover()

    for i in range(1,50):
        TrapList.append(Trap(i*650,260))

def exit():
    global boy


def handle_events():
    global lion
    global charlie
    global backgrand1, backgrand2, backgrand3
    global finsh, go, fire, fire1, fire2, fire3, fire4, fire5, fire6

    global running
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.key == SDLK_ESCAPE:
            backgrand1.bgm.stop()
            game_framework.change_state(title_state)
        elif event.type == SDLK_SPACE and go.state == go.On:
            game_framework.change_state(stage_1)
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_UP:
                lion.jump = True
                charlie.jump = True
                lion.jumpbgm(1)
            elif event.key == SDLK_RIGHT:
                backgrand1.state = backgrand1.Right
                backgrand2.state = backgrand2.Right
                backgrand3.state = backgrand3.Right
                fire.state = fire.Right
                fire1.state = fire1.Right
                fire2.state = fire2.Right
                fire3.state = fire3.Right
                fire4.state = fire4.Right
                fire5.state = fire5.Right
                finsh.state = finsh.Right
                lion.state = lion.RIGHT_RUN
                charlie.state = charlie.RIGHT_RUN
            elif event.key == SDLK_LEFT:
                lion.state = lion.LEFT_RUN
                charlie.state = charlie.LEFT_RUN
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                backgrand1.state = backgrand1.Stop
                backgrand2.state = backgrand2.Stop
                backgrand3.state = backgrand3.Stop
                fire.state = fire.Stop
                fire1.state = fire1.Stop
                fire2.state = fire2.Stop
                fire3.state = fire3.Stop
                fire4.state = fire4.Stop
                fire5.state = fire5.Stop
                finsh.state = finsh.Stop
                lion.state = lion.Stop
                charlie.state = charlie.Stop
            elif event.key == SDLK_LEFT:
                backgrand1.state = backgrand1.Stop
                backgrand2.state = backgrand2.Stop
                backgrand3.state = backgrand3.Stop
                lion.state = lion.Stop
                charlie.state = charlie.Stop

def update():
    charlie.Charlie_move()
    lion.Lion_move()
    backgrand1.bg_Update()
    backgrand2.bg_Update()
    backgrand3.bg_Update()

def draw():
    clear_canvas()
    backgrand1.draw()
    backgrand2.draw()
    backgrand3.draw()

    #for fire in FireTrapList:
        #fire.draw()
        #fire.Trap_move()
        #if (collide(charlie, fire)):
            #print("test")
      #  elif (collide(Lion, fire)):
#            print("test")

    charlie.draw()
    #charlie.draw_bb()
    lion.draw()
    #lion.draw_bb()

    finsh.draw()
    finsh.draw_bb()
    finsh.Trap_move()

    for trap in TrapList:
        trap.draw()
        trap.Trap_move()
        if (collide(charlie, trap)):
            print("charlie불기둥 충돌")
           # Gameover().draw()
          #  go.state = go.On
            #time.sleep(1)
        elif(collide(lion, trap)):
              print("lion불기둥 충돌")

    fire.draw()
    fire.draw_bb()
    fire.Trap_move()
    if (collide(charlie, fire)):
        print("charli불항아리 충돌")
    elif (collide(lion, fire)):
        print("lion불항아리 충돌")

    fire1.draw()
    fire1.draw_bb()
    fire1.Trap_move()
    if (collide(charlie, fire1)):
        print("charli불항아리 충돌")
    elif (collide(lion, fire1)):
        print("lion불항아리 충돌")

    fire2.draw()
    fire2.draw_bb()
    fire2.Trap_move()
    if (collide(charlie, fire2)):
        print("charli불항아리 충돌")
    elif (collide(lion, fire2)):
        print("lion불항아리 충돌")

    fire3.draw()
    fire3.draw_bb()
    fire3.Trap_move()
    if (collide(charlie, fire3)):
        print("charli불항아리 충돌")
    elif (collide(lion, fire3)):
        print("lion불항아리 충돌")

    fire4.draw()
    fire4.draw_bb()
    fire4.Trap_move()
    if (collide(charlie, fire4)):
        print("charli불항아리 충돌")
    elif (collide(lion, fire4)):
        print("lion불항아리 충돌")

    fire5.draw()
    fire5.draw_bb()
    fire5.Trap_move()
    if (collide(charlie, fire5)):
        print("charli불항아리 충돌")
    elif (collide(lion, fire5)):
        print("lion불항아리 충돌")

    handle_events()


    if Finshcollide(lion,finsh):
        game_framework.change_state(stage_2)

    update_canvas()



