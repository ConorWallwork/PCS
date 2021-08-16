from sys import stdin, stdout

for _ in range( int(input()) ):

    letters = input()
    length = len(letters)
    i = 0
    o_then_k = False
    while(letters[i] != 'O'):
        i += 1
        if i == length: break

    while( i < length):
        if letters[i] == "K":
            o_then_k = True
            break
        i += 1

    print("YES" if o_then_k else "NO")
