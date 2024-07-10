import pgzrun
import random
from pgzhelper import*

WIDTH=1024
HEIGHT=768

player = Actor('playership2_blue')
player.pos=(WIDTH/2,HEIGHT/2)

enemy1 = 'enemyblack1'
enemy2 = 'enemygreen1'
enemy3 = 'enemyblue1'

mouse_pos=(0,0)

enemies=[]
player_lasers=[]


def update():
    player.angle=player.angle_to(mouse_pos)

    if keyboard.w:
        player.y-=5
    player.top = max(0, player.top)
    if keyboard.s:
        player.y+=5
    player.bottom = min(HEIGHT, player.bottom)
    if keyboard.a:
        player.x-=5
    player.left = max(0, player.left)
    if keyboard.d:
        player.x+=5
    player.right = min(WIDTH, player.right)
    []

    for l in player_lasers:
        l.move_forward(10)
        if l.top < 0 or l.bottom > HEIGHT or l.left < 0 or l.right > WIDTH:
            player_lasers.remove(l)
            break
        for e in enemies:
            if l.collide_pixel(e):
                enemies.remove(e)
                player_lasers.remove(l)
                break
    if random.randint(0,100) < 2:
        e=Actor(random.choice([enemy1,enemy2,enemy3]))
        direction=random.randint(0,3)
        if direction == 0:
            e.x=random.randint(0,WIDTH)
        elif direction == 1:
            e.right = WIDTH
            e.y=random.randint(0,HEIGHT)
        elif direction == 2:
            e.y=random.randint(0,HEIGHT)
            e.bottom = HEIGHT
        else:
            e.y = random.randint(0,HEIGHT)
        
        

        enemies.append(e)

    for e in enemies:
        e.point_towards(player)
        e.move_forward(3)

def on_mouse_move(pos):
    global mouse_pos
    mouse_pos=pos
def on_mouse_down():
    l=Actor('laserblue04')
    l.angle=player.angle
    l.pos=player.pos
    player_lasers.append(l)
def draw():
    screen.clear()
    player.draw()
    for e in enemies:
        e.draw()
    for l in player_lasers:
        l.draw()


pgzrun.go()