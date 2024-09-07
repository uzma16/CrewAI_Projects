
# class Player:
#     def __init__(self, letter):
#         self.letter = letter

#     def get_move(self, game):
#         pass

# class HumanPlayer(Player):
#     def __init__(self, letter):
#         super().__init__(letter)

#     def get_move(self, game):
#         valid_square = False
#         val = None
#         while not valid_square:
#             square = input(self.letter + '\'s Turn. Input move (0-8): ')
#             try:
#                 val = int(square)
#                 if val not in game.available_moves():
#                     raise ValueError
#                 valid_square = True
#             except ValueError:
#                 print('Invalid square. Try again.')
#         return val

# class RandomComputerPlayer(Player):
#     def __init__(self, letter):
#         super().__init__(letter)

#     def get_move(self, game):
#         import random
#         square = random.choice(game.available_moves())
#         return square

# class TicTacToe:
#     def __init__(self):
#         self.board = [' ' for _ in range(9)]
#         self.current_winner = None

#     def print_board(self):
#         for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
#             print('| ' + ' | '.join(row) + ' |')

#     def available_moves(self):
#         return [i for i, spot in enumerate(self.board) if spot == ' ']

#     def empty_squares(self):
#         return ' ' in self.board

#     def num_empty_squares(self):
#         return self.board.count(' ')

#     def make_move(self, square, letter):
#         if self.board[square] == ' ':
#             self.board[square] = letter
#             if self.winner(square, letter):
#                 self.current_winner = letter
#             return True
#         return False

#     def winner(self, square, letter):
#         row_ind = square // 3
#         row = self.board[row_ind*3:(row_ind+1)*3]
#         if all([spot == letter for spot in row]):
#             return True
#         col_ind = square % 3
#         column = [self.board[col_ind+i*3] for i in range(3)]
#         if all([spot == letter for spot in column]):
#             return True
#         if square % 2 == 0:
#             diagonal1 = [self.board[i] for i in [0, 4, 8]]
#             if all([spot == letter for spot in diagonal1]):
#                 return True
#             diagonal2 = [self.board[i] for i in [2, 4, 6]]
#             if all([spot == letter for spot in diagonal2]):
#                 return True
#         return False


# def play(game, x_player, o_player, print_game=True):
#     if print_game:
#         game.print_board()
#         letter = 'X'
#         while game.empty_squares():
#             if letter == 'O':
#                 square = o_player.get_move(game)
#             else:
#                 square = x_player.get_move(game)
#             if game.make_move(square, letter):
#                 if print_game:
#                     print(letter + ' makes a move to square {}'.format(square))
#                     game.print_board()
#                     print('')
#                 if game.current_winner:
#                     if print_game:
#                         print(letter + ' wins!')
#                     return letter
#                 letter = 'O' if letter == 'X' else 'X'
#         if print_game:
#             print('It\'s a tie!')

# if __name__ == '__main__':
#     x_player = HumanPlayer('X')
#     o_player = RandomComputerPlayer('O')
#     t = TicTacToe()
#     play(t, x_player, o_player, print_game=True)



board = [' ' for x in range(10)]

def insertBoard(letter, pos):
    global board
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)

def playerMove():
    run = True
    while run:
        move = input("Please select a position to place an 'X' (1-9): ")
        try:
            move  = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertBoard('X', move)
                else:
                    print('This postion is already occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print("Welcome to Tic Tac Toe!")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('O\'s win this time...')
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print(' ')
            else:
                insertBoard('O', move)
                print('Computer placed an \'O\' in position', move , ':')
                printBoard(board)
        else:
            print('X\'s win, good job!')
            break

        if isBoardFull(board):
            print('Tie Game!')
            break

    if isWinner(board, 'O'):
        print('O\'s win this time...')
    elif isWinner(board, 'X'):
        print('X\'s win, good job!')
    else:
        print('Tie Game!')

main()