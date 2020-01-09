# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 18:41:10 2020

@author: Mohinish

GAME BOARD :
    
|   |   |   |
-------------
|   |   |   |
-------------
|   |   |   |
 
The board above represents how buttons will be 
placed in a 3 x 3 grid.

"""

from tkinter import Frame, Button, DISABLED, messagebox
import tkinter.font as font
from TicTacToe import TicTacToe
import AIUtil as AI
import copy
import simpleaudio as sa

class App:
    
    def __init__(self, master):
        self.game = TicTacToe()
        self.master = master
        self.frame = Frame(self.master)
        self.frame.pack()
        self.compMoveSound = sa.WaveObject.from_wave_file('compMove.wav')
        self.customFont = font.Font(family='Helvetica', size=12, weight="bold")
        self.tiles = [Button(self.frame, font = self.customFont, text = "", width=10, height=4) for _ in range(9)]
        self.origButtonColor = self.tiles[0].cget("background")
        for i in range(3):
            for j in range(3):      
                self.tiles[3*i+j].config(command=lambda k = 3*i+j : self.playMove('O', k))
                self.tiles[3*i+j].grid(row=i,column=j)
                
    def playMove(self, player, tileIndex):
        self.tiles[tileIndex].config(text=player, state = DISABLED)
        self.game.executeMove(tileIndex, 'O')
        if self.game.isGameFinished():
            if self.game.calculateTerminalScore() != 0:
                self.highlightWin('O')
                messagebox.showinfo("Game won", "You won !")
            else:
                messagebox.showinfo("Game Drawn", "Draw !")
            self.resetGame()
        else :
            self.playComputerMove()
    
    def playComputerMove(self):
        gameState = copy.deepcopy(self.game)
        AI.minimax( gameState, True, -1*AI.INFINITY, AI.INFINITY)
        self.game.executeMove( gameState.bestComputerMove, 'X' )
        sound = self.compMoveSound.play()
        sound.wait_done()
        self.tiles[int(gameState.bestComputerMove)].config(text='X', state = DISABLED)
        if self.game.isGameFinished():
            if self.game.calculateTerminalScore() != 0:
                self.highlightWin('X')
                messagebox.showinfo("Game lost", "You Lost :( ")
            else:
                messagebox.showinfo("Game Drawn", "Draw !")
            self.resetGame()
    
    def highlightWin(self, player):
        index = self.game.winOrientationIndex
        bgColor = ''
        if player == 'X':
            bgColor = 'red'
        else:
            bgColor = 'blue'
        if self.game.winOrientation == 'row':
            for offset in range(3):
                self.tiles[3*index+offset].configure(bg=bgColor)
        elif self.game.winOrientation == 'col':
            for offset in range(3):
                self.tiles[index+3*offset].configure(bg=bgColor)
        else:
            self.tiles[4].configure(bg=bgColor)
            if index == 0:
                self.tiles[0].configure(bg=bgColor)
                self.tiles[8].configure(bg=bgColor)
            else:
                self.tiles[2].configure(bg=bgColor)
                self.tiles[6].configure(bg=bgColor)
    
    def resetGame(self):
        for tileIndex in range(9):
            self.tiles[tileIndex].config(text="", state = "normal", bg=self.origButtonColor)
            self.game.resetGameData()