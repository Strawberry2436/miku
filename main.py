import pygame
import random
game=True
pygame.init()
pygame.mixer.init()
otrezok_x=500
otrezok_speed=3
otrezki=[]
otrezok_y=random.randint(0, 450)
pygame.mixer.music.load("sekai.mp3")          #Музыко
pygame.mixer.music.play(-1)
class Floor():

    def __init__(self, width, height, color, x, y, hitbox):     #Делаем класс хитбокса
        self.width = width
        self.height = height
        self.color = color
        self.x = x
        self.y = y
        self.hitbox = hitbox
font = pygame.font.SysFont('ink free', 52, True)
game_over_text = font.render('you lozeeeee', True, "black")                 #Текст поражения
screen = pygame.display.set_mode((500, 500))
floor = Floor(width=3000, height=2000, color='black',x=0, y=480, hitbox=pygame.Rect(0, 0, 0, 0))    #пол
floor2 = Floor(width=3000, height=1,  color='black',x=0, y=0, hitbox=pygame.Rect(0, 0, 0, 0))    #потолок

bg_image = pygame.transform.scale (pygame.image.load("sprite//hi.jpg"), size=(500, 500))
anim_main_char = [pygame.transform.scale(pygame.image.load("sprite///1.png"), size= (100, 100)),
                    pygame.transform.scale(pygame.image.load("sprite///2.png"), size=(100, 100)),
                    pygame.transform.scale(pygame.image.load("sprite///3.png"), size=(100, 100)),          #Воу спрайты гг
                    pygame.transform.scale(pygame.image.load("sprite///4.png"), size=(100, 100)),
                    pygame.transform.scale(pygame.image.load("sprite///5.png"), size=(100, 100)),
                    pygame.transform.scale(pygame.image.load("sprite///6.png"), size=(100, 100)),
                    pygame.transform.scale(pygame.image.load("sprite///7.png"), size=(100, 100)),
                    pygame.transform.scale(pygame.image.load("sprite///8.png"), size=(100, 100)),
                    pygame.transform.scale(pygame.image.load("sprite///9.png"), size=(100, 100)),
                    pygame.transform.scale(pygame.image.load("sprite///10.png"), size=(100, 100)),
                    pygame.transform.scale(pygame.image.load("sprite//11.png"), size=(100, 100)),
                    pygame.transform.scale(pygame.image.load("sprite///12.png"), size=(100, 100))]
y = 0
x=0
hitbox = pygame.Rect(0, 0, 0, 0)
pressed_key = None
clock = pygame.time.Clock()
speed = 10
current_anim = 0
a_count = 0
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pressed_key = "right"
            if event.key == pygame.K_LEFT:
                pressed_key = "left"
            if event.key == pygame.K_UP:
                pressed_key = "up"                          #Управление
            if event.key == pygame.K_DOWN:
                pressed_key = "down"
            if event.key == pygame.K_SPACE:
                pressed_key = "space"
        if event.type == pygame.KEYUP:
            pressed_key = None
    if pressed_key == "right":
        a_count += 1
        if a_count > 10:
            a_count = 0  # Спрайты вправо
        current_anim = 11
        x += 2
    if pressed_key == "left":

        a_count += 1
        if a_count > 10:  # Спрайты влево
            current_anim += 1
            a_count = 0
            current_anim = 5
        x -= 2
    if pressed_key == "space":  # прыжок
        speed = -4
    if pygame.Rect.colliderect(hitbox, floor2.hitbox):  # Касание с потолком
        if speed < 0:
            speed = 0
    y += speed
    speed += 0.09

    floor.hitbox = pygame.Rect(floor.x, floor.y, floor.width, floor.height)
    floor2.hitbox = pygame.Rect(floor2.x, floor2.y, floor2.width, floor2.height)
    if pygame.Rect.colliderect(hitbox, floor.hitbox):       #Касание с полом
        if speed > 0:
            speed = 0
    if pygame.Rect.colliderect(hitbox, floor2.hitbox):  # Касание с потолком
        if speed < 0:
            speed = 0

    hitbox = pygame.Rect(x, y, 100, 100)
    screen.blit(bg_image, (0,0))
    screen.blit(anim_main_char[current_anim], (x, y))
    # pygame.draw.rect(screen, floor.color, (floor.x, floor.y, floor.width, floor.height))
    # pygame.draw.rect(screen, floor2.color, (floor2.x, floor2.y, floor2.width, floor2.height))
    clock.tick(60)
    pygame.display.update()

