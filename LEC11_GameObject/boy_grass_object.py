from pico2d import *
import random

# Game object class here



class Grass:
    def __init__(self):
        self.img = load_image("grass.png")
        self.grassY = 30
        self.grassX = 400
    def draw(self):
        self.img.draw(self.grassX, self.grassY)
    def update(self):
        pass




class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0,7)
        self.max_frame = 8
        self.deltaPerFrame = 100
        self.dirX = random.randint(1, 10)
        self.img = load_image("run_animation.png")
    def update(self):
        self.frame = (self.frame + 1) % self.max_frame
        self.x += self.dirX
    def draw(self):
        self.img.clip_draw(self.frame*self.deltaPerFrame, 0, self.deltaPerFrame, self.deltaPerFrame, self.x, self.y)


class Zombie:
    def __init__(self):
        self.x, self.y = 100, 170
        self.frame = 0
        self.image = load_image('zombie_run_animation.png')
    def update(self):   
        self.frame = (self.frame + 1) % 10
        self.x += 5
    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h
        self.image.clip_draw(self.frame * frame_width, 0, frame_width, frame_height,
        self.x, self.y, frame_width // 2, frame_height // 2)

class Ball:
    def __init__(self):
        self.size = random.randint(0, 1)
        #self.stop

        if self.size == 0:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')

        self.x = random.randint(50, 750)
        self.y = 60
        self.v = random.randint(1, 20)
        
        
        
        self.mode = 0
       

    def update(self):
        self.y += self.v

        if self.size== 0:
            bound = 21
        else:
            bound = 41 
        if self.y  >= 600 - (bound / 2):
            self.y = 600 - 2 * (bound/2)

    
    def draw(self):
        self.image.draw(self.x, self.y)
            


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    

def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()

    for o in world:
        o.draw()

    update_canvas()

open_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
