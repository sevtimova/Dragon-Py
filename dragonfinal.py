#!/usr/bin/env python3
import os
import sys
import pygame
import time
import random
from mpi4py import MPI

os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
os.environ['DISPLAY'] = ':0.0'

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
TOTAL_WIDTH = SCREEN_WIDTH * 5
TOTAL_HEIGHT = SCREEN_HEIGHT * 4

cloud_1 = pygame.image.load('cloud1.png')
cloud_2 = pygame.image.load('cloud2.png')

pygame.display.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.mouse.set_visible(False)

class myPhoto:
	def __init__(self, name):
		self.name = name
		self.image = pygame.image.load(self.name).convert()
	def show(self):
		screen.blit(self.image, (0,0))

def myCloud_1(co1,co2):
    screen.blit(cloud_1,(co1,co2))

co1 = random.randint(0, 1000)
co2 = random.randint(0, 1000)

def myCloud_2(co3,co4):
    screen.blit(cloud_2,(co3,co4))

co3 = random.randint(0, 1000)
co4 = random.randint(0, 1000)

def myCloud_3(co5,co6):
    screen.blit(cloud_1,(co5,co6))

co5 = random.randint(0, 1000)
co6 = random.randint(0, 1000)

start_time = time.time()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Load background image
    fileName = 'cropped-' + str(rank) + '.jpg'
    twentyImages = myPhoto(fileName)
    twentyImages.show()

    co1 = random.randint(0, 1000)
    co2 = random.randint(0, 1000)
    co3 = random.randint(0, 1000)
    co4 = random.randint(0, 1000)
    co5 = random.randint(0, 1000)
    co6 = random.randint(0, 1000)

    if comm.rank == 0:
        myCloud_1(co1,co2)
        myCloud_2(co3,co4)
        myCloud_3(co5,co6)
    elif comm.rank == 1:
        myCloud_1(co1,co2)
        myCloud_3(co5,co6)
    elif comm.rank == 2:
        myCloud_1(co1,co2)
    elif comm.rank == 3:
        myCloud_1(co1,co2)
        myCloud_3(co5,co6)
    elif comm.rank == 4:
        myCloud_1(co1,co2)
        myCloud_2(co3,co4)
        myCloud_3(co5,co6)
    elif comm.rank == 5:
        myCloud_2(co3,co4)
    elif comm.rank == 6:
        pass
    elif comm.rank == 7:
        pass
    elif comm.rank == 8:
        pass
    elif comm.rank == 9:
        myCloud_1(co1,co2)
    elif comm.rank == 10:
        myCloud_1(co1,co2)
        myCloud_3(co5,co6)
    elif comm.rank == 11:
        myCloud_1(co1,co2)
    elif comm.rank == 12:
        pass
    elif comm.rank == 13:
        myCloud_2(co3,co4)
    elif comm.rank == 14:
        myCloud_1(co1,co2)
        myCloud_3(co5,co6)
    elif comm.rank == 15:
        myCloud_1(co1,co2)
        myCloud_2(co3,co4)
        myCloud_3(co5,co6)
    elif comm.rank == 16:
        myCloud_1(co1,co2)
        myCloud_3(co5,co6)
    elif comm.rank == 17:
        myCloud_1(co1,co2)
    elif comm.rank == 18:
        myCloud_1(co1,co2)
        myCloud_3(co5,co6)
    elif comm.rank == 19:
        myCloud_1(co1,co2)
        myCloud_2(co3,co4)
        myCloud_3(co5,co6)
    else: 
        pass

    pygame.time.wait(2000)
    pygame.display.update()

    # Load background image
    fileName = 'cropped-' + str(rank) + '.jpg'
    twentyImages = myPhoto(fileName)
    twentyImages.show()

    pygame.time.wait(2000)

    if time.time() - start_time > 60:
        running = False

    comm.Barrier()
    pygame.display.flip()

pygame.display.quit()