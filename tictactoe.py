import cv2 as cv
import numpy as np
from random import choice

def setup():
    """
    Sets up the moves array

    Inputs:
    - None

    Outputs:
    - moves(2d array)

    example:
    >>> moves = setup()
    >>> print(moves)
    [[3, 4, 5,
    6, 7, 8,
    9, 10, 11]]
    """
    moves = np.arange(3,12)    # creates the array of possible moves
    moves.shape = (3,3)

    #input("X's or O's")
    return(moves)

def detect(moves):
    """
    Detects where a move has been played, then evaluates where that is and removes it from being able to be played from the moves array

    Inputs:
    - moves(2d array)

    Outputs:
    - ref(reference image, game board, NumPy array)
    - moves(2d array with removed moves)

    Example:
    >>> a = detect(m)
    >>> print(a)
    {array (a)}, {array (ref)}
    """
    def draw_circle(event,x,y,flags,param):
        if event == cv.EVENT_LBUTTONDBLCLK:
            cv.circle(current_board, (x,y), 45, (255,255,255), 5)

    cv.namedWindow("image")
    cv.setMouseCallback("image", draw_circle)

    current_board = cv.imread("tictactoe.png")    # reads both the user-played image and the reference image
    reference = cv.imread("tictactoe_ref.png")
    current_board = cv.cvtColor(current_board, cv.COLOR_BGR2GRAY)    # converts both images to B&W
    reference = cv.cvtColor(reference, cv.COLOR_BGR2GRAY)

    while(1):
        cv.imshow("image", current_board)
        if cv.waitKey(20) & 0xFF == 27:
            break
    cv.destroyAllWindows()

    mask1 = reference != current_board    # creates a mask of where the reference board does not match the current board, to determine where a move has been played
    new_board = np.zeros((512,512), np.uint8)    # creates an empty board in order to store the new moves

    for x in range(512):    # scans the board for where the two original boards match
        for y in range(512):
         if mask1[x,y] == True:
                new_board[x, y] = 255
                continue
    
    cv.imshow("new board", new_board)
    k = cv.waitKey(0)

    if k == ord("s"):
        print("key pressed")
        cv.destroyAllWindows()
    
    row = [np.arange(0,166), np.arange(174,336), np.arange(344, 512)]    # scans each section of the board for where a move has been played
    col = [np.arange(0,166), np.arange(174,336), np.arange(344, 512)]
    for r in range(len(row)):
        for c in range(len(col)):
            for y in row[r]:
                for x in col[c]:
                    if mask1[x,y] == True:
                        moves[c,r] = 0
                        continue

    ref = current_board
    cv.imshow('ref board', ref)
    k = cv.waitKey(0)

    if k == ord("s"):
        print("neat")
        #cv.imwrite("tictactoe_ref.png", ref)
        cv.imwrite("tictactoe.png", ref)
        cv.destroyAllWindows()
    
    return(ref, moves)

def next_move(ref, moves):
    """
    Uses the input information to determine where to play next.

    Inputs:
    - ref(The reference image, NumPy array)
    - moves(2d array)

    Outputs:
    - ref(The updated reference image with the new move, NumPy array)
    - moves(Updated 2d array with available moves)

    Example:
    >>> a = next_move(ref, moves)
    >>> print(a)
    [{NumPy array (ref)}, {NumPy array (moves)}]
    """
    mask = moves != 0    # creates a mask of playable moves
    moves2 = moves[mask]    # creates a new array of only playable moves
    c = choice(moves2)    # chooses a random value from the updated choices list

    if c == 3:    # uses the chosen value to determine where to place an "X"
        cv.line(ref, (11,11), (155,155), (255,255,255), 5)
        cv.line(ref, (11,155), (155,11), (255,255,255), 5)
    elif c == 4:
        cv.line(ref, (185,11), (325,155), (255,255,255), 5)
        cv.line(ref, (185,155), (325,11), (255,255,255), 5)
    elif c == 5:
        cv.line(ref, (355,11), (500,155), (255,255,255), 5)
        cv.line(ref, (355,155), (500,11), (255,255,255), 5)
    elif c == 6:
        cv.line(ref, (11,185), (155,325), (255,255,255), 5)
        cv.line(ref, (11,325), (155,185), (255,255,255), 5)
    elif c == 7:
        cv.line(ref, (185,185), (325,325), (255,255,255), 5)
        cv.line(ref, (185,325), (325,185), (255,255,255), 5)
    elif c == 8:
        cv.line(ref, (355,185), (500,325), (255,255,255), 5)
        cv.line(ref, (355,325), (500,185), (255,255,255), 5)
    elif c == 9:
        cv.line(ref, (11,355), (155,500), (255,255,255), 5)
        cv.line(ref, (11,500), (155,355), (255,255,255), 5)
    elif c == 10:
        cv.line(ref, (185,355), (325,500), (255,255,255), 5)
        cv.line(ref, (185,500), (325,355), (255,255,255), 5)
    elif c == 11:
        cv.line(ref, (355,355), (500,500), (255,255,255), 5)
        cv.line(ref, (355,500), (500,355), (255,255,255), 5)
    
    loc = np.where(moves == c)
    moves[loc] = 0

    cv.imshow("test",ref)
    k = cv.waitKey(0)
    if k == ord("s"):
        print("yay")
        cv.imwrite("tictactoe.png", ref)
        cv.destroyAllWindows()

    return(ref, moves)

def reset():
    """
    reset() resets the game board to a blank state

    Inputs:
    - None

    Outputs:
    - None

    Example:
    >>> reset()
    "Game has been reset"
    """
    img = np.zeros((512,512), np.uint8)

    cv.line(img, (170,0), (170,512), (255,255,255), 5)
    cv.line(img, (340,0), (340,512), (255,255,255), 5)
    cv.line(img, (0,170), (512,170), (255,255,255), 5)
    cv.line(img, (0,340), (512,340), (255,255,255), 5)

    cv.imwrite("tictactoe_ref.png", img)
    cv.imwrite("tictactoe.png", img)
    print("Game has been reset")

    #cv.imshow("Testing", img)
    #k = cv.waitKey(0)

    #if k == ord("s"):
        #cv.imwrite("tictactoe_ref.png", img)
        #cv.imwrite("tictactoe.png", img)
    
    return

def detect2():     # ignore this, it was a testing tree
    current_board = cv.imread("tictactoe.png")
    reference = cv.imread("tictactoe_ref.png")
    current_board = cv.cvtColor(current_board, cv.COLOR_BGR2GRAY)
    reference = cv.cvtColor(reference, cv.COLOR_BGR2GRAY)

    moves = np.arange(3,12)
    moves.shape = (3,3)

    loc = np.where(reference != current_board)
    mask1 = reference != current_board
    new_board = np.zeros((512,512), np.uint8)

    #new_board[loc] = 255

    #print(loc)

    for x in range(512):
        for y in range(512):
            if mask1[x,y] == True:
                new_board[x, y] = 255
                continue

    #print(new_board)
    cv.imshow("Test 1", new_board)
    k = cv.waitKey(0)

    if k == ord("s"):
        print("key pressed")
        cv.destroyAllWindows()

    row = [np.arange(0,166), np.arange(174,336), np.arange(344, 512)]
    col = [np.arange(0,166), np.arange(174,336), np.arange(344, 512)]
    for r in range(len(row)):
        for c in range(len(col)):
            for y in row[r]:
                for x in col[c]:
                    if mask1[x,y] == True:
                        moves[c,r] = 0

    print(moves)
    mask4 = moves != 0
    moves = moves[mask4]

    c = choice(moves)
    ref = current_board
    cv.imshow("test 2", ref)
    k = cv.waitKey(0)
    if k == ord('s'):
        cv.destroyAllWindows
    print("hello")
    return(ref, moves)