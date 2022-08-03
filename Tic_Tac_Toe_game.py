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
    return 0,'tie'


def computer(mode,total_moves):
    if mode == '1':
        # When 1st Turn Aquire Any Corner
        if total_moves==0:
            while True:
                temp = str(random.randint(1,4))
                if temp == '1' and board['C1'] == ' ':
                    return 1,'C1'
                if temp == '2' and board['C3'] == ' ':
                    return 1,'C3'
                if temp == '3' and board['C7'] == ' ':
                    return 1,'C7'
                if temp == '4' and board['C9'] == ' ':
                    return 1,'C9'

        # When Second Turn of computer
        if total_moves==1 and board['C5'] == ' ':
            return 1,'C5'

    # Trying To Win

    # Horizontal
    if board['C1'] == 'O' and board['C2'] == 'O' and board['C3'] == ' ':
        return 1,'C3'
    if board['C1'] == ' ' and board['C2'] == 'O' and board['C3'] == 'O':
        return 1,'C1'
    if board['C1'] == 'O' and board['C2'] == ' ' and board['C3'] == 'O':
        return 1,'C2'
    if board['C4'] == 'O' and board['C5'] == 'O' and board['C6'] == ' ':
        return 1,'C6'
    if board['C4'] == ' ' and board['C5'] == 'O' and board['C6'] == 'O':
        return 1,'C4'
    if board['C4'] == 'O' and board['C5'] == ' ' and board['C6'] == 'O':
        return 1,'C5'
    if board['C7'] == 'O' and board['C8'] == 'O' and board['C9'] == ' ':
        return 1,'C9'
    if board['C7'] == ' ' and board['C8'] == 'O' and board['C9'] == 'O':
        return 1,'C7'
    if board['C7'] == 'O' and board['C8'] == ' ' and board['C9'] == 'O':
        return 1,'C8'

    # Vartical    
    if board['C1'] == 'O' and board['C4'] == 'O' and board['C7'] == ' ':
        return 1,'C7'
    if board['C1'] == ' ' and board['C4'] == 'O' and board['C7'] == 'O':
        return 1,'C1'
    if board['C1'] == 'O' and board['C4'] == ' ' and board['C7'] == 'O':
        return 1,'C4'
    if board['C2'] == 'O' and board['C5'] == 'O' and board['C8'] == ' ':
        return 1,'C8'
    if board['C2'] == ' ' and board['C5'] == 'O' and board['C8'] == 'O':
        return 1,'C2'
    if board['C2'] == 'O' and board['C5'] == ' ' and board['C8'] == 'O':
        return 1,'C5'
    if board['C3'] == 'O' and board['C6'] == 'O' and board['C9'] == ' ':
        return 1,'C9'
    if board['C3'] == ' ' and board['C6'] == 'O' and board['C9'] == 'O':
        return 1,'C3'
    if board['C3'] == 'O' and board['C6'] == ' ' and board['C9'] == 'O':
        return 1,'C6'

    # Diagonal
    if board['C1'] == 'O' and board['C5'] == 'O' and board['C9'] == ' ':
        return 1,'C9'
    if board['C1'] == ' ' and board['C5'] == 'O' and board['C9'] == 'O':
        return 1,'C1'
    if board['C1'] == 'O' and board['C5'] == ' ' and board['C9'] == 'O':
        return 1,'C5'
    if board['C3'] == 'O' and board['C5'] == 'O' and board['C7'] == ' ':
        return 1,'C7'
    if board['C3'] == ' ' and board['C5'] == 'O' and board['C7'] == 'O':
        return 1,'C3'
    if board['C3'] == 'O' and board['C5'] == ' ' and board['C7'] == 'O':
        return 1,'C5'


    # Block Opponent To Win

    # Horizontal
    if board['C1'] == 'X' and board['C2'] == 'X' and board['C3'] == ' ':
        return 1,'C3'
    if board['C1'] == ' ' and board['C2'] == 'X' and board['C3'] == 'X':
        return 1,'C1'
    if board['C1'] == 'X' and board['C2'] == ' ' and board['C3'] == 'X':
        return 1,'C2'
    if board['C4'] == 'X' and board['C5'] == 'X' and board['C6'] == ' ':
        return 1,'C6'
    if board['C4'] == ' ' and board['C5'] == 'X' and board['C6'] == 'X':
        return 1,'C4'
    if board['C4'] == 'X' and board['C5'] == ' ' and board['C6'] == 'X':
        return 1,'C5'
    if board['C7'] == 'X' and board['C8'] == 'X' and board['C9'] == ' ':
        return 1,'C9'
    if board['C7'] == ' ' and board['C8'] == 'X' and board['C9'] == 'X':
        return 1,'C7'
    if board['C7'] == 'X' and board['C8'] == ' ' and board['C9'] == 'X':
        return 1,'C8'

    # Vartical    
    if board['C1'] == 'X' and board['C4'] == 'X' and board['C7'] == ' ':
        return 1,'C7'
    if board['C1'] == ' ' and board['C4'] == 'X' and board['C7'] == 'X':
        return 1,'C1'
    if board['C1'] == 'X' and board['C4'] == ' ' and board['C7'] == 'X':
        return 1,'C4'
    if board['C2'] == 'X' and board['C5'] == 'X' and board['C8'] == ' ':
        return 1,'C8'
    if board['C2'] == ' ' and board['C5'] == 'X' and board['C8'] == 'X':
        return 1,'C2'
    if board['C2'] == 'X' and board['C5'] == ' ' and board['C8'] == 'X':
        return 1,'C5'
    if board['C3'] == 'X' and board['C6'] == 'X' and board['C9'] == ' ':
        return 1,'C9'
    if board['C3'] == ' ' and board['C6'] == 'X' and board['C9'] == 'X':
        return 1,'C3'
    if board['C3'] == 'X' and board['C6'] == ' ' and board['C9'] == 'X':
        return 1,'C6'

    # Diagonal
    if board['C1'] == 'X' and board['C5'] == 'X' and board['C9'] == ' ':
        return 1,'C9'
    if board['C1'] == ' ' and board['C5'] == 'X' and board['C9'] == 'X':
        return 1,'C1'
    if board['C1'] == 'X' and board['C5'] == ' ' and board['C9'] == 'X':
        return 1,'C5'
    if board['C3'] == 'X' and board['C5'] == 'X' and board['C7'] == ' ':
        return 1,'C7'
    if board['C3'] == ' ' and board['C5'] == 'X' and board['C7'] == 'X':
        return 1,'C3'
    if board['C3'] == 'X' and board['C5'] == ' ' and board['C7'] == 'X':
        return 1,'C5'


    if mode == '1':
        # Prevent Opponent to Win:
        if board['C5'] == 'O':
            # Strategy : When Opponent Aquires corner in 1st turn and computer aquires center in secornd turn then IF Opponent Aquires Opposite corner of 1st aquired corner or then computer have to aquire any center of any edge to prevent to opponent to win
            if ((board['C1'] == 'X' and board['C9'] == 'X') or (board['C3'] == 'X' and board['C7'] == 'X')):
                while True:
                    temp = str(random.randint(1,4))
                    if temp == '1' and board['C2'] == ' ':
                        return 1,'C2'
                    if temp == '2' and board['C4'] == ' ':
                        return 1,'C4'
                    if temp == '3' and board['C6'] == ' ':
                        return 1,'C6'
                    if temp == '4' and board['C8'] == ' ':
                        return 1,'C8'

            # Strategy : When Opponent Aquires corner in 1st turn and computer aquires center in secornd turn then IF Opponent Aquires Center of opposite edge then computer have to aquire corner of Two edges aquire by opponent to Block opponent to win
            elif (board['C7'] == 'X' and board['C6'] == 'X') or (board['C3'] == 'X' and board['C8'] == 'X'):
                return 1,'C9'
            elif (board['C7'] == 'X' and board['C2'] == 'X') or (board['C3'] == 'X' and board['C4'] == 'X'):
                return 1,'C1'
            elif (board['C1'] == 'X' and board['C6'] == 'X') or (board['C9'] == 'X' and board['C2'] == 'X'):
                return 1,'C3'
            elif (board['C1'] == 'X' and board['C8'] == 'X') or (board['C9'] == 'X' and board['C4'] == 'X'):
                return 1,'C7'


        # Win Statagies -- Acquire corners if empty
        # When 1st turn of computer and Opponent Aquires Center
        elif board['C5'] == 'X':
            # Strategy-1 To cover corner
            if board['C1'] == 'O' and board['C9'] == ' ':
                return 1,'C9'

            if board['C9'] == 'O' and board['C1'] == ' ':
                return 1,'C1'

            if board['C3'] == 'O' and board['C7'] == ' ':
                return 1,'C7'

            if board['C7'] == 'O' and board['C3'] == ' ':
                return 1,'C3'

        if board['C1'] == ' ' or board['C3'] == ' ' or board['C7'] == ' ' or board['C9'] == ' ':
            while True:
                temp = str(random.randint(1,4))
                if temp == '1' and board['C1'] == ' ':
                    return 1,'C1'
                if temp == '2' and board['C3'] == ' ':
                    return 1,'C3'
                if temp == '3' and board['C7'] == ' ':
                    return 1,'C7'
                if temp == '4' and board['C9'] == ' ':
                    return 1,'C9'

    else:
        return 0,None


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
print("1. Play with Smart Computer")
print("2. Play with friend")
print("3. Play with Normal Computer")
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

elif mode == '1' or mode == '3':
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
                flag,p2_input = computer(mode,total_moves)
                if flag:
                    print('Computer')
                    board[p2_input] = 'O'
                    player = '1'
                    break
                else:
                    p2_input = str(random.randint(1,9))
                    p2_input = 'C'+p2_input
                    if board[p2_input] == ' ':
                        print('Computer')
                        board[p2_input] = 'O'
                        player = '1'
                        break
                    else:
                        continue

        total_moves += 1
        print('***************************')
        print()

else:
    print("Please chose valid game mode !")