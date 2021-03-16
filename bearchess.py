from sys import stdin, stdout


def bearChess(R, C, mat):

    max = min(R-1,C-1)
    highest = 0

    for i in range(R):
        for j in range(C):
            if(mat[i][j] == 1): continue
            if(R == 1 or C == 1):
                return 0 if mat[i][j] == 1 else 1
            submatrix = [[mat[x][y] for y in range(C) if y != j] for x in range(R) if x != i]
            subhighest = bearChess(R-1, C-1, submatrix)
            if(subhighest == max):
                return 1 + max
            else:
                if subhighest + 1 > highest:
                    highest = subhighest + 1
    return highest


T = int(input())

for _ in range(T):
    R,C = input().split()
    R = int(R)
    C = int(C)

    mat = [[int(i) for i in input().split()] for j in range(R)]

    print(bearChess(R, C, mat))
