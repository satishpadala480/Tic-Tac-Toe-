def printboard(board):
    print("*"*20)
    for row in board:
        print("   |".join(row))
        print("-"*15)
    print("*"*20)
def isfull(board):
    for row in board:
        for col in row:
            if col=="":
                return False
    else:
        return True
def check(board,p):
    for row in board:
        if row[0]==p and row[1]==p and row[2]==p:
            return True
    for i in range(3):
        if board[0][i]==p and board[1][i]==p and board[2][i]==p:
            return true
    if board[1][1]==p and board[2][2]==p and board[0][0]==p:
        return True
    if board[0][2]==p and board[1][1]==p and board[2][0]==p:
        return True


    
board=[[""]*3 for i in range(3)]
print("welcome to game,tic tac toe")
printboard(board)
print("player - x and 0")
current='x'
while True:
    print("current player is",current)
    print("enter the dimension")
    x,y=map(int,input().split())
    if -1<x<3 and -1<y<3:
        if board[x][y]=="":
            board[x][y]=current
            printboard(board)
            if check(board,current):
                print("congrats",current,"wins")
                break
            if isfull(board):
                print("Game is draw")
                break
                board[x][y]=current
                printboard(board)
            if current=="x":
                current="0"
            else:
                current="x"
    else:
        print("enter a valid no")
