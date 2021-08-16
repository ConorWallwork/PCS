from sys import stdin, stdout




def maximumSubArray(arr):

    while arr[0] < 0:
        del arr[0]
        if arr == []:
            return 0
    ## TRIM THE LEADING NEGATIVES

    if arr == []:
        return 0
    ## THERE WERE NO POSITIVE HOUSES


    while arr[-1] < 0:
        del arr[-1]

    ## TRIM THE TRAILING NEGATIVES


    profit = 0
    i = 0
    while arr[i] >= 0:
        profit += arr[i]
        i += 1
        if i == len(arr):
            return profit
    ## FIND THE SUM OF THE LEFT SIDE CONTIGUOUS POSITIVE HOUSES



    cost = 0
    while arr[i] < 0:
        cost += arr[i]
        i += 1
    ## FIND THE SUM OF THE NEGATIVE HOUSES BETWEEN THE POSITIVES AND THE SUB ARRAY

    subarray = arr[i:]
    submax = maximumSubArray(subarray)
    return max(submax, profit, submax + profit + cost)



for _ in range(int(input())):
    nhouses = int(input())
    if nhouses == 0:
        continue
    profits = [int(i) for i in input().split()]
    max = maximumSubArray(profits)
    print(str(max))

