# -*- coding: utf-8 -*-
"""
Created on Sat May 05 12:32:19 2018

@author: Mohinish
"""
INFINITY = 10000

def minimax( node, isMAXTurn, alpha, beta):
    
    if isTerminalNode(node):
        return getTerminalValue(node)
    
    """ Since computer plays as a maximizing player,
        we're interested in keeping a track of the
        moves made, so that best move can be returned."""
    if isMAXTurn:
        bestValue = -1*INFINITY
        moveDictionary = fetchChildNodes(node,node.MAX_PLAYER)
        for move, child in moveDictionary.items():
            value = minimax(child,False,alpha,beta)
            if bestValue < value:
                bestValue = value
                node.bestComputerMove = move
            alpha = max( alpha, bestValue)
            if beta <= alpha:
                break      
        return bestValue
    
    else:
        bestValue = INFINITY
        moveDictionary = fetchChildNodes(node,node.MIN_PLAYER)
        for move, child in moveDictionary.items():
            value = minimax(child,True,alpha,beta)
            bestValue = min( bestValue, value)
            beta = min( beta, bestValue)
            if beta <= alpha:
                break       
        return bestValue

def fetchChildNodes( node , player):
    possibleMoves = node.getPossibleMoves()
    childNodes = node.generateGameStates( possibleMoves , player)
    return dict(zip(possibleMoves,childNodes))
    
def isTerminalNode( node ):
    return node.isGameFinished()
    
def getTerminalValue( node ):
    return node.calculateTerminalScore()