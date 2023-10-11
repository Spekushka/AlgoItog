from pygame import *
from random import randint,choice

win_width = 700
win_height = 500
width = 700
height = 500
window = display.set_mode(
    (win_width, win_height)
)
display.set_caption('Catching Fruits')
background = transform.scale(
    image.load('bg.png'),
    (win_width, win_height)
)
fruits_sprite = ['Color_Apple.png','Color_Pear.png','Color_Strawberry.png']
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render("ТЫ ПРОИГРАЛ!", True, (180, 0, 0))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
class Fruits(GameSprite):
    def update(self):
        self.rect.y+=self.speed
        global lost
        if self.rect.y > height:
            self.rect.x = randint(80, width-80)
            self.rect.y = 0
    def die(self):
            self.kill()
player = Player('Color_Player.png', 280, 420, 10, 80, 80)
bombs=sprite.Group()
for i in range(2):
    bomb = Fruits('Color_Bomb.png', randint(65,700-65),-40,randint(1,5), 65, 65)
    bombs.add(bomb)
fruits = sprite.Group()
for i in range(5):
    fruit = Fruits(choice(fruits_sprite), randint(65,700-65),-40,randint(2,5), 65, 65)
    fruits.add(fruit)


clock = time.Clock()
FPS = 60
run = True
finish = False
score = 0
speed_x = 3
speed_y = 3
font.init()
font1 = font.SysFont('Arial', 80)
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))
font2 = font.SysFont('Arial', 40)
health = 3
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False


    if finish != True:
        window.blit(background, (0, 0))
        if sprite.spritecollide(player, bombs, True):
            health-=1
            bomb = Fruits('Color_Bomb.png', randint(65,700-65),-40,randint(1,5), 65, 65)
            bombs.add(bomb)
        if health ==0:
            finish = True
            window.blit(lose, (200, 200))
        if score >= 100:
            finish = True
            window.blit(win, (200, 200))
        if sprite.spritecollide(player, fruits, True):
            score += 1
            print(score)
            fruit = Fruits(choice(fruits_sprite), randint(65,700-65),-40,randint(2,5), 65, 65)
            fruits.add(fruit)


    



        
        bombs.update()
        bombs.draw(window)
        fruits.update()
        fruits.draw(window)
        player.update()
        player.reset()

        text_win = font2.render('Счет:' + str(score), 1, (255, 255, 255))
        window.blit(text_win,(5, 40))
        text_health = font2.render('Жизни:' + str(health), 1, (255, 255, 255))
        window.blit(text_health,(5, 90))
  
        clock.tick(FPS)
    display.update()


