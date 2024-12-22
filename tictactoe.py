"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY,EMPTY, EMPTY],
            [EMPTY, EMPTY,EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num_X=0
    num_O=0
    if terminal(board):
        return "game already over"
    for i in range(3):
        for j in range(3):
            if board[i][j]==X:
                num_X+=1
            elif board[i][j]==O:
                num_O+=1
    if board==initial_state() or num_O==num_X:
        num_X+=1
        return X
    elif num_X>num_O:
        num_O+=1
        return O
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions=set()
    if terminal(board):
        return "game already over"
    for row in range(3):
        for cell in range(3):
            if board[row][cell]==EMPTY:
                possible_actions.add((row,cell))
    return possible_actions
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]]!=EMPTY or terminal(board):
        raise Exception("cell Error")
    else:
        play=player(board)
        new_board=copy.deepcopy(board)
        new_board[action[0]][action[1]]=play
        return new_board
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0]!=EMPTY and board[i][0]==board[i][1] and board[i][1]==board[i][2]:
            if board[i][0]==X:
                return X
            else:
                return O
        elif board[0][i]!=EMPTY and board[0][i]==board[1][i] and board[1][i]==board[2][i]:
            if board[0][i] == X:
                return X
            else:
                return O
        elif board[i][i]!=EMPTY and board[0][0]==board[1][1]==board[2][2]:
            if board[0][0] == X:
                return X
            else:
                return O
        elif board[0][2]!=EMPTY and board[0][2]==board[1][1]==board[2][0]:
            if board[0][2] == X:
                return X
            else:
                return O
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if any(EMPTY in row for row in board)!=True:
        return True
    for i in range(3):
        if board[i][0]!=EMPTY and board[i][0]==board[i][1] and board[i][1]==board[i][2]:
            return True
        elif board[0][i]!=EMPTY and board[0][i]==board[1][i] and board[1][i]==board[2][i]:
            return True
        elif board[i][i]!=EMPTY and board[0][0]==board[1][1]==board[2][2]:
            return True
        elif board[0][2]!=EMPTY and board[0][2]==board[1][1]==board[2][0]:
            return True
    return False
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    play=player(board)
    optimal_action=None
    if play==X:
        max_action=-10
        for action in actions(board):
            new_board=copy.deepcopy(board)
            new_board[action[0]][action[1]]=X
            value=min_value(new_board)
            if value>=max_action:
                max_action=value
                optimal_action=action
    else:
        min_action = 10
        for action in actions(board):
            new_board = copy.deepcopy(board)
            new_board[action[0]][action[1]] = O
            value = max_value(new_board)
            if value <= min_action:
                min_action = value
                optimal_action=action
    return optimal_action
def max_value(board):
    v=-10
    if terminal(board):
        return utility(board)
    else:
        for action in actions(board):
            v=max(v,min_value(result(board,action)))
        return v
def min_value(board):
    v=10
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v=min(v, max_value(result(board, action)))
    return v
def main ():
    optimal=minimax(initial_state())
    print(optimal)
