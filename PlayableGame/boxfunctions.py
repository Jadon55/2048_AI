import pygame
import random
import numpy as np

boxes_pos = (
        [[10, 10, 100, 100], [120, 10, 100, 100], [230, 10, 100, 100], [340, 10, 100, 100]],
        [[10, 120, 100, 100], [120, 120, 100, 100], [230, 120, 100, 100], [340, 120, 100, 100]],
        [[10, 230, 100, 100], [120, 230, 100, 100], [230, 230, 100, 100], [340, 230, 100, 100]],
        [[10, 340, 100, 100], [120, 340, 100, 100], [230, 340, 100, 100], [340, 340, 100, 100]]
    )

# adjust pos for points bar
for row in boxes_pos:
    for box in row:
        box[1] += 100

colors = {
   2 : (238, 228, 218),
   4 : (237, 224, 200),
   8 : (242, 177, 121),
   16 : (245, 149, 99),
   32 : (246, 124, 95),
   64 : (246, 94, 59),
   128 : (237, 207, 114),
   256 : (237, 204, 97),
   512 : (237, 200, 80),
   1024 : (237, 197, 63),
   2048 : (237, 194, 46)
}

def clearBoard(window):
    window.fill((187, 173, 160))
    for row in boxes_pos:
        for box in row:
            pygame.draw.rect(window, (204, 192, 179),
                                box, 0)

def getRandomBox(boxes):
    list = []
    board = boxes.flatten()
    for i in range(len(board)):
        if board[i] == 0:
            list.append(i)
    return(random.choice(list))

def fillBox(window, pos, value, boxes):
    d1 = 0

    if pos > 11:
        d1 = 3
        pos = pos-12
    elif pos > 7:
        d1 = 2
        pos = pos-8
    elif pos > 3:
        d1 = 1
        pos = pos-4

    boxes[d1][pos] = value
    pygame.draw.rect(window, colors[value],
                                boxes_pos[d1][pos], 0)
    
    my_font = pygame.font.SysFont('arial', 40, bold=True)

    text_surface = my_font.render(str(value), False, (0, 0, 0))
    text_rect = text_surface.get_rect(center=((boxes_pos[d1][pos][0]+50), (boxes_pos[d1][pos][1]+50)))
    window.blit(text_surface, text_rect)

def moveUp(window, boxes, score):
    # 2nd row
    for i in range(4):
        # combine
        if boxes[1][i] != 0 and boxes[0][i] == boxes[1][i]:
            # adjust boxes array
            score += boxes[1][i]+boxes[0][i]
            boxes[0][i] = boxes[1][i]+boxes[0][i]
            boxes[1][i] = 0
        # move up
        elif boxes[1][i] != 0 and boxes[0][i] == 0:
            # adjust boxes array
            boxes[0][i] = boxes[1][i]
            boxes[1][i] = 0
    # 3rd row
    for i in range(4):
        # combine (into row 2)
        if boxes[2][i] != 0 and boxes[1][i] == boxes[2][i]:
            # adjust boxes array
            score += boxes[2][i]+boxes[1][i]
            boxes[1][i] = boxes[2][i]+boxes[1][i]
            boxes[2][i] = 0
        # combine (into row 1)
        elif boxes[2][i] != 0 and boxes[0][i] == boxes[2][i] and boxes[1][i] == 0:
            # adjust boxes array
            score += boxes[2][i]+boxes[0][i]
            boxes[0][i] = boxes[2][i]+boxes[0][i]
            boxes[2][i] = 0

        # move up (into row 1)
        elif boxes[2][i] != 0 and boxes[0][i] == 0 and boxes[1][i] == 0:
            # adjust boxes array
            boxes[0][i] = boxes[2][i]
            boxes[2][i] = 0
        # move up (into row 2)
        elif boxes[2][i] != 0 and boxes[1][i] == 0:
            # adjust boxes array
            boxes[1][i] = boxes[2][i]
            boxes[2][i] = 0
    # 4th row
    for i in range(4):
        # combine (into row 3)
        if boxes[3][i] != 0 and boxes[2][i] == boxes[3][i]:
            # adjust boxes array
            score += boxes[3][i]+boxes[2][i]
            boxes[2][i] = boxes[3][i]+boxes[2][i]
            boxes[3][i] = 0
        # combine (into row 2)
        elif boxes[3][i] != 0 and boxes[1][i] == boxes[3][i] and boxes[2][i] == 0:
            # adjust boxes array
            score += boxes[3][i]+boxes[1][i]
            boxes[1][i] = boxes[3][i]+boxes[1][i]
            boxes[3][i] = 0
        # combine (into row 1)
        elif boxes[3][i] != 0 and boxes[0][i] == boxes[3][i] and boxes[2][i] == 0 and boxes[1][i] == 0:
            # adjust boxes array
            score += boxes[3][i]+boxes[0][i]
            boxes[0][i] = boxes[3][i]+boxes[0][i]
            boxes[3][i] = 0

        # move up (into row 1)
        elif boxes[3][i] != 0 and boxes[0][i] == 0 and boxes[2][i] == 0 and boxes[1][i] == 0:
            # adjust boxes array
            boxes[0][i] = boxes[3][i]
            boxes[3][i] = 0
        # move up (into row 2)
        elif boxes[3][i] != 0 and boxes[1][i] == 0 and boxes[2][i] == 0:
            # adjust boxes array
            boxes[1][i] = boxes[3][i]
            boxes[3][i] = 0
        # move up (into row 3)
        elif boxes[3][i] != 0 and boxes[2][i] == 0:
            # adjust boxes array
            boxes[2][i] = boxes[3][i]
            boxes[3][i] = 0
    return score

def moveDown(window, boxes, score):
    # 3rd row
    for i in range(4):
        # combine
        if boxes[2][i] != 0 and boxes[3][i] == boxes[2][i]:
            # adjust boxes array
            score += boxes[2][i]+boxes[3][i]
            boxes[3][i] = boxes[2][i]+boxes[3][i]
            boxes[2][i] = 0
        # move up
        elif boxes[2][i] != 0 and boxes[3][i] == 0:
            # adjust boxes array
            boxes[3][i] = boxes[2][i]
            boxes[2][i] = 0
    # 2nd row
    for i in range(4):
        # combine (into row 3)
        if boxes[1][i] != 0 and boxes[2][i] == boxes[1][i]:
            # adjust boxes array
            score += boxes[1][i]+boxes[2][i]
            boxes[2][i] = boxes[1][i]+boxes[2][i]
            boxes[1][i] = 0
        # combine (into row 4)
        elif boxes[1][i] != 0 and boxes[3][i] == boxes[1][i] and boxes[2][i] == 0:
            # adjust boxes array
            score += boxes[1][i]+boxes[3][i]
            boxes[3][i] = boxes[1][i]+boxes[3][i]
            boxes[1][i] = 0

        # move down (into row 4)
        elif boxes[1][i] != 0 and boxes[3][i] == 0 and boxes[2][i] == 0:
            # adjust boxes array
            boxes[3][i] = boxes[1][i]
            boxes[1][i] = 0
        # move down (into row 3)
        elif boxes[1][i] != 0 and boxes[2][i] == 0:
            # adjust boxes array
            boxes[2][i] = boxes[1][i]
            boxes[1][i] = 0
    # 1strow
    for i in range(4):
        # combine (into row 3)
        if boxes[0][i] != 0 and boxes[1][i] == boxes[0][i]:
            # adjust boxes array
            score += boxes[0][i]+boxes[1][i]
            boxes[1][i] = boxes[0][i]+boxes[1][i]
            boxes[0][i] = 0
        # combine (into row 2)
        elif boxes[0][i] != 0 and boxes[2][i] == boxes[0][i] and boxes[1][i] == 0:
            # adjust boxes array
            score += boxes[0][i]+boxes[2][i]
            boxes[2][i] = boxes[0][i]+boxes[2][i]
            boxes[0][i] = 0
        # combine (into row 4)
        elif boxes[0][i] != 0 and boxes[3][i] == boxes[0][i] and boxes[1][i] == 0 and boxes[2][i] == 0:
            # adjust boxes array
            score += boxes[0][i]+boxes[3][i]
            boxes[3][i] = boxes[0][i]+boxes[3][i]
            boxes[0][i] = 0

        # move down (into row 4)
        elif boxes[0][i] != 0 and boxes[3][i] == 0 and boxes[1][i] == 0 and boxes[2][i] == 0:
            # adjust boxes array
            boxes[3][i] = boxes[0][i]
            boxes[0][i] = 0
        elif boxes[0][i] != 0 and boxes[2][i] == 0 and boxes[1][i] == 0:
            # adjust boxes array
            boxes[2][i] = boxes[0][i]
            boxes[0][i] = 0
        # move down (into row 2)
        elif boxes[0][i] != 0 and boxes[1][i] == 0:
            # adjust boxes array
            boxes[1][i] = boxes[0][i]
            boxes[0][i] = 0
    return score

def moveRight(window, boxes, score):
    # 3rd col
    for i in range(4):
        # combine
        if boxes[i][2] != 0 and boxes[i][3] == boxes[i][2]:
            # adjust boxes array
            score += boxes[i][2]+boxes[i][3]
            boxes[i][3] = boxes[i][2]+boxes[i][3]
            boxes[i][2] = 0

        # move right
        elif boxes[i][2] != 0 and boxes[i][3] == 0:
            # adjust boxes array
            boxes[i][3] = boxes[i][2]
            boxes[i][2] = 0
    # 2nd col
    for i in range(4):
        # combine (into col 2)
        if boxes[i][1] != 0 and boxes[i][2] == boxes[i][1]:
            # adjust boxes array
            score += boxes[i][1]+boxes[i][2]
            boxes[i][2] = boxes[i][1]+boxes[i][2]
            boxes[i][1] = 0
        # combine (into col 3)
        elif boxes[i][1] != 0 and boxes[i][3] == boxes[i][1] and boxes[i][2] == 0:
            # adjust boxes array
            score += boxes[i][1]+boxes[i][3]
            boxes[i][3] = boxes[i][1]+boxes[i][3]
            boxes[i][1] = 0

        # move right (into col 3)
        elif boxes[i][1] != 0 and boxes[i][3] == 0 and boxes[i][2] == 0:
            # adjust boxes array
            boxes[i][3] = boxes[i][1]
            boxes[i][1] = 0
        # move right (into col 2)
        elif boxes[i][1] != 0 and boxes[i][2] == 0:
            # adjust boxes array
            boxes[i][2] = boxes[i][1]
            boxes[i][1] = 0
    # 1nd col
    for i in range(4):
        # combine (into col 1)
        if boxes[i][0] != 0 and boxes[i][1] == boxes[i][0]:
            # adjust boxes array
            score += boxes[i][0]+boxes[i][1]
            boxes[i][1] = boxes[i][0]+boxes[i][1]
            boxes[i][0] = 0
        # combine (into col 2)
        elif boxes[i][0] != 0 and boxes[i][2] == boxes[i][0] and boxes[i][1] == 0:
            # adjust boxes array
            score += boxes[i][0]+boxes[i][2]
            boxes[i][2] = boxes[i][0]+boxes[i][2]
            boxes[i][0] = 0
        # combine (into col 3)
        elif boxes[i][0] != 0 and boxes[i][3] == boxes[i][0] and boxes[i][1] == 0 and boxes[i][2] == 0:
            # adjust boxes array
            score += boxes[i][0]+boxes[i][3]
            boxes[i][3] = boxes[i][0]+boxes[i][3]
            boxes[i][0] = 0

        # move right (into col 3)
        elif boxes[i][0] != 0 and boxes[i][3] == 0 and boxes[i][1] == 0 and boxes[i][2] == 0:
            # adjust boxes array
            boxes[i][3] = boxes[i][0]
            boxes[i][0] = 0
        # move right (into col 2)
        elif boxes[i][0] != 0 and boxes[i][2] == 0 and boxes[i][1] == 0:
            # adjust boxes array
            boxes[i][2] = boxes[i][0]
            boxes[i][0] = 0
        # move right (into col 1)
        elif boxes[i][0] != 0 and boxes[i][1] == 0:
            # adjust boxes array
            boxes[i][1] = boxes[i][0]
            boxes[i][0] = 0
    return score

def moveLeft(window, boxes, score):
    # 2nd col
    for i in range(4):
        # combine
        if boxes[i][1] != 0 and boxes[i][0] == boxes[i][1]:
            # adjust boxes array
            score += boxes[i][1]+boxes[i][0]
            boxes[i][0] = boxes[i][1]+boxes[i][0]
            boxes[i][1] = 0

        # move right
        elif boxes[i][1] != 0 and boxes[i][0] == 0:
            # adjust boxes array
            boxes[i][0] = boxes[i][1]
            boxes[i][1] = 0
    # 3rd col
    for i in range(4):
        # combine (into 2 col)
        if boxes[i][2] != 0 and boxes[i][0] == boxes[i][2] and boxes[i][1] == 0:
            # adjust boxes array
            score += boxes[i][2]+boxes[i][0]
            boxes[i][0] = boxes[i][2]+boxes[i][0]
            boxes[i][2] = 0
        # combine (into 1 col)
        elif boxes[i][2] != 0 and boxes[i][1] == boxes[i][2]:
            # adjust boxes array
            score += boxes[i][2]+boxes[i][1]
            boxes[i][1] = boxes[i][2]+boxes[i][1]
            boxes[i][2] = 0

        # move right (into 1 col)
        elif boxes[i][2] != 0 and boxes[i][0] == 0 and boxes[i][1] == 0:
            # adjust boxes array
            boxes[i][0] = boxes[i][2]
            boxes[i][2] = 0
        # move right (into 2 col)
        elif boxes[i][2] != 0 and boxes[i][1] == 0:
            # adjust boxes array
            boxes[i][1] = boxes[i][2]
            boxes[i][2] = 0
    # 3rd col
    for i in range(4):
        # combine (into 3 col)
        if boxes[i][3] != 0 and boxes[i][2] == boxes[i][3]:
            # adjust boxes array
            score += boxes[i][3]+boxes[i][2]
            boxes[i][2] = boxes[i][3]+boxes[i][2]
            boxes[i][3] = 0
        # combine (into 2 col)
        elif boxes[i][3] != 0 and boxes[i][1] == boxes[i][3] and boxes[i][2] == 0:
            # adjust boxes array
            score += boxes[i][3]+boxes[i][1]
            boxes[i][1] = boxes[i][3]+boxes[i][1]
            boxes[i][3] = 0
        # combine (into 1 col)
        elif boxes[i][3] != 0 and boxes[i][0] == boxes[i][3] and boxes[i][1] == 0 and boxes[i][2] == 0:
            # adjust boxes array
            score += boxes[i][3]+boxes[i][0]
            boxes[i][0] = boxes[i][3]+boxes[i][0]
            boxes[i][3] = 0

        # move right (into 1 col)
        elif boxes[i][3] != 0 and boxes[i][0] == 0 and boxes[i][1] == 0 and boxes[i][2] == 0:
            # adjust boxes array
            boxes[i][0] = boxes[i][3]
            boxes[i][3] = 0
        # move right (into 2 col)
        elif boxes[i][3] != 0 and boxes[i][1] == 0 and boxes[i][2] == 0:
            # adjust boxes array
            boxes[i][1] = boxes[i][3]
            boxes[i][3] = 0
        # move right (into 3 col)
        elif boxes[i][3] != 0 and boxes[i][2] == 0:
            # adjust boxes array
            boxes[i][2] = boxes[i][3]
            boxes[i][3] = 0
    return score

def drawAll(window, boxes, score):
    clearBoard(window)
    # draw all boxes
    for i in range(4):
        for j in range(4):
            if boxes[i][j] != 0:
                fillBox(window, (i*4)+j, boxes[i][j], boxes)

    # update score
    my_font = pygame.font.SysFont('arial', 40, bold=True)
    scoreboard = my_font.render("Score: "+str(score), False, (0, 0, 0))
    window.blit(scoreboard, (50, 30))

def checkLoss(boxes):
    loss = True
    
    if not np.any(boxes.flatten() == 0):
        # check rows
        for i in range(4):
            for j in range(3):
                if boxes[i][j] == boxes[i][j+1]:
                    loss = False
                    break
        
        # check cols
        if loss:
            for i in range(4):
                for j in range(3):
                    if boxes[j][i] == boxes[j+1][i]:
                        loss = False
                        break
    else:
        loss = False
    
    return loss

def checkWin(boxes):
    win = False
    
    if np.any(boxes.flatten() == 2048):
        win = True
    
    return win