import pygame, random
from pygame.locals import *
from sys import exit

def on_grid_random():
    x = random.randint(10,590)
    y = random.randint(10,590)
    return (x//10 * 10, y//10 * 10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


def reiniciar_jogo():
    pontos = 0
    snake = [(200, 200), (210, 200), (220, 200)]
    snake_skin = pygame.Surface((10,10))
    snake_skin.fill((255,255,0))
    apple_pos = on_grid_random()
    apple = pygame.Surface((10,10))
    apple.fill((255,0,0))
    perdeu = False


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()

pygame.mixer.music.set_volume(0.1)
musica_de_funco = pygame.mixer.music.load('Snake/BRIGHT_MOTION_p_brejean_HIB77_LC06881.mp3')
pygame.mixer.music.play(-1)

som_colisao = pygame.mixer.Sound('salamisound-4724461-sfx-collect-gather-2.mp3')

tela = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake2')

snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,0))

apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

pontos = 0
fonte = pygame.font.SysFont('arial', 40, bold=True, italic=True)

perdeu = False

my_direction = LEFT

clock = pygame.time.Clock()

while True:
    clock.tick(20)

    mensagem = f'pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255,255,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))
        pontos +=1
        som_colisao.play()
    tela.blit(texto_formatado, (10,40))

    if snake.count(snake) > 1:
        fonte2 = pygame.font.pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game Over! Pressione a tecla r para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, (250,69,0))

        perdeu = True
        while perdeu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == Quit:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                        if event.key == K_r:
                            reiniciar_jogo()
            tela.blit(texto_formatado, on_grid_random())
            pygame.display.update()

    for i in range(len(snake) -1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    tela.fill((0,0,0))
    tela.blit(apple, apple_pos)
    for pos in snake:
        tela.blit(snake_skin, pos)

    pygame.display.update()