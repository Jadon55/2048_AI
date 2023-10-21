import pygame
from boxfunctions import clearBoard, getRandomBox, fillBox, moveUp, moveRight, moveDown, moveLeft, drawAll, checkLoss, checkWin
import numpy as np
import random
import copy

# make window
pygame.font.init()
window = pygame.display.set_mode((450, 550))
window.fill((187, 173, 160))
pygame.display.set_caption('2048')

# draw blank board
clearBoard(window)

boxes = np.array([
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
])
probablity = [2,2,2,2,2,2,2,2,2,4]
score = 0

def fillRandom():
    fillBox(window, getRandomBox(boxes), random.choice(probablity), boxes)

# fill starting boxes
fillRandom()
fillRandom()
run = True
prevBoard = copy.deepcopy(boxes)
# score board
my_font = pygame.font.SysFont('arial', 40, bold=True)
scoreboard = my_font.render("Score: "+str(score), False, (0, 0, 0))
window.blit(scoreboard, (50, 30))

if __name__=="__main__":
    while run:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run =False

            if event.type == pygame.KEYDOWN:
                prevBoard = copy.deepcopy(boxes)
                if event.key == pygame.K_LEFT:
                    score = moveLeft(window, boxes, score)
                if event.key == pygame.K_RIGHT:
                    score = moveRight(window, boxes, score)
                if event.key == pygame.K_UP:
                    score = moveUp(window, boxes, score)
                if event.key == pygame.K_DOWN:
                    score = moveDown(window, boxes, score)

                if not np.array_equal(prevBoard, boxes):
                    drawAll(window, boxes, score)
                    fillRandom()
                else:
                    print("Invalid")
                
                if checkLoss(boxes):
                    print("Loss")
                    my_font = pygame.font.SysFont('arial', 100, bold=True)

                    text_surface = my_font.render("You Lose", False, (0, 0, 0))
                    text_rect = text_surface.get_rect(center=(450/2, 450/2))
                    window.blit(text_surface, text_rect)
                
                if checkWin(boxes):
                    print("Win")
                    my_font = pygame.font.SysFont('arial', 100, bold=True)

                    text_surface = my_font.render("You Win", False, (0, 0, 0))
                    text_rect = text_surface.get_rect(center=(450/2, 450/2))
                    window.blit(text_surface, text_rect)
        pygame.display.update()

pygame.quit()