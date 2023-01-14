import pygame as p
from const import *
import os


os.chdir(os.path.dirname(os.path.abspath(__file__)))




IMAGES = {}
def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK',
              'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        IMAGES[piece] = p.transform.scale(p.image.load(
            "images/" + piece + ".png"), (SQUARE_SIZE, SQUARE_SIZE))

def drawPieces(screen, board):
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            piece = board[row][column]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(
                    column * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

