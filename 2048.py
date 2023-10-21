import pygame
from boxfunctions import clearBoard, getRandomBox, fillBox, moveUp, moveRight, moveDown, moveLeft, drawAll, checkLoss, checkWin
import numpy as np
import random
import copy
import os
import neat

def main(genomes, config):
    for i, genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)

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

        while run:
            for event in pygame.event.get():
                output = net.activate((score, boxes[0][0], boxes[0][1], boxes[0][2], boxes[0][3],
                                              boxes[1][0], boxes[1][1], boxes[1][2], boxes[1][3],
                                              boxes[2][0], boxes[2][1], boxes[2][2], boxes[2][3],
                                              boxes[3][0], boxes[3][1], boxes[3][2], boxes[3][3]))
                decision = output.index(max(output))
                print(decision)

                if event.type == pygame.QUIT:
                    run =False
                    pygame.quit()

                
                prevBoard = copy.deepcopy(boxes)
                if decision == 0:
                    score = moveLeft(window, boxes, score)
                elif decision == 1:
                    score = moveRight(window, boxes, score)
                elif decision == 2:
                    score = moveUp(window, boxes, score)
                else:
                    score = moveDown(window, boxes, score)

                if not np.array_equal(prevBoard, boxes):
                    genome.fitness += 1
                    drawAll(window, boxes, score)
                    fillRandom()
                else:
                    genome.fitness -= 1
                    print("Invalid")
                
                if checkLoss(boxes):
                    run = False
                    print("Loss")
                    print(score)
                    my_font = pygame.font.SysFont('arial', 100, bold=True)

                    text_surface = my_font.render("You Lose", False, (0, 0, 0))
                    text_rect = text_surface.get_rect(center=(450/2, 450/2))
                    window.blit(text_surface, text_rect)
                    return genome
                
                if checkWin(boxes):
                    print("Win")
                    print(score)
                    my_font = pygame.font.SysFont('arial', 100, bold=True)

                    text_surface = my_font.render("You Win", False, (0, 0, 0))
                    text_rect = text_surface.get_rect(center=(450/2, 450/2))
                    window.blit(text_surface, text_rect)
            pygame.display.update()
        pygame.quit()

def run(config_file):
    # load config file
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    # create population based on the config file
    p = neat.Population(config)

    # add reported to get updates in the terminal
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    # Run for up to 10 generations.
    winner = p.run(main, 10)

    # Display the winning genome.
    print('\nBest genome:\n{!s}'.format(winner))

if __name__=="__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-neat.txt')
    run(config_path)