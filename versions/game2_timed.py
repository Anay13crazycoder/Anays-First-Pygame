import pygame
import math
import random
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Anays First game(TIMED)")
icon = pygame.image.load('images/blueberries.png')
background = pygame.image.load('images/fire_land (1).jpg')
mixer.music.load('sounds/latin-loop-brazil-154637.wav')
mixer.music.play(-1)
pygame.display.set_icon(icon)
hit_sound1 = mixer.Sound('sounds/laser-shot-ingame-230500.mp3')
hit_sound2 = mixer.Sound('sounds/man-shout-like-a-goat-105005.wav')
hit_sound2.set_volume(0.12)
boxsound = mixer.Sound('sounds/collect-ring-15982.mp3')
gameover_sound = mixer.Sound('sounds/yt1z.net - Dababy - LET&39;S GO sound effect.wav')

#character options: 
a=pygame.image.load('playable_characters/anay_beach_autism (1).jpg')
b=pygame.image.load('playable_characters/rekkit (1).jpg')
c=pygame.image.load('playable_characters/lf (1).jpg')
d=pygame.image.load('playable_characters/whirlpool_man (1).jpg')

# Player 1 details
player1img = pygame.image.load('playable_characters/popartemeraldporcupine (1).jpg')
player1X = 300
player1Y = 500
speed1 = 0.3

# Player 2 details
player2img = pygame.image.load('playable_characters/ronaldo2014.jpg')
player2X = 300
player2Y = 40
speed2 = 0.3

# Football1 details
football1img = pygame.image.load('images/bullet (1).png')
football1X = 0
football1Y = 500
speed3 = 0.31
football1state = False

# Football2 details
football2img = pygame.image.load('images/bullet (2).png')
football2X = 0
football2Y = 40
speed4 = 0.31
football2state = False

# Scoring
score1 = score2 = 0
font = pygame.font.Font('texts/Rushblade.ttf', 50)
font1 = pygame.font.Font('texts/PlayfulTime-BLBB8.ttf', 40)
font2 = pygame.font.Font('texts/PlayfulTime-BLBB8.ttf', 120)

# Random walls
walls = []
wall = pygame.image.load('images/brick_wall (2) (1).png')
RANDOM_WALL_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(RANDOM_WALL_EVENT, 12000)  # Trigger every 12 seconds

# Mystery box
boxes = []
mysterybox = pygame.image.load('images/mystery_box.jpg')
RANDOM_BOX_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(RANDOM_BOX_EVENT, 9000)  # Trigger every 9 seconds

def display():
    scored1 = font1.render('Score: ' + str(score1), True, (255,255,255))
    screen.blit(scored1, (700, 500))
    scored2 = font1.render('Score: ' + str(score2), True, (255,255,255))
    screen.blit(scored2, (700, 40))
    a = font.render('P1', True, (255,255,255))
    screen.blit(a, (40, 500))
    b = font.render('P2', True, (255,255,255))
    screen.blit(b, (40, 40))


def game_ending(x):
    final_text = font2.render(f'{x} Wins!!!', True, (255,255,255))
    screen.blit(final_text, (130, 230))
    gameover_sound.play(-1)


def player1(x, y):
    screen.blit(player1img, (x, y))

def player2(x, y):
    screen.blit(player2img, (x, y))


def shoot_theball1(x, y):
    global football1state
    football1state = True
    screen.blit(football1img, (x + 16, y + 10))


def shoot_theball2(x, y):
    global football2state
    football2state = True
    screen.blit(football2img, (x + 16, y - 10))


def hit_player(a, b, c, d):
    dist = math.sqrt(math.pow((c - a), 2) + math.pow((d - b), 2))
    return dist < 28


def hit_wall(a, b, c, d):
    dist = math.sqrt(math.pow((c - a), 2) + math.pow((d - b), 2))
    return dist < 23.5

selection=True
selection2=False
running=False
font3 = pygame.font.SysFont('chalkduster.ttf', 60)
background2=pygame.image.load('images/rainbowimage (1).jpg')
while selection:
    screen.blit(background2, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            selection = running= False
    keys = pygame.key.get_pressed()    
    if keys[pygame.K_1]:
        player1img=a
        selection2=True
        selection=False
    if keys[pygame.K_2]:
        player1img=b
        selection2=True
        selection=False
    if keys[pygame.K_3]:
        player1img=c
        selection2=True
        selection=False
    if keys[pygame.K_4]:
        player1img=d
        selection2=True
        selection=False
    if keys[pygame.K_5]:
        selection2=True
        selection=False

    screen.blit(a, (50, 400))
    screen.blit(b, (250, 400))
    screen.blit(c, (450, 400))
    screen.blit(d, (650, 400))
    screen.blit(player1img,(800, 400))

    printer = font3.render('SELECT CHARACTER 1,2,3,4 OR 5 FOR P1', True, (0,0,0))
    screen.blit(printer, (30,270))    
    pygame.display.update()

while selection2:
    screen.blit(background2, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            selection = running= False
    keys = pygame.key.get_pressed()    
    if keys[pygame.K_a]:
        player2img=a
        running=True
        selection2=False
    if keys[pygame.K_b]:
        player2img=b
        running=True
        selection2=False
    if keys[pygame.K_c]:
        player2img=c
        running=True
        selection2=False
    if keys[pygame.K_d]:
        player2img=d
        running=True
        selection2=False
    if keys[pygame.K_e]:
        running=True
        selection2=False

    screen.blit(a, (50, 400))
    screen.blit(b, (250, 400))
    screen.blit(c, (450, 400))
    screen.blit(d, (650, 400))
    screen.blit(player2img,(800, 400))
        
    printer = font3.render('SELECT CHARACTER a,b,c,d,e FOR P2', True, (255,255,255))
    screen.blit(printer, (30,270))    
    pygame.display.update()

# Timer
time_limit = 60
clock = pygame.time.Clock()
game_time = pygame.time.get_ticks() 

while running:
    screen.blit(background, (0, 0))
    current_time = (pygame.time.get_ticks() - game_time) / 1000  # Calculate elapsed time ,video in backgrnd
    if current_time >= time_limit:
        winner = 'PLAYER1' if score1 > score2 else 'PLAYER2' if score2 > score1 else 'NOBODY'
        game_ending(winner)
        pygame.display.update()
        pygame.time.delay(11000)
        running = False
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == RANDOM_WALL_EVENT:
            wall_x = random.randint(60, 830)
            wall_y = random.randint(150, 350)
            walls.append([wall_x, wall_y])
        if event.type == RANDOM_BOX_EVENT:
            box_x = random.randint(60, 830)
            box_y = random.randint(150, 350)
            boxes.append((box_x, box_y))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player1X > 0:
        player1X -= speed1
    if keys[pygame.K_RIGHT] and player1X < 836:
        player1X += speed1
    if keys[pygame.K_a] and player2X > 0:
        player2X -= speed2
    if keys[pygame.K_d] and player2X < 836:
        player2X += speed2
    if keys[pygame.K_UP] and not football1state:
        football1X = player1X
        shoot_theball1(football1X, football1Y)
    if keys[pygame.K_w] and not football2state:
        football2X = player2X
        shoot_theball2(football2X, football2Y)

    if football1Y <= -10:
        football1Y = 500
        football1state = False
    if football1state:
        shoot_theball1(football1X, football1Y)
        football1Y -= speed3
    if football2Y >= 610:
        football2Y = 40
        football2state = False
    if football2state:
        shoot_theball2(football2X, football2Y)
        football2Y += speed4

    collision1 = hit_player(player2X, player2Y, football1X, football1Y)
    collision2 = hit_player(player1X, player1Y, football2X, football2Y)
    if collision1:
        hit_sound1.play()
        football1Y = 500
        football1state = False
        score1 += 1
    if collision2:
        hit_sound2.play()
        football2Y = 40
        football2state = False
        score2 += 1
    for wall_data in walls:
        wall_data[0] += random.choice([-2, 2]) * 0.2  # Random x movement
        wall_data[1] += random.choice([-0.1, 0.1]) * 0.2  # Random y movement
        screen.blit(wall, (wall_data[0], wall_data[1]))
        if hit_wall(football1X, football1Y, wall_data[0], wall_data[1]):
            football1Y = 500
            football1state = False
        if hit_wall(football2X, football2Y, wall_data[0], wall_data[1]):
            football2Y = 40
            football2state = False

    for index, (i,j) in enumerate(boxes):
        collision_withbox1 = hit_wall(football1X, football1Y, i,j)
        collision_withbox2 = hit_wall(football2X, football2Y, i,j)

        if collision_withbox1: 
            boxsound.play()
            boxes.pop(index)
            p=random.randint(1,3) # 1 2 3
            print(p)
            if p==1:
                speed1 += 0.2
            elif p==2:
                speed3 += 0.15
            elif p==3:
                speed1-= 0.1

            football1Y = 500
            football1state = False

        if collision_withbox2:
            boxsound.play()
            boxes.pop(index)
            p=random.randint(1,3)
            print(p)
            if p==1:
                speed2 += 0.2
            elif p==2:
                speed4 += 0.15
            elif p==3:
                speed2-= 0.1
            football2Y = 40
            football2state = False

    timer_display = font1.render(f'Time: {int(time_limit - current_time)}', True, (255,255,255))
    screen.blit(timer_display, (380, 10))
    
    player1(player1X, player1Y)
    player2(player2X, player2Y)
    
    for i,j in boxes:
        screen.blit(mysterybox, (i,j))
    display()
    pygame.display.flip()