import random

piece_score = {"K": 0, "Q": 9, "R": 5, "B": 3, "N": 3, "p": 1}

king_endgame_scores =   [[-0.1, 0, 0.1, 0.2, 0.2, 0.1, 0, -0.1],
                         [0.1, 0.2, 0.3, 0,0, 0.3, 0.2, 0.1],
                         [0.1, 0.3, 0.5, 0.6, 0.6, 0.5, 0.3, 0.1],
                         [0.1, 0.3, 0.6, 0.7, 0.7, 0.6, 0.3, 0.1],
                         [0.1, 0.3, 0.6, 0.7, 0.7, 0.6, 0.3, 0.1],
                         [0.1, 0.3, 0.5, 0.6, 0.6, 0.5, 0.3, 0.1],
                         [0.1, 0.1, 0.4, 0.4, 0.4, 0.4, 0.1, 0.1],
                         [-0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, -0.1]]

knight_scores = [[0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0],
                 [0.1, 0.3, 0.5, 0.5, 0.5, 0.5, 0.3, 0.1],
                 [0.2, 0.5, 0.6, 0.65, 0.65, 0.6, 0.5, 0.2],
                 [0.2, 0.55, 0.65, 0.7, 0.7, 0.65, 0.55, 0.2],
                 [0.2, 0.5, 0.65, 0.7, 0.7, 0.65, 0.5, 0.2],
                 [0.2, 0.55, 0.6, 0.65, 0.65, 0.6, 0.55, 0.2],
                 [0.1, 0.3, 0.5, 0.55, 0.55, 0.5, 0.3, 0.1],
                 [0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0]]

bishop_scores = [[0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0],
                 [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                 [0.2, 0.4, 0.5, 0.6, 0.6, 0.5, 0.4, 0.2],
                 [0.2, 0.5, 0.5, 0.6, 0.6, 0.5, 0.5, 0.2],
                 [0.2, 0.4, 0.6, 0.6, 0.6, 0.6, 0.4, 0.2],
                 [0.2, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.2],
                 [0.2, 0.5, 0.4, 0.4, 0.4, 0.4, 0.5, 0.2],
                 [0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0]]

rook_scores = [[0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
               [0.5, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.5],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
               [0.25, 0.25, 0.25, 0.5, 0.5, 0.25, 0.25, 0.25]]

queen_scores = [[0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0],
                [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                [0.2, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2],
                [0.3, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3],
                [0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3],
                [0.2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2],
                [0.2, 0.4, 0.5, 0.4, 0.4, 0.4, 0.4, 0.2],
                [0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0]]

pawn_scores = [[0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
               [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
               [0.3, 0.3, 0.4, 0.5, 0.5, 0.4, 0.3, 0.3],
               [0.25, 0.25, 0.3, 0.45, 0.45, 0.3, 0.25, 0.25],
               [0.2, 0.2, 0.2, 0.4, 0.4, 0.2, 0.2, 0.2],
               [0.25, 0.15, 0.1, 0.2, 0.2, 0.1, 0.15, 0.25],
               [0.25, 0.3, 0.3, 0.0, 0.0, 0.3, 0.3, 0.25],
               [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]]

piece_position_scores = {"wN": knight_scores,
                         "bN": knight_scores[::-1],
                         "wB": bishop_scores,
                         "bB": bishop_scores[::-1],
                         "wQ": queen_scores,
                         "bQ": queen_scores[::-1],
                         "wR": rook_scores,
                         "bR": rook_scores[::-1],
                         "wp": pawn_scores,
                         "bp": pawn_scores[::-1],
                         "wK": king_endgame_scores,
                         "bK": king_endgame_scores[::-1]}

CHECKMATE = 1000
STALEMATE = 0
DEPTH = 3

# Heuristic 1
def getMaterialScore(game_state, weight):
    white_score = 0
    black_score = 0
    for row in range(len(game_state.board)):
        for col in range(len(game_state.board[row])):
            piece = game_state.board[row][col]
            if piece != "--":
                if piece[0] == "w":
                    white_score += piece_score[piece[1]]
                else:
                    black_score += piece_score[piece[1]]
    if white_score <= 19 or black_score <= 19:
        game_state.inEndGame = True                
    return (white_score - black_score) * weight

# Heuristic 2
def getPiecePositionScore(game_state, weight):
    score = 0
    for row in range(len(game_state.board)):
        for col in range(len(game_state.board[row])):
            piece = game_state.board[row][col]
            if piece != "--":
                if piece[0] == "w":
                    if game_state.inEndGame == False:
                        if piece[1] != "K":
                            score += piece_position_scores[piece][row][col]
                    else:
                        score += piece_position_scores[piece][row][col]
                if piece[0] == "b":
                    if game_state.inEndGame == False:
                        if piece[1] != "K":
                            score -= piece_position_scores[piece][row][col]
                    else:
                        score -= piece_position_scores[piece][row][col]
    return score * weight

# Heuristic 3 
def inCheckScore(game_state, weight):
    score = 0
    if game_state.white_to_move:
        if game_state.in_check:
            score -= 1
    else:
        if game_state.in_check:
            score += 1
    return score * weight

# Heuristic 4
def pawnStructureScore(game_state, weight):
    score = 0
    board = game_state.board
    for row in range(len(board)):
        cntPawn = 0 
        for col in range(len(board[row])):
            piece = board[row][col]
            if piece == "bp":
                if row >= 1 and col >= 1 and board[row-1][col-1] == "bp":
                    score -= 1
                if row >= 1 and col <= 6 and board[row-1][col+1] == "bp":
                    score -= 1
            if board[col][row] == "bp": 
                cntPawn += 1
        if cntPawn >= 2:
            score += cntPawn
    return score * weight

# Heuristic 5
def kingProtection(game_state, weight):
    score = 0
    board = game_state.board
    whiteSurrounding = 0
    blackSurrounding = 0
    black_row = game_state.black_king_location[0]
    black_col = game_state.black_king_location[1]
    for i in range(black_row-1, black_row+2):
        for j in range(black_col-1, black_col+2):
            if i>=0 and i<=7 and j>=0 and j<=7:
                if board[i][j][0] == "b":
                    blackSurrounding += 1
    white_row = game_state.white_king_location[0]
    white_col = game_state.white_king_location[1]
    for i in range(white_row-1, white_row+2):
        for j in range(white_col-1, white_col+2):
            if i>=0 and i<=7 and j>=0 and j<=7:
                if board[i][j][0] == "w":
                    whiteSurrounding += 1
    score = (whiteSurrounding - blackSurrounding) * weight
    return score * weight
    

def findBestMove(game_state, valid_moves, return_queue):
    global next_move
    next_move = None
    random.shuffle(valid_moves)
    AlphaBeta(game_state, valid_moves, DEPTH, -CHECKMATE, CHECKMATE, True if game_state.white_to_move else False)
    return_queue.put(next_move)


def AlphaBeta(game_state, valid_moves, depth, alpha, beta, maximizing):
    global next_move
    if depth == 0:
        return scoreBoard(game_state)

    if(maximizing):
        best_score = -CHECKMATE
        for move in valid_moves:
            game_state.makeMove(move)
            next_moves = game_state.getValidMoves()
            score = AlphaBeta(game_state,next_moves, depth - 1, alpha, beta, False)
            if score > best_score:
                best_score = score
                if depth == DEPTH:
                    next_move = move
            game_state.undoMove()
            alpha = max(alpha, best_score)
            if(beta<=alpha):
                break
        return best_score
    else:
        best_score = CHECKMATE
        for move in valid_moves:
            game_state.makeMove(move)
            next_moves = game_state.getValidMoves()
            score = AlphaBeta(game_state,next_moves, depth - 1, alpha, beta, True)
            if score < best_score:
                best_score = score
                if depth == DEPTH:
                    next_move = move
            game_state.undoMove()
            beta = min(beta, best_score)
            if(beta<=alpha):
                break
        return best_score



def scoreBoard(game_state):
    """
    Score the board. A positive score is good for white, a negative score is good for black.
    """
    if game_state.checkmate:
        if game_state.white_to_move:
            return -CHECKMATE  # black wins
        else:
            return CHECKMATE  # white wins
    elif game_state.stalemate:
        return STALEMATE
    score = 0    
    score += getMaterialScore(game_state, 100)
    score += getPiecePositionScore(game_state, 80)
    score += inCheckScore(game_state, 2)
    score += pawnStructureScore(game_state, 2)
    score += kingProtection(game_state, 1)
    return score


def findRandomMove(valid_moves):
    """
    Picks and returns a random valid move.
    """
    return random.choice(valid_moves)
