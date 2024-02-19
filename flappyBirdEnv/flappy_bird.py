import pygame
import neat
import time
import os 
import random

WIN_WIDTH = 600
WIN_HEIGHT = 800

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("Images", "bird1.png"))),
             pygame.transform.scale2x(pygame.image.load(os.path.join("Images", "bird2.png"))),
             pygame.transform.scale2x(pygame.image.load(os.path.join("Images", "bird3.png")))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("Images", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("Images", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("Images", "bg.png")))


