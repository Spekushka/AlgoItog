from pygame import *
from random import randint

win_width = 700
win_height = 500
width = 700
height = 500
window = display.set_mode(
    (win_width, win_height)
)
display.set_caption('Catching Fruits')
background = transform.scale(
    image.load('White_Background.jpg'),
    (win_width, win_height)
)
fruits_sprite = {
    1 : 'Color_Apple.png',
    2 : 'Color_Pear.png',
    3 : 'Color_Strawberry.png'
}
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
Player = Player('Color_Player.png', 280, 420, 7, 80, 80)
fruits = sprite.Group()
for i in range(1,5):
    fruit_sprite = randint(1,3)
    fruit = Fruits(fruits_sprite.get(fruit_sprite), randint(65,700-65),-40,randint(3,5),65,65)
    fruit.add(fruits)

clock = time.Clock()
FPS = 60
run = True
finish = False

speed_x = 3
speed_y = 3
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(background, (0, 0))
    fruits.update()
    fruits.draw(window)
    Player.update()
    Player.reset()
    display.update()
    clock.tick(FPS)


