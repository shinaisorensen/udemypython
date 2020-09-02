# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 18:27:21 2020

@author: Shinai
@date: September 2, 2020

This class creates a player with a total amount of money, a hand and number of points
"""


class Player():
   
    def __init__(self,total):
        self.total = total # Total amount of money the player has
        self.hand = []
        self.points = 0
        
    
    
    