from pygame import *
import random
import sys
win = display.set_mode((700, 500))
display.set_caption("Game")
BG = transform.scale(image.load("taraan2002.png"), (700, 500))
score = 0
anti_score = 0
#мусик
def FM ():
    mixer.init()
    #mixer.music.load('space.ogg')
    #mixer.music.play()


#классы
    #супер
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))
    #пули
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
    #пули
Bullets = sprite.Group()
#for en in range(0, 7):
#    bullet = Bullet('bullet.png',
#                    random.randint(1, win.get_width() - 65),
#                    -1 * random.randrange(1, 50),
#                    random.randint(1, 3))
#                        Bullets.add(bullet)
    #обычный
class Player(GameSprite):
    def  update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT]:
            self.rect.x -= speed
        if keys_pressed[K_RIGHT]:
            self.rect.x += speed
        if keys_pressed[K_UP]:
            self.rect.y -= speed
        if keys_pressed[K_DOWN]:
            self.rect.y += speed
    def fire(self):
        bullet = Bullet('traj.png', self.rect.centerx, self.rect.top, 15)
        Bullets.add(bullet)
        print('ХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХХ')       
    #враг
class Enemy(GameSprite):
    def update(self):
        global anti_score
        self.rect.y += self.speed
        if self.rect.y + 65 > win.get_height():
            anti_score += 1
            self.rect.x = random.randrange(1, win.get_width() - 65)
            self.rect.y = 1 

speed = 4
speede = 1
x1 = 200
y1 = 400
# hello worlg
x2 = 500
y2 = 200
Enemies = sprite.Group()
for en in range(0, 7):
    enemy = Enemy('traj.png',
                    random.randint(1, win.get_width() - 65),
                    -1 * random.randrange(1, 50),
                    random.randint(1, 3))
    Enemies.add(enemy)


#спрайты 
player = Player('traj.png', x1, y1, speed)
#bullet1 = transform.scale(image.load('bullet.png'), (80, 80))
player1 = transform.scale(image.load('traj.png'), (100, 100))
enemy1 = transform.scale(image.load('traj.png'), (60, 60))

#score
def show_score(choice, color, zont, size):
    font.init()
    sc_fnt = font.SysFont(zont, size)
    sc_srfc = sc_fnt.render(f"Score: {str(score)}", True, color)
    sc_rect = sc_srfc.get_rect()
    if choice == 1:
        sc_rect.midtop = (100, 15)
    else:
        sc_rect.midtop = (win.get_width() / 2, win.get_height() / 1.25)

    win.blit(sc_srfc, sc_rect)

    antsc_fnt = font.SysFont(zont, size)
    antsc_srfc = antsc_fnt.render(f"Skips: {str(anti_score)}", True, color)
    antsc_rect = antsc_srfc.get_rect()
    if choice == 1:
        print(win.get_width() / 10)
        antsc_rect.midtop = (100, 50)
    else:
        antsc_rect.midtop = (win.get_width() / 2, win.get_height() / 1.25)

    win.blit(antsc_srfc, antsc_rect)

#игровой цикл
finish = False
game = True
clock = time.Clock()
FPS = 144
FM()
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type  == KEYDOWN and e.key == K_SPACE:
            print('дааааааааааа')
            player.fire()
    if finish != True:
        win.blit(BG,(0, 0))
        Bullets.update()
        Bullets.draw(win)
        Bullets.sprites()     
        player.update()
        Enemies.update()
        player.reset()
        Enemies.draw(win)
    show_score(1, Color(255, 255, 255), 'consolas' , 20)
    display.update()
    clock.tick(FPS)