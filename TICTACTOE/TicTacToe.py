import random


class TicTacToe:
    
    def __init__(self):
        self.board = [['-','-','-'],
                    ['-','-','-'],
                    ['-','-','-']]
    
    def get_random_first_player(self):
        return random.randint(0,1)
                    
    def print_board(self):
        for row in self.board:
            for item in row:
                print(item,end=" ")
            print()
        
    def check_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True 
        
    def fix_spot(self,row,col,player):
        self.board[row][col] = player
        
    def player_win(self,player):
        win = None
        n = len(self.board)
        
        #checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win
                
        #checking coloumns  
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win
                
        #checking diagonals  
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win  
            
        win = True
        for i in range(n):
            if self.board[i][n-1-i] != player:
                win = False
                break
        if win:
            return win 
        return False
        
    def swap_player(self,player):
        return 'X' if player == 'O' else 'O'    
        
    def start(self):
        
        player = 'X' if self.get_random_first_player() == 1 else 'O'
        
        while True:
            print('Player {} turn'.format(player))
            
            self.print_board()
            
            #taking input
            row,col = list(map(int,input("Enter row and coloumn values to fix spot: ").split()))
            print('\n')
            
            #fixing spot
            self.fix_spot(row - 1, col - 1, player)
            
            #check if current player won
            if self.player_win(player):
                print("Player {} wins the game!".format(player))
                break
            
            #check if match is draw
            if self.check_board_filled():
                print("Match Draw!")
                break
            
            #swap player turn
            player = self.swap_player(player)
            
        #final board view
        print()
        self.print_board()
        
            
Tic_Tac_Toe = TicTacToe()     
Tic_Tac_Toe.start()