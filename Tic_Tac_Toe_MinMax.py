def check():

    # For player 1
    if board['C1'] == 'X' and board['C2'] == 'X' and board['C3'] == 'X':
        return 1,'p1'
    if board['C4'] == 'X' and board['C5'] == 'X' and board['C6'] == 'X':
        return 1,'p1'
    if board['C7'] == 'X' and board['C8'] == 'X' and board['C9'] == 'X':
        return 1,'p1'
    if board['C1'] == 'X' and board['C4'] == 'X' and board['C7'] == 'X':
        return 1,'p1'
    if board['C2'] == 'X' and board['C5'] == 'X' and board['C8'] == 'X':
        return 1,'p1'
    if board['C3'] == 'X' and board['C6'] == 'X' and board['C9'] == 'X':
        return 1,'p1'
    if board['C1'] == 'X' and board['C5'] == 'X' and board['C9'] == 'X':
        return 1,'p1'
    if board['C3'] == 'X' and board['C5'] == 'X' and board['C7'] == 'X':
        return 1,'p1'


    # For player 2
    if board['C1'] == 'O' and board['C2'] == 'O' and board['C3'] == 'O':
        return 1,'p2'
    if board['C4'] == 'O' and board['C5'] == 'O' and board['C6'] == 'O':
        return 1,'p2'
    if board['C7'] == 'O' and board['C8'] == 'O' and board['C9'] == 'O':
        return 1,'p2'
    if board['C1'] == 'O' and board['C4'] == 'O' and board['C7'] == 'O':
        return 1,'p2'
    if board['C2'] == 'O' and board['C5'] == 'O' and board['C8'] == 'O':
        return 1,'p2'
    if board['C3'] == 'O' and board['C6'] == 'O' and board['C9'] == 'O':
        return 1,'p2'
    if board['C1'] == 'O' and board['C5'] == 'O' and board['C9'] == 'O':
        return 1,'p2'
    if board['C3'] == 'O' and board['C5'] == 'O' and board['C7'] == 'O':
        return 1,'p2'

    return 0,''


def com_minimax(board, isMaximizing):
    win_check,player_won = check()

    if win_check == 1:
        if(player_won=='p2'):
            return 1
        elif(player_won=='p1'):
            return -1

    elif ' ' not in board.values():
        return 0

    if (isMaximizing):
        bestScore = -1
        for pos in board.keys():
            if (board[pos] == ' '):
                board[pos] = 'O'
                score = com_minimax(board, False)
                board[pos] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 1
        for pos in board.keys():
            if (board[pos] == ' '):
                board[pos] = 'X'
                score = com_minimax(board, True)
                board[pos] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore


# Body of the program
import random
print(' 1| 2| 3')
print('--+--+--')
print(' 4| 5| 6')
print('--+--+--')
print(' 7| 8| 9\n')
print('***************************')

total_moves = 0
win_check = 0

board = {
    'C1': ' ', 'C2': ' ', 'C3': ' ',
    'C4': ' ', 'C5': ' ', 'C6': ' ',
    'C7': ' ', 'C8': ' ', 'C9': ' '
}

print("Please Chose mode of game : ")
print("1. Play with Smart Computer(Minmax)")
print("2. Play with friend")
mode = input("Please enter your choice : ")


if mode == '2':
    player = '1'
    while True:
        print(board['C1'] + '|' + board['C2'] + '|' + board['C3'])
        print('-+-+-')
        print(board['C4'] + '|' + board['C5'] + '|' + board['C6'])
        print('-+-+-')
        print(board['C7'] + '|' + board['C8'] + '|' + board['C9'])
        win_check,player_won = check()

        if win_check == 1:
            if(player_won=='p1'):
                print("Player-1 win the game")
                break
            elif(player_won=='p2'):
                print("Player-2 win the game")
                break

        if win_check == 0 and total_moves==9:
            print("Game Tie !")
            break

        while True:
            if player == '1':
                p1_input = 'C' + input('Player one Enter your move [1 - 9]: ')
                if p1_input.upper() in board and board[p1_input.upper()] == ' ':
                    board[p1_input.upper()] = 'X'
                    player = '2'
                    break
                else:
                    print('Invalid input !')
                    continue
            else:
                p2_input = 'C' + input('Player two Enter your move [1 - 9]: ')
                if p2_input.upper() in board and board[p2_input.upper()] == ' ':
                    board[p2_input.upper()] = 'O'
                    player = '1'
                    break
                else:
                    print('Invalid input !')
                    continue


        total_moves += 1
        print('***************************')
        print()

elif mode == '1':
    while True:
        player = input("Please Chose Your Turn 1 or 2 : ")
        if player == '1' or player == '2':
            break
        else:
            print("Invalid input !")
    
    while True:
        print(board['C1'] + '|' + board['C2'] + '|' + board['C3'])
        print('-+-+-')
        print(board['C4'] + '|' + board['C5'] + '|' + board['C6'])
        print('-+-+-')
        print(board['C7'] + '|' + board['C8'] + '|' + board['C9'])
        win_check,player_won = check()
        
        if win_check == 1:
            if(player_won=='p1'):
                print("Player-1 win the game")
                break
            elif(player_won=='p2'):
                print("Computer win the game")
                break

        if win_check == 0 and total_moves==9:
            print("Game Tie !")
            break

        while True:
            if player == '1':
                p1_input = 'C' + input('Your Turn Enter your move [1-9]: ')
                if p1_input.upper() in board and board[p1_input.upper()] == ' ':
                    board[p1_input.upper()] = 'X'
                    player = '2'
                    break
                else:
                    print('Invalid input !')
                    continue
            else:
                bestScore = -1
                bestMove = 0
                for pos in board.keys():
                    if (board[pos] == ' '):
                        board[pos] = 'O'
                        score = com_minimax(board, False)
                        board[pos] = ' '
                        if (score > bestScore):
                            bestScore = score
                            bestMove = pos
                board[bestMove] = 'O'
                player = '1'
                print(f"Computer's Move : {bestMove}")
                break

        total_moves += 1
        print('***************************')
        print()

else:
    print("Please chose valid game mode !")