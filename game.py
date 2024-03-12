import pygame

pygame.init()
pygame.mixer.init()

WIDTH = 890
HEIGHT = 750
size = (WIDTH,HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
GREY = (212, 210, 212)
BLACK = (0, 0, 0)
BLUE = (0, 97, 148)

RED = (162, 8, 0)
ORANGE = (183, 119, 0)
GREEN = (0, 127, 33)
YELLOW = (197, 199, 37)

score = 0
balls = 1
velocity = 4

paddle_width = 84
paddle_height = 20

all_sprites_list = pygame.sprite.Group()

brick_sound = pygame.mixer.Sound('./sounds/brick.wav')
paddle_sound = pygame.mixer.Sound('./sounds/paddle.wav')
wall_sound = pygame.mixer.Sound('./sounds/wall.wav')


class Brick(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()


class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels
        if self.rect.x > WIDTH - wall_width - paddle_width:
            self.rect.x = WIDTH - wall_width - paddle_width

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < wall_width:
            self.rect.x = wall_width


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.velocity = [velocity, velocity]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = self.velocity[0]
        self.velocity[1] = -self.velocity[1]


paddle = Paddle(BLUE, paddle_width, paddle_height)
paddle.rect.x = WIDTH // 2 - paddle_width // 2
paddle.rect.y = HEIGHT - 65

ball = Ball(WHITE, 10, 10)
ball.rect.x = WIDTH // 2 - 5
ball.rect.y = HEIGHT // 2 - 5

all_bricks = pygame.sprite.Group()

brick_width = 55
brick_height = 16
x_gap = 7
y_gap = 5
wall_width = 16

def bricks_position(i, j, all_bricks, all_sprites_list, color, brick_width, brick_height, wall_width, x_gap, y_gap):
    if i == 0:
        brick = Brick(color, brick_width, brick_height)
        brick.rect.x = wall_width
        brick.rect.y = 215 + j * (y_gap + brick_height)
        all_sprites_list.add(brick)
        all_bricks.add(brick)
    else:
        brick = Brick(color, brick_width, brick_height)
        brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
        brick.rect.y = 215 + j * (y_gap + brick_height)
        all_sprites_list.add(brick)
        all_bricks.add(brick)

def bricks():
    for j in range(8):
        for i in range(14):
            if j < 2:
                bricks_position(i, j, all_bricks, all_sprites_list, RED, brick_width, brick_height, wall_width, x_gap, y_gap)
            if 1 < j < 4:
                bricks_position(i, j, all_bricks, all_sprites_list, ORANGE, brick_width, brick_height, wall_width, x_gap, y_gap)
            if 3 < j < 6:
                bricks_position(i, j, all_bricks, all_sprites_list, GREEN, brick_width, brick_height, wall_width, x_gap, y_gap)
            if 5 < j < 8:
                bricks_position(i, j, all_bricks, all_sprites_list, YELLOW, brick_width, brick_height, wall_width, x_gap, y_gap)
                    
                    
brick_wall = bricks()

all_sprites_list.add(paddle)
all_sprites_list.add(ball)