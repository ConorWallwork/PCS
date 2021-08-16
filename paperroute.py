from sys import stdin, stdout

for _ in range(int(input())):
    nhouses = int(input())
    max = 0
    profits = [int(i) for i in input().split()]
    for x in range(nhouses):
        if profits[x] <= 0: continue
        thissubarray = 0
        for y in range(x, nhouses):
            thissubarray += profits[y]
            if thissubarray > max: max = thissubarray

    print(str(max))


