import pygame as p
import operation
import ai
import sys
from multiprocessing import Process, Queue
from piece import *
from gameState import *
from playWithAIState import *


def playWithPerson():
    p.init()
    screen = p.display.set_mode(
        (BOARD_WIDTH + MOVE_LOG_PANEL_WIDTH, BOARD_HEIGHT))
    clock = p.time.Clock()
    
    screen.fill(p.Color("white"))
    game_state = operation.GameState()
    valid_moves = game_state.getValidMoves()
    move_made = False  # flag variable for when a move is made
    animate = False  # flag variable for when we should animate a move
    loadImages()  # do this only once before while loop
    running = True
    # no square is selected initially, this will keep track of the last click of the user (tuple(row,col))
    square_selected = ()
    player_clicks = []  # this will keep track of player clicks (two tuples)
    game_over = False
    move_undone = False
    move_finder_process = None
    move_log_font = p.font.SysFont("Arial", 14, False, False)
    player_one = True  # if a human is playing white, then this will be True, else False
    player_two = False  # if a human is playing black, then this will be True, else False

    while running:

        for e in p.event.get():
            if e.type == p.QUIT:
                p.quit()
                sys.exit()
            # mouse handler
            elif e.type == p.MOUSEBUTTONDOWN:
                if not game_over:
                    location = p.mouse.get_pos()  # (x, y) location of the mouse
                    col = location[0] // SQUARE_SIZE
                    row = location[1] // SQUARE_SIZE
                    # user clicked the same square twice
                    if square_selected == (row, col) or col >= 8:
                        square_selected = ()  # deselect
                        player_clicks = []  # clear clicks
                    else:
                        square_selected = (row, col)
                        # append for both 1st and 2nd click
                        player_clicks.append(square_selected)
                    if len(player_clicks) == 2:  # after 2nd click
                        move = operation.Move(
                            player_clicks[0], player_clicks[1], game_state.board)
                        for i in range(len(valid_moves)):
                            if move == valid_moves[i]:
                                game_state.makeMove(valid_moves[i])
                                move_made = True
                                animate = True
                                square_selected = ()  # reset user clicks
                                player_clicks = []
                        if not move_made:
                            player_clicks = [square_selected]

            # key handler
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:  # undo when 'z' is pressed
                    game_state.undoMove()
                    move_made = True
                    animate = False
                    game_over = False
                    # if ai_thinking:
                    #     move_finder_process.terminate()
                    #     ai_thinking = False
                    move_undone = True
                if e.key == p.K_r:  # reset the game when 'r' is pressed
                    game_state = operation.GameState()
                    valid_moves = game_state.getValidMoves()
                    square_selected = ()
                    player_clicks = []
                    move_made = False
                    animate = False
                    game_over = False


        if move_made:
            if animate:
                animateMove(game_state.move_log[-1],
                            screen, game_state.board, clock)
            valid_moves = game_state.getValidMoves()
            move_made = False
            animate = False
            move_undone = False

        drawGameState(screen, game_state, valid_moves, square_selected)
        if not game_over:
            drawMoveLog(screen, game_state, move_log_font)

            

        
        if game_state.checkmate:
            game_over = True
            if game_state.white_to_move:
                drawEndGameText(screen, "Bạn thua")
            else:
                drawEndGameText(screen, "Bạn thắng")

        elif game_state.stalemate:
            game_over = True
            drawEndGameText(screen, "Stalemate")

        clock.tick(MAX_FPS)
        p.display.flip()
