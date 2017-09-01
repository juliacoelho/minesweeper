#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 00:31:12 2017

@author: julia
"""

from random import randint

class Matrix:
    def __init__(self, n):
        self.n = n
        self.createMatrix(self.n)
        
    def createMatrix(self, n):
        self.matrix = []
        for i in range(n):
            self.matrix.append(["-"]*n)
            
    def getMatrix(self):
        for line in self.matrix:
            print(line)
            
    def insertBombs(self, n):
        for x in range(n):
            i = randint(0, self.n-1)
            j = randint(0, self.n-1)
            self.matrix[i][j] = "X"
    
    def returnMatrix(self):
        return self.matrix
    
    def insertNumbers(self):
        for i in range(self.n):
            for j in range(self.n):
                adjBombs = 0
                for a in [i - 1, i, i + 1]:
                    for b in [j - 1, j, j + 1]:
                        if (a == i and b == j):
                            continue
                        if (a >= 0 and b >= 0 and a < self.n and b < self.n):
                            if (self.matrix[a][b] == "X"):
                                adjBombs += 1
                if (self.matrix[i][j] != "X"):
                    self.matrix[i][j] = str(adjBombs)
                    

class Game:
    
    def __init__(self, sizeMatrix, nbBombs):
        self.sizeMatrix = sizeMatrix
        self.matrix = Matrix(self.sizeMatrix)
        self.nbBombs = nbBombs
        self.matrix.insertBombs(self.nbBombs)
        self.matrix.insertNumbers()
        self.answers = self.matrix.returnMatrix()
        self.display = []
        self.createMatrix(self.sizeMatrix)
        self.getDisplayMatrix()
    
    def createMatrix(self, n):
        for i in range(n):
            self.display.append(["-"]*n)
    
    def getDisplayMatrix(self):
        for line in self.display:
            print(line)

    def reveal(self, i, j):
        if (self.display[i][j] != "*"):
            self.display[i][j] = self.answers[i][j]
        if (self.answers[i][j] == "X" and self.display[i][j] != "*"):
            self.getDisplayMatrix()
            print("GAME OVER!!!")
            self.gameOver()
        elif (self.answers[i][j] == "0"):
            for a in [i - 1, i, i + 1]:
                for b in [j - 1, j, j + 1]:
                    if (a >= 0 and b >= 0 and a < self.sizeMatrix and b < self.sizeMatrix):
                        if (a == i and b == j):
                            continue
                        elif (self.display[a][b] == "-"):
                            self.reveal(a, b)
    
    def play(self, i, j):
        self.reveal(i, j)
        self.getDisplayMatrix()
        if (self.display == []):
            input("Press Enter to start a new game!")
            self.newGame()
    
    def gameOver(self):
        self.display = []
        
    def newGame(self):
        self.matrix.createMatrix(self.sizeMatrix)
        self.matrix.insertBombs(self.nbBombs)
        self.matrix.insertNumbers()
        self.answers = self.matrix.returnMatrix()
        self.createMatrix(self.sizeMatrix)
        self.getDisplayMatrix()
    
    def mark(self, i, j):
        if (self.display[i][j] == "-"):
            self.display[i][j] = "*"
        self.getDisplayMatrix()
    
    def unmark(self, i, j):
        if (self.display[i][j] == "*"):
            self.display[i][j] = "-"
        self.getDisplayMatrix()




g = Game(5, 5)