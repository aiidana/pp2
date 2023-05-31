import pygame
pygame.init()

#Начинка
width = 500
height = 700
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('StackByHack')
bg=pygame.image.load("images/backround.png").convert_alpha()
boss=pygame.image.load("images/Boss.png").convert_alpha()
boss2=pygame.image.load("images/Boss2.png").convert_alpha()
boss=pygame.transform.scale(boss, (200,200))
boss2=pygame.transform.scale(boss2, (200,200))
bg=pygame.transform.scale(bg, (width,height))
effect = pygame.mixer.Sound('sound/stack.wav')
effect2 = pygame.mixer.Sound('sound/stack2.wav')
boss_sound=pygame.mixer.Sound('sound/Boss_sound.wav')
boss_sound2=pygame.mixer.Sound('sound/Boss_sound2.wav')
clock = pygame.time.Clock()

# Цвета
color = [(120, 40, 31), (148, 49, 38), (176, 58, 46), (203, 67, 53), (231, 76, 60), (236, 112, 99), (241, 148, 138), (245, 183, 177), (250, 219, 216), (253, 237, 236),
    (254, 249, 231), (252, 243, 207), (249, 231, 159), (247, 220, 111), (244, 208, 63), (241, 196, 15), (212, 172, 13), (183, 149, 11), (154, 125, 10), (125, 102, 8),
    (126, 81, 9), (156, 100, 12), (185, 119, 14), (202, 111, 30), (214, 137, 16), (243, 156, 18), (245, 176, 65), (248, 196, 113),(250, 215, 160), (253, 235, 208), 
    (254, 245, 231),(232, 246, 243), (162, 217, 206), (162, 217, 206),(115, 198, 182), (69, 179, 157), (22, 160, 133),(19, 141, 117), (17, 122, 101), (14, 102, 85),
    (11, 83, 69),(21, 67, 96), (26, 82, 118), (31, 97, 141),(36, 113, 163), (41, 128, 185), (84, 153, 199),(127, 179, 213), (169, 204, 227), (212, 230, 241),
    (234, 242, 248),(251, 238, 230), (246, 221, 204), (237, 187, 153),(229, 152, 102), (220, 118, 51), (211, 84, 0),(186, 74, 0), (160, 64, 0), (135, 54, 0)
        ]

colorIndex = 0

brickH = 10
brickW = 100

score = 0
speed = 3
flag=False
sound_flag=1
sound_flag2=1


# Характеристики блока
class Brick:
    def __init__(self, x, y, color, speed):
        self.x = x
        self.y = y
        self.w = brickW
        self.h = brickH
        self.color = color
        self.speed = speed

    def draw(self):
        pygame.draw.rect(display, self.color, (self.x, self.y, self.w, self.h))

    def move(self):
        self.x += self.speed
        if self.x > width:
            self.speed *= -1
        if self.x + self.w < 1:
            self.speed *= -1


# Блоки
class Stack:
    def __init__(self):
        global colorIndex
        self.stack = []
        self.initSize = 10
        for i in range(self.initSize):
            newBrick = Brick(width/2 - brickW/2, height - (i + 1)*brickH, color[colorIndex], 0)
            colorIndex += 1
            self.stack.append(newBrick)

    def show(self):
        for i in range(self.initSize):
            self.stack[i].draw()

    def move(self):
        for i in range(self.initSize):
            self.stack[i].move()

    def addNewBrick(self):
        global colorIndex, speed

        if colorIndex >= len(color):
            colorIndex = 0
        
        y = self.peek().y
        
        newBrick = Brick(width, y - brickH, color[colorIndex], speed)
        colorIndex += 1
        self.initSize += 1
        self.stack.append(newBrick)
        
    def peek(self):
        return self.stack[self.initSize - 1]

    def pushToStack(self):
        global brickW, score, flag
        b = self.stack[self.initSize - 2]
        b2 = self.stack[self.initSize - 1]
        if b2.x <= b.x and not (b2.x + b2.w < b.x):
            self.stack[self.initSize - 1].w = self.stack[self.initSize - 1].x + self.stack[self.initSize - 1].w - b.x
            self.stack[self.initSize - 1].x = b.x
            if self.stack[self.initSize - 1].w > b.w:
                self.stack[self.initSize - 1].w = b.w
            self.stack[self.initSize - 1].speed = 0
            score += 1
            if flag==False:
                flag=True
                effect.play()
            else:
                flag=False
                effect2.play()
        elif b.x <= b2.x <= b.x + b.w:
            self.stack[self.initSize - 1].w = b.x + b.w - b2.x
            self.stack[self.initSize - 1].speed = 0
            score += 1
            if flag==False:
                flag=True
                effect.play()
            else:
                flag=False
                effect2.play()
        elif score>=61:
            Passed()
        else:
            gameOver()
        for i in range(self.initSize):
            self.stack[i].y += brickH

        brickW = self.stack[self.initSize - 1].w

# Retake text
def gameOver():
    loop = True

    font = pygame.font.Font('beantown2.ttf', 60)
    text = font.render("RETAKE!", True, (236, 240, 241))

    textRect = text.get_rect()
    textRect.center = (width/2, height/2 - 80)

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    gameLoop()
        display.blit(text, textRect)
        
        pygame.display.update()
        clock.tick()

#Passed text

def Passed():
    loop = True

    font = pygame.font.Font('beantown2.ttf', 60)
    text = font.render("Good job!", True, (236, 240, 241))

    textRect = text.get_rect()
    textRect.center = (width/2, height/2 - 80)


    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    import Final
        display.blit(text, textRect)
        
        pygame.display.update()
        clock.tick()

# Attestation points
def showScore():
    font = pygame.font.Font('beantown2.ttf', 20)
    text = font.render("Attestation: " + str(score), True, (236, 240, 241))
    display.blit(text, (10, 10))


#Главный цикл
def gameLoop():
    global brickW, brickH, score, colorIndex, speed, sound_flag
    loop = True

    brickH = 30
    brickW = 200
    colorIndex = 0
    speed = 3

    score = 0

    stack = Stack()
    stack.addNewBrick()

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    gameLoop()
                if event.key == pygame.K_SPACE:
                    stack.pushToStack()
                stack.addNewBrick()
                

        display.blit(bg, (0,0))

        stack.move()
        stack.show()
        showScore()
        if score>=20 and score<30:
            display.blit(boss, (150,50))
            speed=5
            font_mid = pygame.font.Font('beantown2.ttf', 50)
            text = font_mid.render("MidTerm", True, (236, 240, 241))
            textRect = text.get_rect()
            textRect.center = (width/2, height/2 - 40)
            display.blit(text, textRect)
            if sound_flag==1:
                boss_sound.play()
                sound_flag=0
        elif score>=50 and score<60:
            display.blit(boss2, (150,50))
            speed=5
            font_mid = pygame.font.Font('beantown2.ttf', 50)
            text = font_mid.render("EndTerm", True, (236, 240, 241))
            textRect = text.get_rect()
            textRect.center = (width/2, height/2 - 40)
            display.blit(text, textRect)
            if sound_flag2==1:
                boss_sound.play()
                sound_flag2=0
        else:
            speed=3
        
        pygame.display.update()
        clock.tick(60)

gameLoop()
