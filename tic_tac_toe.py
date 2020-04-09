# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 11:22:50 2020

@author: Rakesh
"""

import os
os.system("clear")

class Board():
    def __init__(self):
        self.cells = [" "," "," "," "," "," "," "," "," "," "]
        
    def display(self):
        
        print()
        print(" %s | %s | %s " %(self.cells[1],self.cells[2],self.cells[3]))
        print("------------")
        print(" %s | %s | %s " %(self.cells[4],self.cells[5],self.cells[6]))
        print("------------")
        print(" %s | %s | %s " %(self.cells[7],self.cells[8],self.cells[9]))
        print()
        
    def update_cell(self,cell_no, player):
        
        if self.cells[cell_no] ==" ":
            self.cells[cell_no] = player
            
    def is_winner(self,player):
        
        for combo in [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]:
            result = True
            for cell_no in combo:
                if self.cells[cell_no] != player:
                    result = False
                    
            if result:
                return True
        return False
        
        
    def reset(self):
        self.cells = [" "," "," "," "," "," "," "," "," "," "]
        
    def is_tie(self):
        used_cells = 0
        for cell in self.cells:
            if cell!= " ":
                used_cells += 1
        if used_cells == 9:
            return True
        else:
            return False
        
    def ai_move(self,player):
        
        if self.cells[5] == " ":
            self.update_cell(5,player)
        elif (self.cells[2] == "O" and self.cells[3] == "O" and self.cells[1] == " ") or (self.cells[4] == "O" and self.cells[7] == "O" and self.cells[1] == " ") or (self.cells[5] == "O" and self.cells[9] == "O" and self.cells[1] == " "):
            self.update_cell(1,player)
        elif (self.cells[1] == "O" and self.cells[3] == "O" and self.cells[2] == " ") or (self.cells[5] == "O" and self.cells[8] == "O" and self.cells[2] == " "):
            self.update_cell(2,player)
            
        elif (self.cells[1] == "O" and self.cells[2] == "O" and self.cells[3] == " ") or (self.cells[6] == "O" and self.cells[9] == "O" and self.cells[3] == " ") or (self.cells[5] == "O" and self.cells[7] == "O" and self.cells[3] == " "):
            self.update_cell(3,player)
            
        elif (self.cells[1] == "O" and self.cells[7] == "O" and self.cells[4] == " ") or (self.cells[5] == "O" and self.cells[6] == "O" and self.cells[4] == " "):
            self.update_cell(4,player)
        
        elif (self.cells[1] == "O" and self.cells[9] == "O" and self.cells[5] == " ") or (self.cells[2] == "O" and self.cells[8] == "O" and self.cells[5] == " ") or (self.cells[3] == "O" and self.cells[7] == "O" and self.cells[5] == " ") or (self.cells[4] == "O" and self.cells[6] == "O" and self.cells[5] == " "):
            self.update_cell(5,player)
            
        elif (self.cells[4] == "O" and self.cells[5] == "O" and self.cells[6] == " ") or (self.cells[3] == "O" and self.cells[9] == "O" and self.cells[6] == " "):
            self.update_cell(6,player)
            
        elif (self.cells[1] == "O" and self.cells[4] == "O" and self.cells[7] == " ") or (self.cells[3] == "O" and self.cells[5] == "O" and self.cells[7] == " ") or (self.cells[8] == "O" and self.cells[9] == "O" and self.cells[0] == " "):
            self.update_cell(7,player)
            
        elif (self.cells[2] == "O" and self.cells[5] == "O" and self.cells[8] == " ") or (self.cells[7] == "O" and self.cells[9] == "O" and self.cells[8] == " "):
            self.update_cell(8,player)
            
        elif (self.cells[1] == "O" and self.cells[5] == "O" and self.cells[9] == " ") or (self.cells[3] == "O" and self.cells[6] == "O" and self.cells[9] == " ") or (self.cells[7] == "O" and self.cells[8] == "O" and self.cells[9] == " "):
            self.update_cell(9,player)
    
            #AI Blocks
        elif (self.cells[2] == "X" and self.cells[3] == "X" and self.cells[1] == " ") or (self.cells[4] == "X" and self.cells[7] == "X" and self.cells[1] == " ") or (self.cells[5] == "X" and self.cells[9] == "X" and self.cells[1] == " "):
            self.update_cell(1,player)
        elif (self.cells[1] == "X" and self.cells[3] == "X" and self.cells[2] == " ") or (self.cells[5] == "X" and self.cells[8] == "X" and self.cells[2] == " "):
            self.update_cell(2,player)
            
        elif (self.cells[1] == "X" and self.cells[2] == "X" and self.cells[3] == " ") or (self.cells[6] == "X" and self.cells[9] == "X" and self.cells[3] == " ") or (self.cells[5] == "X" and self.cells[7] == "X" and self.cells[3] == " "):
            self.update_cell(3,player)
            
        elif (self.cells[1] == "X" and self.cells[7] == "X" and self.cells[4] == " ") or (self.cells[5] == "X" and self.cells[6] == "X" and self.cells[4] == " "):
            self.update_cell(4,player)
        
        elif (self.cells[1] == "X" and self.cells[9] == "X" and self.cells[5] == " ") or (self.cells[2] == "X" and self.cells[8] == "X" and self.cells[5] == " ") or (self.cells[3] == "X" and self.cells[7] == "X" and self.cells[5] == " ") or (self.cells[4] == "X" and self.cells[6] == "X" and self.cells[5] == " "):
            self.update_cell(5,player)
            
        elif (self.cells[4] == "X" and self.cells[5] == "X" and self.cells[6] == " ") or (self.cells[3] == "X" and self.cells[9] == "X" and self.cells[6] == " "):
            self.update_cell(6,player)
            
        elif (self.cells[1] == "X" and self.cells[4] == "X" and self.cells[7] == " ") or (self.cells[3] == "X" and self.cells[5] == "X" and self.cells[7] == " ") or (self.cells[8] == "X" and self.cells[9] == "X" and self.cells[0] == " "):
            self.update_cell(7,player)
            
        elif (self.cells[2] == "X" and self.cells[5] == "X" and self.cells[8] == " ") or (self.cells[7] == "X" and self.cells[9] == "X" and self.cells[8] == " "):
            self.update_cell(8,player)
            
        elif (self.cells[1] == "X" and self.cells[5] == "X" and self.cells[9] == " ") or (self.cells[3] == "X" and self.cells[6] == "X" and self.cells[9] == " ") or (self.cells[7] == "X" and self.cells[8] == "X" and self.cells[9] == " "):
            self.update_cell(9,player)
        else:
            #choose Random
            for i in range(1,10):
                if self.cells[i] == " ":
                    print("executing\n")
                    self.update_cell(i,player)
                    break
        
board = Board()
print("\n<-- INSTRUCTIONS -->\n")
print("There are 2 modes available in the game\n\n1.Single player (choose 'S')\n2.Multi player(choose 'M').\n Kindly follow the instructions in the game.\n")
def print_header():
    print("\nWelcome To Tic Tac Toe\n")
    
def refresh_screen():
    
    #clear the screen
    os.system("clear")
    
    #prints welcome screen
    print_header()
    
    #to show the board
    board.display()
    
mode = input("\nsingle player or multiplayer.(S/M) >").upper()

while True:
    
    refresh_screen()
    
    #get x input
    x_choice = int(input("\nX : Please choose 1 - 9. > "))
    
    while (x_choice <1 and x_choice>9) or board.cells[x_choice] != " ":
        print("\n You entered wrong input\n")
        x_choice = int(input("\nX : Please choose 1 - 9. > "))
        
        
    
    #update board
    board.update_cell(x_choice,"X")
    
    #to refresh the screen
    refresh_screen()
    
    #check for an X win
    if board.is_winner("X"):
        print("\n<-- X Won the Game -->\n")
        play_again = input("would you like to play again? (Y/N)> ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break
        
    #check for Tie
    if board.is_tie():
        print("\n<-- Tie Game -->\n")
        play_again = input("would you like to play again? (Y/N)> ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break
        
    if mode == "S":
        board.ai_move("O")
        
    else:
        #get O input
        o_choice = int(input("\nO : Please choose 1 - 9. > "))
        while (x_choice <1 and x_choice>9) or board.cells[x_choice] != " ":
            print("\n You entered wrong input\n")
            x_choice = int(input("\nX : Please choose 1 - 9. > "))
        
        #update board
        board.update_cell(o_choice,"O")
        
    #to refresh the screen
    refresh_screen()
    
    #check for an O win
    if board.is_winner("O"):
        print("\n<-- O Won the Game -->\n")
        play_again = input("Would you like to play again? (Y/N)> ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break
        
    #check for Tie
    if board.is_tie():
        print("\n<-- Tie Game -->\n")
        play_again = input("would you like to play again? (Y/N)> ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break
    
        