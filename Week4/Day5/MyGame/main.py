import pygame

WIDTH, HEIGHT = 1280, 800
fps = 60

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
# bacground
img = pygame.image.load("bg.jpg").convert()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    sc.blit(img, (0, 0))

    # update screen
    pygame.display.flip()
    clock.tick(fps)
