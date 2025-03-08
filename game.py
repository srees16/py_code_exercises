from player import HumanPlayer, RandomComputerPlayer
import time
import math

class TicTacToe():

    def __init__(self):
        self.board = self.make_board()
        self.winner = None # to keep track of winner
    
    @staticmethod
    def make_board():
        return [' ' for _ in range(9)] # we will use single list to represent 3x3 board
    
    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| '+' | '.join(row)+' |')
    
    @staticmethod
    def print_board_numbers():
        # 0 | 1 | 2 etc, tells us what number corresponds to what box
        num_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in num_board:
            print('| ' + ' | '.join(row)+' |')
    
    def available_moves(self):
        '''moves = []
        for (i, spot) in enumerate(self.board):
            if spot == ' ':
                moves.append(i)
        return moves'''
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.board
    
    def no_of_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        # if move is valid, then make a move (assign square to letter) and return true, if invalid then return false
        if self.board[square] == '':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # winner if 3 in a row anywhere, we need to check all the possibilities
        # first lets check the row
        row_index = math.floor(square / 3)
        row = self.board[row_index*3: (row_index+1) * 3]
        if all([spot == letter for spot in row]):
            return True
        # check column
        col_index = square % 3
        column = [self.board[col_index+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        # check diagonals but only if the square is an even number (0,2,4,6,8)
        # these are the only moves possible to win a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]] # top left to bottom right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]] # top right to bottom right diagonal
            if all([spot == letter for spot in diagonal2]):
                return True
        # if all above checks fail
        return False


def play(game, x_player, o_player, print_game=True):
    # returns winner of the game (letter of winner) or None for a tie
    if print_game:
        game.print_board_numbers()

    letter = 'X' # starting letter
    #iterate while the game is still incomplete and has empty squares
    while game.empty_squares():
        # get the move from appropriate player
        if letter == 'o':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        # define function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter+' makes a move to square {}'.format(square))
                game.print_board()
                print('') # empty line
            if game.current_winner:
                if print_game:
                    print(letter+' wins!')
                return letter
            # after we make a move, alternate letters
            letter = 'O' if letter == 'X' else 'X'
        # tiny pause
        time.sleep(0.8)

    #check who won?
    if print_game:
        print('Its a tie')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)