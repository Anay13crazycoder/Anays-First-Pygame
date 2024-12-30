import pygame
import math
import random
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Anays First Game")
icon = pygame.image.load('images/blueberries.png')
background = pygame.image.load('images/output (1).jpg')
mixer.music.load('sounds/latin-loop-brazil-154637.wav')
mixer.music.play(-1)
pygame.display.set_icon(icon)
hit_sound1 = mixer.Sound('sounds/laser-shot-ingame-230500.mp3')
hit_sound2 = mixer.Sound('sounds/man-shout-like-a-goat-105005.wav')
hit_sound2.set_volume(0.12)
boxsound = mixer.Sound('sounds/collect-ring-15982.mp3')
gameover_sound = mixer.Sound('sounds/yt1z.net - Dababy - LET&39;S GO sound effect.wav')
running = True

# Player 1 details
player1img = pygame.image.load('images/anay_beach_autism (1).jpg')
player1X = 300
player1Y = 500
speed1 = 0.3

# Player 2 details
player2img = pygame.image.load('images/popartemeraldporcupine (1).jpg')
player2X = 300
player2Y = 40
speed2 = 0.3

# Football1 details
football1img = pygame.image.load('images/football (1).png')
football1X = 0
football1Y = 500
speed3 = 0.31
football1state = False

# Football2 details
football2img = pygame.image.load('images/football (1).png')
football2X = 0
football2Y = 40
speed4 = 0.31
football2state = False

# Scoring
score1 = score2 = 0
font = pygame.font.Font('Rushblade.ttf', 50)
font1 = pygame.font.Font('PlayfulTime-BLBB8.ttf', 40)
font2 = pygame.font.Font('PlayfulTime-BLBB8.ttf', 120)

# Random walls
walls = []
wall = pygame.image.load('images/brick_wall (2) (1).png')
RANDOM_WALL_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(RANDOM_WALL_EVENT, 7000) #Trigger every 7 seconds

# Mystery box
boxes = []
mysterybox = pygame.image.load('images/mystery_box.jpg')
RANDOM_BOX_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(RANDOM_BOX_EVENT, 8000)  # Trigger every 8 seconds

def display():
    scored1 = font1.render('Score: ' + str(score1), True, (0, 0, 0))
    screen.blit(scored1, (700, 500))
    scored2 = font1.render('Score: ' + str(score2), True, (0, 0, 0))
    screen.blit(scored2, (700,40))
    a = font.render('P1', True, (0,0,0))
    screen.blit(a, (40,500))
    b = font.render('P2', True, (0,0,0))
    screen.blit(b, (40,40))

def game_ending(x):
    final_text = font2.render(str(x) + ' Wins!!!', True, (0, 0, 0))
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
    return dist < 27

def hit_wall(a, b, c, d):
    dist = math.sqrt(math.pow((c - a), 2) + math.pow((d - b), 2))  
    return dist < 27

while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == RANDOM_WALL_EVENT:
            wall_x = random.randint(60,830)
            wall_y = random.randint(150,350)
            walls.append((wall_x, wall_y))
        if event.type == RANDOM_BOX_EVENT:
            box_x = random.randint(60,830)
            box_y = random.randint(150,350)
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
    for i,j in walls:
        i += random.choice([-2, 2]) * 0.2  # Random x movement
        j += random.choice([-0.1, 0.1]) * 0.2  # Random y movement
        screen.blit(wall, (i,j))
        if hit_wall(football1X, football1Y, i,j):
            football1Y = 500
            football1state = False
        if hit_wall(football2X, football2Y, i, j):
            football2Y = 40
            football2state = False
            
    for index,(i,j) in enumerate(boxes):
        collision_withbox1 = hit_wall(football1X, football1Y,(i-10),j)
        collision_withbox2 = hit_wall(football2X, football2Y,(i-10),j)
        if collision_withbox1:
            boxsound.play()
            boxes.pop(index)
            speed1+=0.05
            speed3+=0.1
            football1Y = 500
            football1state = False

        if collision_withbox2:
            boxsound.play()
            boxes.pop(index)
            speed2+=0.05
            speed4+=0.1
            football2Y = 40
            football2state = False

    if score1 >= 10:
        game_ending('PLAYER1')
        pygame.display.update()
        pygame.time.delay(10000)
        break
    if score2 >= 10:
        game_ending('PLAYER2') 
        pygame.display.update()
        pygame.time.delay(10000)
        break

    for i,j in boxes:
        screen.blit(mysterybox,(i,j))

    player1(player1X, player1Y)
    player2(player2X, player2Y)
    display()
    pygame.display.update()
    
    #character selection menu,cool powerups,dynamic backgrns,timed mode