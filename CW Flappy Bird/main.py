
import pygame

pygame.init()

screen = pygame.display.set_mode((864, 936))
pygame.display.set_caption("FALLPY (FLAPPY) BIRD")

fps = 60
clock = pygame.time.Clock()

groundScroll = 0
scrollSpeed = 4

bg = pygame.image.load("img/bg.png")
ground = pygame.image.load("img/ground.png")

run = True

while run:
    clock.tick(fps)
    screen.blit(bg, (0, 0))
    screen.blit(ground, (groundScroll, 768))